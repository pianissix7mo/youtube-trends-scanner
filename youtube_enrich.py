#!/usr/bin/env python3
"""Enrich ChatGPT-selected entities with YouTube Data API metrics.

Input:  data/selected_entities.json
Output: output/latest.json and output/latest.md

This stage does not decide what is interesting and does not compute a final
opportunity score. It only measures recent YouTube supply/performance so the
final ChatGPT review can combine judgement + data.
"""

from __future__ import annotations

import json
import os
import statistics
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


def cache_key(query: str) -> str:
    normalized = " ".join((query or "").lower().split())
    return f"{LOOKBACK_DAYS}d|{normalized}"


def cached_metrics(cache: dict[str, Any], query: str, max_age_hours: float) -> dict[str, Any] | None:
    row = cache.get(cache_key(query))
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


def fetch_metrics(query: str, api_key: str) -> dict[str, Any]:
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
        return {
            "recent_video_estimate": estimated_supply,
            "sample_size": 0,
            "median_views": 0,
            "median_views_per_day": 0,
            "small_channel_hit_rate": 0.0,
            "median_channel_subscribers": None,
            "status": "ok_no_videos",
        }

    videos = api_get("videos", {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "maxResults": SAMPLE_SIZE,
        "key": api_key,
    })

    parsed: list[dict[str, Any]] = []
    channel_ids: list[str] = []
    for item in videos.get("items") or []:
        snippet = item.get("snippet") or {}
        stats = item.get("statistics") or {}
        try:
            views = int(stats.get("viewCount") or 0)
            published = parse_dt(str(snippet.get("publishedAt") or ""))
        except Exception:
            continue
        age_days = max(0.25, (now - published).total_seconds() / 86400.0)
        channel_id = str(snippet.get("channelId") or "")
        if channel_id:
            channel_ids.append(channel_id)
        parsed.append({
            "video_id": item.get("id"),
            "title": snippet.get("title"),
            "channel_id": channel_id,
            "published_at": published.isoformat(),
            "views": views,
            "views_per_day": int(round(views / age_days)),
        })

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

    views = [int(v["views"]) for v in parsed]
    vpds = [int(v["views_per_day"]) for v in parsed]
    channel_sub_values: list[int] = []
    small_known = 0
    small_hits = 0
    for v in parsed:
        sub = subscribers.get(str(v.get("channel_id") or ""))
        v["channel_subscribers"] = sub
        if sub is not None:
            channel_sub_values.append(sub)
            if sub < 50_000:
                small_known += 1
                if int(v["views"]) >= 1_000:
                    small_hits += 1

    return {
        "recent_video_estimate": estimated_supply,
        "sample_size": len(parsed),
        "median_views": int(statistics.median(views)) if views else 0,
        "median_views_per_day": int(statistics.median(vpds)) if vpds else 0,
        "small_channel_hit_rate": round(100.0 * small_hits / small_known, 1) if small_known else 0.0,
        "median_channel_subscribers": int(statistics.median(channel_sub_values)) if channel_sub_values else None,
        "status": "ok",
        "sample_videos": sorted(parsed, key=lambda x: int(x["views_per_day"]), reverse=True)[:10],
    }


def fmt(value: Any) -> str:
    return "—" if value is None else str(value)


def write_outputs(payload: dict[str, Any]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "latest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    window_label = f"{LOOKBACK_DAYS}d"
    lines = [
        "# YouTube Entity Enrichment",
        "",
        f"Generated: **{payload['generated_at_utc']}**",
        "",
        "This is a measurement table, not the final editorial ranking. ChatGPT reviews it at 06:00 Toronto time.",
        "",
        f"| # | Entity | YouTube query | Regions | {window_label} videos* | Median views/day | Small-channel hit | Status |",
        "|---:|---|---|---|---:|---:|---:|---|",
    ]
    for i, row in enumerate(payload["entities"], 1):
        m = row.get("youtube_metrics") or {}
        lines.append(
            f"| {i} | {row.get('entity','')} | {row.get('youtube_query','')} | "
            f"{','.join(row.get('regions') or []) or '—'} | {fmt(m.get('recent_video_estimate'))} | "
            f"{fmt(m.get('median_views_per_day'))} | "
            f"{fmt(m.get('small_channel_hit_rate'))}% | {m.get('status','—')} |"
        )
    lines.extend([
        "",
        f"\\* `{window_label} videos` is YouTube API's approximate total result count for videos published in the last {LOOKBACK_DAYS} days.",
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
        if not entity or not query:
            print(f"[skip] malformed selection row {i}: {item}")
            continue
        row["entity"] = entity
        row["youtube_query"] = query
        print(f"[youtube] {i}/{len(entities)} {entity!r} via {query!r}")

        metrics = cached_metrics(cache, query, CACHE_TTL_HOURS)
        if metrics is not None:
            metrics = dict(metrics)
            metrics["status"] = "cache_fresh"
            print("[cache] fresh")
        else:
            try:
                metrics = fetch_metrics(query, api_key)
                cache[cache_key(query)] = {
                    "cached_at_utc": datetime.now(timezone.utc).isoformat(),
                    "metrics": metrics,
                }
            except Exception as exc:
                print(f"[warn] API failed: {exc}")
                metrics = cached_metrics(cache, query, STALE_FALLBACK_HOURS)
                if metrics is not None:
                    metrics = dict(metrics)
                    metrics["status"] = "cache_stale_fallback"
                    metrics["api_error"] = str(exc)
                else:
                    metrics = {
                        "recent_video_estimate": None,
                        "sample_size": 0,
                        "median_views": None,
                        "median_views_per_day": None,
                        "small_channel_hit_rate": None,
                        "median_channel_subscribers": None,
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
        "entities": enriched,
    }
    write_outputs(payload)
    print(f"[done] enriched {len(enriched)} entities over {LOOKBACK_DAYS} days")


if __name__ == "__main__":
    main()
