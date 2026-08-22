#!/usr/bin/env python3
"""Enrich ChatGPT-selected entities with YouTube Data API metrics.

Input:  data/selected_entities.json
Output: output/latest.json and output/latest.md

ChatGPT decides what each entity means and supplies dynamic relevance_groups.
Python applies those rules to the YouTube sample before calculating metrics.
This stage measures recent supply/performance; it does not compute the final
editorial opportunity score.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import statistics
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "output"
CACHE_DIR = ROOT / ".cache"
CACHE_FILE = CACHE_DIR / "youtube_metrics.json"
YT_API = "https://www.googleapis.com/youtube/v3"
LOOKBACK_DAYS = max(1, int(os.getenv("YOUTUBE_LOOKBACK_DAYS", "3")))
SAMPLE_SIZE = 50
CACHE_TTL_HOURS = float(os.getenv("YOUTUBE_CACHE_TTL_HOURS", "12"))
STALE_FALLBACK_HOURS = float(os.getenv("YOUTUBE_STALE_FALLBACK_HOURS", "48"))
SMALL_CHANNEL_MAX_SUBS = max(1, int(os.getenv("SMALL_CHANNEL_MAX_SUBS", "50000")))
SMALL_CHANNEL_HIT_VPD = max(1, int(os.getenv("SMALL_CHANNEL_HIT_VPD", "1000")))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_cache() -> dict[str, Any]:
    if not CACHE_FILE.exists():
        return {}
    try:
        value = load_json(CACHE_FILE)
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def save_cache(cache: dict[str, Any]) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_text(text: str) -> str:
    value = unicodedata.normalize("NFKC", str(text or "")).lower()
    return " ".join(value.split())


def normalize_relevance_groups(raw: Any) -> list[list[str]]:
    """Return clean OR-within / AND-across relevance groups."""
    if not isinstance(raw, list):
        return []
    groups: list[list[str]] = []
    for group in raw:
        if not isinstance(group, list):
            continue
        cleaned: list[str] = []
        seen: set[str] = set()
        for term in group:
            value = str(term or "").strip()
            key = normalize_text(value)
            if not key or key in seen:
                continue
            seen.add(key)
            cleaned.append(value)
        if cleaned:
            groups.append(cleaned)
    return groups


def term_matches(normalized_title: str, term: str) -> bool:
    needle = normalize_text(term)
    if not needle:
        return False
    if re.fullmatch(r"[a-z0-9.+&/-]+", needle):
        pattern = rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])"
        return re.search(pattern, normalized_title) is not None
    return needle in normalized_title


def is_relevant_title(title: str, groups: list[list[str]]) -> bool:
    """All groups must match; any term inside a group may satisfy that group."""
    if not groups:
        return True
    normalized_title = normalize_text(title)
    return all(any(term_matches(normalized_title, term) for term in group) for group in groups)


def relevance_signature(groups: list[list[str]]) -> str:
    normalized = [[normalize_text(term) for term in group] for group in groups]
    payload = json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:12]


def cache_key(query: str, relevance_groups: list[list[str]]) -> str:
    normalized_query = normalize_text(query)
    return f"{LOOKBACK_DAYS}d|{normalized_query}|rel:{relevance_signature(relevance_groups)}"


def cached_metrics(
    cache: dict[str, Any],
    query: str,
    relevance_groups: list[list[str]],
    max_age_hours: float,
) -> dict[str, Any] | None:
    row = cache.get(cache_key(query, relevance_groups))
    if not isinstance(row, dict):
        return None
    stamp = row.get("cached_at_utc")
    if not stamp:
        return None
    try:
        dt = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
        age = datetime.now(timezone.utc) - dt.astimezone(timezone.utc)
    except Exception:
        return None
    if age <= timedelta(hours=max_age_hours):
        return row.get("metrics") if isinstance(row.get("metrics"), dict) else None
    return None


def api_get(path: str, params: dict[str, Any]) -> dict[str, Any]:
    r = requests.get(f"{YT_API}/{path}", params=params, timeout=25)
    if not r.ok:
        try:
            detail = r.json()
        except Exception:
            detail = r.text[:500]
        raise RuntimeError(f"YouTube API {r.status_code}: {detail}")
    return r.json()


def parse_dt(text: str) -> datetime:
    return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(timezone.utc)


def empty_metrics(
    estimated_supply: int | None,
    raw_sample_size: int,
    relevant_sample_size: int | None,
    relevance_ratio: float | None,
    relevance_groups: list[list[str]],
    status: str,
) -> dict[str, Any]:
    return {
        "recent_video_estimate": estimated_supply,
        "raw_recent_video_estimate": estimated_supply,
        "raw_sample_size": raw_sample_size,
        "relevant_sample_size": relevant_sample_size,
        "relevance_ratio": relevance_ratio,
        "median_views": 0 if relevant_sample_size == 0 else None,
        "median_views_per_day": 0 if relevant_sample_size == 0 else None,
        "small_channel_sample_size": 0 if relevant_sample_size == 0 else None,
        "small_channel_median_views_per_day": 0 if relevant_sample_size == 0 else None,
        "small_channel_hit_rate": 0.0 if relevant_sample_size == 0 else None,
        "top10_small_channel_share": 0.0 if relevant_sample_size == 0 else None,
        "top10_small_channel_count": 0 if relevant_sample_size == 0 else None,
        "top10_known_channels": 0 if relevant_sample_size == 0 else None,
        "median_channel_subscribers": None,
        "small_channel_max_subscribers": SMALL_CHANNEL_MAX_SUBS,
        "small_channel_hit_vpd_threshold": SMALL_CHANNEL_HIT_VPD,
        "relevance_filter_applied": bool(relevance_groups),
        "status": status,
    }


def fetch_metrics(
    query: str,
    relevance_groups: list[list[str]],
    api_key: str,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    published_after = (now - timedelta(days=LOOKBACK_DAYS)).isoformat().replace("+00:00", "Z")

    search = api_get("search", {
        "part": "id",
        "q": query,
        "type": "video",
        "order": "relevance",
        "maxResults": SAMPLE_SIZE,
        "publishedAfter": published_after,
        "relevanceLanguage": "zh",
        "key": api_key,
    })

    video_ids = [
        str(item.get("id", {}).get("videoId") or "")
        for item in search.get("items") or []
    ]
    video_ids = [x for x in video_ids if x]
    estimated_supply = int((search.get("pageInfo") or {}).get("totalResults") or 0)

    if not video_ids:
        return empty_metrics(
            estimated_supply,
            raw_sample_size=0,
            relevant_sample_size=0,
            relevance_ratio=0.0,
            relevance_groups=relevance_groups,
            status="ok_no_videos",
        )

    videos = api_get("videos", {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "maxResults": SAMPLE_SIZE,
        "key": api_key,
    })

    raw_parsed: list[dict[str, Any]] = []
    for item in videos.get("items") or []:
        snippet = item.get("snippet") or {}
        stats = item.get("statistics") or {}
        try:
            views = int(stats.get("viewCount") or 0)
            published = parse_dt(str(snippet.get("publishedAt") or ""))
        except Exception:
            continue
        age_days = max(0.25, (now - published).total_seconds() / 86400.0)
        raw_parsed.append({
            "video_id": item.get("id"),
            "title": snippet.get("title"),
            "channel_id": str(snippet.get("channelId") or ""),
            "published_at": published.isoformat(),
            "views": views,
            "views_per_day": int(round(views / age_days)),
        })

    relevant = [
        row for row in raw_parsed
        if is_relevant_title(str(row.get("title") or ""), relevance_groups)
    ]
    raw_sample_size = len(raw_parsed)
    relevant_sample_size = len(relevant)
    relevance_ratio = (
        round(100.0 * relevant_sample_size / raw_sample_size, 1)
        if raw_sample_size
        else 0.0
    )

    if not relevant:
        return empty_metrics(
            estimated_supply,
            raw_sample_size=raw_sample_size,
            relevant_sample_size=0,
            relevance_ratio=relevance_ratio,
            relevance_groups=relevance_groups,
            status="ok_no_relevant_videos",
        )

    channel_ids = [
        str(v.get("channel_id") or "")
        for v in relevant
        if str(v.get("channel_id") or "")
    ]
    subscribers: dict[str, int | None] = {}
    unique_channels = list(dict.fromkeys(channel_ids))[:50]
    if unique_channels:
        channels = api_get("channels", {
            "part": "statistics",
            "id": ",".join(unique_channels),
            "maxResults": 50,
            "key": api_key,
        })
        for item in channels.get("items") or []:
            stats = item.get("statistics") or {}
            hidden = bool(stats.get("hiddenSubscriberCount"))
            if hidden:
                subscribers[str(item.get("id"))] = None
            else:
                try:
                    subscribers[str(item.get("id"))] = int(stats.get("subscriberCount") or 0)
                except Exception:
                    subscribers[str(item.get("id"))] = None

    views = [int(v["views"]) for v in relevant]
    vpds = [int(v["views_per_day"]) for v in relevant]
    channel_sub_values: list[int] = []
    small_vpds: list[int] = []
    small_hits = 0

    for v in relevant:
        sub = subscribers.get(str(v.get("channel_id") or ""))
        v["channel_subscribers"] = sub
        if sub is not None:
            channel_sub_values.append(sub)
            if sub < SMALL_CHANNEL_MAX_SUBS:
                vpd = int(v["views_per_day"])
                small_vpds.append(vpd)
                if vpd >= SMALL_CHANNEL_HIT_VPD:
                    small_hits += 1

    sorted_relevant = sorted(relevant, key=lambda x: int(x["views_per_day"]), reverse=True)
    top10 = sorted_relevant[:10]
    top10_known = [v for v in top10 if v.get("channel_subscribers") is not None]
    top10_small = [
        v for v in top10_known
        if int(v.get("channel_subscribers") or 0) < SMALL_CHANNEL_MAX_SUBS
    ]

    status = "ok_low_relevance" if relevance_groups and relevance_ratio < 30.0 else "ok"
    return {
        "recent_video_estimate": estimated_supply,
        "raw_recent_video_estimate": estimated_supply,
        "raw_sample_size": raw_sample_size,
        "relevant_sample_size": relevant_sample_size,
        "relevance_ratio": relevance_ratio,
        "median_views": int(statistics.median(views)) if views else 0,
        "median_views_per_day": int(statistics.median(vpds)) if vpds else 0,
        "small_channel_sample_size": len(small_vpds),
        "small_channel_median_views_per_day": (
            int(statistics.median(small_vpds)) if small_vpds else 0
        ),
        "small_channel_hit_rate": (
            round(100.0 * small_hits / len(small_vpds), 1) if small_vpds else 0.0
        ),
        "top10_small_channel_share": (
            round(100.0 * len(top10_small) / len(top10_known), 1)
            if top10_known
            else 0.0
        ),
        "top10_small_channel_count": len(top10_small),
        "top10_known_channels": len(top10_known),
        "median_channel_subscribers": (
            int(statistics.median(channel_sub_values)) if channel_sub_values else None
        ),
        "small_channel_max_subscribers": SMALL_CHANNEL_MAX_SUBS,
        "small_channel_hit_vpd_threshold": SMALL_CHANNEL_HIT_VPD,
        "relevance_filter_applied": bool(relevance_groups),
        "status": status,
        "sample_videos": sorted_relevant[:10],
    }


def fmt(value: Any) -> str:
    return "—" if value is None else str(value)


def write_outputs(payload: dict[str, Any]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "latest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# YouTube Entity Enrichment",
        "",
        f"Generated: **{payload['generated_at_utc']}**",
        "",
        "This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.",
        "",
        "| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for i, row in enumerate(payload["entities"], 1):
        m = row.get("youtube_metrics") or {}
        lines.append(
            f"| {i} | {row.get('entity','')} | {row.get('youtube_query','')} | "
            f"{fmt(m.get('relevant_sample_size'))}/{fmt(m.get('raw_sample_size'))} | "
            f"{fmt(m.get('relevance_ratio'))}% | "
            f"{fmt(m.get('median_views_per_day'))} | "
            f"{fmt(m.get('small_channel_median_views_per_day'))} | "
            f"{fmt(m.get('small_channel_hit_rate'))}% | "
            f"{fmt(m.get('top10_small_channel_share'))}% | {m.get('status','—')} |"
        )
    lines.extend([
        "",
        f"- Window: last {LOOKBACK_DAYS} days.",
        f"- Small channel: fewer than {SMALL_CHANNEL_MAX_SUBS:,} subscribers.",
        f"- Small-channel hit: at least {SMALL_CHANNEL_HIT_VPD:,} views/day.",
        "- Relevance rules are generated dynamically by the selection-stage ChatGPT.",
        "- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.",
    ])
    (OUT / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    selected_path = DATA / "selected_entities.json"
    if not selected_path.exists():
        raise RuntimeError("data/selected_entities.json does not exist")

    selected_payload = load_json(selected_path)
    entities = selected_payload.get("selected") or selected_payload.get("entities") or []
    if not isinstance(entities, list) or not entities:
        raise RuntimeError("selected_entities.json has no selected entities")
    entities = entities[:20]

    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("YOUTUBE_API_KEY secret is missing")

    cache = load_cache()
    enriched: list[dict[str, Any]] = []

    for i, item in enumerate(entities, 1):
        row = dict(item)
        entity = str(row.get("entity") or row.get("name") or "").strip()
        query = str(row.get("youtube_query") or row.get("query") or entity).strip()
        relevance_groups = normalize_relevance_groups(row.get("relevance_groups"))

        if not entity or not query:
            print(f"[skip] malformed selection row {i}: {item}")
            continue

        row["entity"] = entity
        row["youtube_query"] = query
        row["relevance_groups"] = relevance_groups
        print(
            f"[youtube] {i}/{len(entities)} {entity!r} via {query!r}; "
            f"relevance_groups={relevance_groups or 'LEGACY_UNFILTERED'}"
        )

        metrics = cached_metrics(cache, query, relevance_groups, CACHE_TTL_HOURS)
        if metrics is not None:
            metrics = dict(metrics)
            metrics["cache_status"] = "fresh"
            print("[cache] fresh")
        else:
            try:
                metrics = fetch_metrics(query, relevance_groups, api_key)
                cache[cache_key(query, relevance_groups)] = {
                    "cached_at_utc": datetime.now(timezone.utc).isoformat(),
                    "metrics": metrics,
                }
            except Exception as exc:
                print(f"[warn] API failed: {exc}")
                metrics = cached_metrics(cache, query, relevance_groups, STALE_FALLBACK_HOURS)
                if metrics is not None:
                    metrics = dict(metrics)
                    metrics["cache_status"] = "stale_fallback"
                    metrics["api_error"] = str(exc)
                else:
                    metrics = {
                        "recent_video_estimate": None,
                        "raw_recent_video_estimate": None,
                        "raw_sample_size": 0,
                        "relevant_sample_size": None,
                        "relevance_ratio": None,
                        "median_views": None,
                        "median_views_per_day": None,
                        "small_channel_sample_size": None,
                        "small_channel_median_views_per_day": None,
                        "small_channel_hit_rate": None,
                        "top10_small_channel_share": None,
                        "top10_small_channel_count": None,
                        "top10_known_channels": None,
                        "median_channel_subscribers": None,
                        "small_channel_max_subscribers": SMALL_CHANNEL_MAX_SUBS,
                        "small_channel_hit_vpd_threshold": SMALL_CHANNEL_HIT_VPD,
                        "relevance_filter_applied": bool(relevance_groups),
                        "status": "api_failed_no_cache",
                        "api_error": str(exc),
                    }

        row["youtube_metrics"] = metrics
        enriched.append(row)

    save_cache(cache)
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "lookback_days": LOOKBACK_DAYS,
        "selection_generated_at_utc": selected_payload.get("generated_at_utc"),
        "selection_notes": selected_payload.get("notes"),
        "small_channel_max_subscribers": SMALL_CHANNEL_MAX_SUBS,
        "small_channel_hit_vpd_threshold": SMALL_CHANNEL_HIT_VPD,
        "entities": enriched,
    }
    write_outputs(payload)
    print(
        f"[done] enriched {len(enriched)} entities over {LOOKBACK_DAYS} days; "
        f"small channel < {SMALL_CHANNEL_MAX_SUBS:,} subs; "
        f"hit >= {SMALL_CHANNEL_HIT_VPD:,} views/day"
    )


if __name__ == "__main__":
    main()
