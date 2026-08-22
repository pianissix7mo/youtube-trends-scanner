#!/usr/bin/env python3
"""Run the hybrid scanner with persistent caching for YouTube deep checks.

YouTube search.list has a small independent daily quota. Re-running the scanner
while tuning filters should not spend another search call for the same keyword.
This wrapper caches the expensive per-keyword YouTube metrics and monkey-patches
the existing scanner without changing its ranking/discovery logic.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

import hybrid_scan
import scan


ROOT = Path(__file__).resolve().parent
CACHE_PATH = ROOT / ".cache" / "youtube_competition.json"
CACHE_TTL_HOURS = max(1.0, float(os.getenv("YOUTUBE_CACHE_TTL_HOURS", "12")))
STALE_FALLBACK_HOURS = max(
    CACHE_TTL_HOURS,
    float(os.getenv("YOUTUBE_STALE_FALLBACK_HOURS", "48")),
)
METRIC_FIELDS = (
    "recent_video_estimate",
    "median_views",
    "median_views_per_day",
    "small_channel_hit_rate",
)

ORIGINAL_YOUTUBE_COMPETITION = scan.youtube_competition
QUOTA_EXHAUSTED = False


def load_cache() -> dict[str, dict[str, Any]]:
    try:
        data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


CACHE = load_cache()


def cache_key(candidate: scan.Candidate) -> str:
    keyword = " ".join(candidate.keyword.lower().split())
    return f"{candidate.geo}|{candidate.language}|{keyword}"


def age_hours(entry: dict[str, Any]) -> float:
    saved_at = str(entry.get("saved_at") or "")
    if not saved_at:
        return float("inf")
    try:
        stamp = datetime.fromisoformat(saved_at.replace("Z", "+00:00"))
    except ValueError:
        return float("inf")
    return max(0.0, (datetime.now(timezone.utc) - stamp).total_seconds() / 3600.0)


def hydrate(candidate: scan.Candidate, entry: dict[str, Any]) -> None:
    for field in METRIC_FIELDS:
        setattr(candidate, field, entry.get(field))


def save_candidate(candidate: scan.Candidate) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE[cache_key(candidate)] = {
        "saved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        **{field: getattr(candidate, field) for field in METRIC_FIELDS},
    }
    CACHE_PATH.write_text(
        json.dumps(CACHE, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def is_quota_error(exc: Exception) -> bool:
    text = str(exc).lower()
    if isinstance(exc, requests.HTTPError) and exc.response is not None:
        try:
            text += " " + exc.response.text.lower()
        except Exception:
            pass
    quota_markers = (
        "quota",
        "dailylimitexceeded",
        "ratelimitexceeded",
        "search quota",
    )
    return any(marker in text for marker in quota_markers)


def cached_youtube_competition(candidate: scan.Candidate, api_key: str) -> None:
    global QUOTA_EXHAUSTED

    key = cache_key(candidate)
    entry = CACHE.get(key)
    age = age_hours(entry) if entry else float("inf")

    if entry and age <= CACHE_TTL_HOURS:
        hydrate(candidate, entry)
        print(
            f"[youtube-cache] fresh {candidate.keyword!r} "
            f"({age:.1f}h old; no search.list call)"
        )
        return

    # Once the daily search quota is known to be exhausted, never waste more
    # live calls in this run. Prefer a slightly older cached sample if available.
    if QUOTA_EXHAUSTED:
        if entry and age <= STALE_FALLBACK_HOURS:
            hydrate(candidate, entry)
            print(
                f"[youtube-cache] stale fallback {candidate.keyword!r} "
                f"({age:.1f}h old; quota exhausted)"
            )
            return
        raise RuntimeError("YouTube search quota exhausted and no cached metrics available")

    try:
        ORIGINAL_YOUTUBE_COMPETITION(candidate, api_key)
    except Exception as exc:
        if is_quota_error(exc):
            QUOTA_EXHAUSTED = True
            if entry and age <= STALE_FALLBACK_HOURS:
                hydrate(candidate, entry)
                print(
                    f"[youtube-cache] stale fallback {candidate.keyword!r} "
                    f"({age:.1f}h old after quota error)"
                )
                return
        raise

    # Only cache a completed search result. Empty result sets are still valid
    # because recent_video_estimate is then 0 rather than None.
    if candidate.recent_video_estimate is not None:
        save_candidate(candidate)


# hybrid_scan.main() calls scan.youtube_competition dynamically, so replacing it
# here adds caching without duplicating any discovery/ranking code.
scan.youtube_competition = cached_youtube_competition


if __name__ == "__main__":
    hybrid_scan.main()
