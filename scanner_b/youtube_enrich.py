#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import statistics
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

from scanner_common import DATA, OUT, clamp, ensure_dirs, load_config, normalize_text, parse_timestamp, write_json

YT_API = "https://www.googleapis.com/youtube/v3"
CACHE_DIR = DATA.parent / ".cache"
CACHE_FILE = CACHE_DIR / "youtube_metrics_b.json"
CACHE_TTL_HOURS = float(os.getenv("YOUTUBE_CACHE_TTL_HOURS", "12"))
STALE_FALLBACK_HOURS = float(os.getenv("YOUTUBE_STALE_FALLBACK_HOURS", "48"))


def api_get(session: requests.Session, path: str, params: dict[str, Any]) -> dict[str, Any]:
    r = session.get(f"{YT_API}/{path}", params=params, timeout=30)
    if not r.ok:
        try:
            detail = r.json()
        except Exception:
            detail = r.text[:500]
        raise RuntimeError(f"YouTube API {r.status_code}: {detail}")
    return r.json()


def clean_terms(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    seen: set[str] = set()
    for value in raw:
        term = str(value or "").strip()
        key = normalize_text(term)
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(term)
    return out


def cache_key(query: str, terms: list[str], lookback_days: int) -> str:
    payload = json.dumps(
        {
            "lookback_days": int(lookback_days),
            "query": normalize_text(query),
            "terms": [normalize_text(x) for x in terms],
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()


def load_cache() -> dict[str, Any]:
    if not CACHE_FILE.exists():
        return {}
    try:
        value = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def save_cache(cache: dict[str, Any]) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def parse_cache_time(value: Any) -> datetime | None:
    try:
        dt = datetime.fromisoformat(str(value or "").replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def cached_metrics(
    cache: dict[str, Any],
    query: str,
    terms: list[str],
    lookback_days: int,
    max_age_hours: float,
) -> dict[str, Any] | None:
    row = cache.get(cache_key(query, terms, lookback_days))
    if not isinstance(row, dict):
        return None
    dt = parse_cache_time(row.get("cached_at_utc"))
    metrics = row.get("metrics")
    if dt is None or not isinstance(metrics, dict):
        return None
    age = datetime.now(timezone.utc) - dt.astimezone(timezone.utc)
    if age <= timedelta(hours=max_age_hours):
        return dict(metrics)
    return None


def seed_cache_from_latest(
    cache: dict[str, Any],
    lookback_days: int,
    max_age_hours: float,
) -> int:
    """Bootstrap Actions cache from the last committed B output.

    This is important when cache support is first deployed or when an Actions
    cache entry is unavailable. Matching is based on query + event terms rather
    than event_id, so metadata-only fixes do not burn new search.list quota.
    """
    latest = OUT / "latest.json"
    if not latest.exists():
        return 0
    try:
        payload = json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        return 0

    dt = parse_cache_time(payload.get("generated_at_utc"))
    if dt is None:
        return 0
    age = datetime.now(timezone.utc) - dt.astimezone(timezone.utc)
    if age > timedelta(hours=max_age_hours):
        return 0

    seeded = 0
    stamp = dt.astimezone(timezone.utc).isoformat()
    for event in payload.get("events") or []:
        if not isinstance(event, dict):
            continue
        query = str(event.get("youtube_query") or event.get("entity") or "").strip()
        terms = clean_terms(event.get("youtube_event_terms"))
        metrics = event.get("youtube_metrics")
        if not query or not isinstance(metrics, dict):
            continue
        status = str(metrics.get("status") or "")
        if status in {"api_failed_no_cache", "skipped_no_api_key", "skipped_budget_exhausted"}:
            continue
        key = cache_key(query, terms, lookback_days)
        if key not in cache:
            cache[key] = {"cached_at_utc": stamp, "metrics": metrics}
            seeded += 1
    return seeded


def quota_exhausted_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return (
        "youtube api 429" in msg
        or "resource_exhausted" in msg
        or "quota exceeded" in msg
        or "ratelimitexceeded" in msg
        or "rate_limit_exceeded" in msg
    )


def event_title_relevant(title: str, terms: list[str]) -> bool:
    if not terms:
        return True
    hay = normalize_text(title)
    return any(normalize_text(term) in hay for term in terms if normalize_text(term))


def supply_gap_score(relevant_sample_size: int) -> float:
    if relevant_sample_size <= 2:
        return 100.0
    if relevant_sample_size <= 5:
        return 95.0
    if relevant_sample_size <= 10:
        return 85.0
    if relevant_sample_size <= 20:
        return 70.0
    if relevant_sample_size <= 35:
        return 50.0
    return 30.0


def enrich_event(
    session: requests.Session,
    event: dict[str, Any],
    api_key: str,
    config: dict[str, Any],
) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    lookback_days = max(1, int(config.get("youtube_lookback_days", 3)))
    sample_size = min(50, max(1, int(config.get("youtube_sample_size", 50))))
    published_after = (now - timedelta(days=lookback_days)).isoformat().replace("+00:00", "Z")
    query = str(event.get("youtube_query") or event.get("entity") or "").strip()

    search = api_get(session, "search", {
        "part": "id",
        "q": query,
        "type": "video",
        "order": "date",
        "maxResults": sample_size,
        "publishedAfter": published_after,
        "relevanceLanguage": "zh",
        "key": api_key,
    })
    video_ids = [
        str(item.get("id", {}).get("videoId") or "")
        for item in (search.get("items") or [])
    ]
    video_ids = [x for x in video_ids if x]
    estimated_total = int((search.get("pageInfo") or {}).get("totalResults") or 0)

    if not video_ids:
        return {
            "status": "ok_no_videos",
            "query": query,
            "raw_sample_size": 0,
            "relevant_sample_size": 0,
            "estimated_total_results": estimated_total,
            "youtube_supply_gap_score": 100.0,
            "median_views_per_day": 0,
            "small_channel_hit_rate": 0.0,
            "sample_videos": [],
        }

    videos = api_get(session, "videos", {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "maxResults": 50,
        "key": api_key,
    })

    terms = clean_terms(event.get("youtube_event_terms"))
    parsed: list[dict[str, Any]] = []
    for item in videos.get("items") or []:
        snippet = item.get("snippet") or {}
        stats = item.get("statistics") or {}
        title = str(snippet.get("title") or "")
        if not event_title_relevant(title, terms):
            continue
        try:
            published = parse_timestamp(str(snippet.get("publishedAt") or ""))
            views = int(stats.get("viewCount") or 0)
        except Exception:
            continue
        age_days = max(0.125, (now - published).total_seconds() / 86400.0)
        parsed.append({
            "video_id": item.get("id"),
            "title": title,
            "channel_id": str(snippet.get("channelId") or ""),
            "published_at": published.isoformat(),
            "views": views,
            "views_per_day": int(round(views / age_days)),
        })

    channel_ids = list(dict.fromkeys([x["channel_id"] for x in parsed if x.get("channel_id")]))[:50]
    subscribers: dict[str, int | None] = {}
    if channel_ids:
        channels = api_get(session, "channels", {
            "part": "statistics",
            "id": ",".join(channel_ids),
            "maxResults": 50,
            "key": api_key,
        })
        for item in channels.get("items") or []:
            stats = item.get("statistics") or {}
            if stats.get("hiddenSubscriberCount"):
                subscribers[str(item.get("id"))] = None
            else:
                try:
                    subscribers[str(item.get("id"))] = int(stats.get("subscriberCount") or 0)
                except Exception:
                    subscribers[str(item.get("id"))] = None

    small_max = int(config.get("small_channel_max_subscribers", 50000))
    hit_vpd = int(config.get("small_channel_hit_views_per_day", 1000))
    small_count = 0
    small_hits = 0
    for row in parsed:
        subs = subscribers.get(row["channel_id"])
        row["channel_subscribers"] = subs
        if subs is not None and subs < small_max:
            small_count += 1
            if int(row["views_per_day"]) >= hit_vpd:
                small_hits += 1

    vpds = [int(x["views_per_day"]) for x in parsed]
    parsed.sort(key=lambda x: int(x["views_per_day"]), reverse=True)
    relevant_count = len(parsed)
    return {
        "status": "ok",
        "query": query,
        "raw_sample_size": len(video_ids),
        "relevant_sample_size": relevant_count,
        "estimated_total_results": estimated_total,
        "youtube_supply_gap_score": supply_gap_score(relevant_count),
        "median_views_per_day": int(statistics.median(vpds)) if vpds else 0,
        "small_channel_sample_size": small_count,
        "small_channel_hit_rate": round(100.0 * small_hits / small_count, 1) if small_count else 0.0,
        "sample_videos": parsed[:10],
    }


def failure_metrics(query: str, error: str) -> dict[str, Any]:
    return {
        "status": "api_failed_no_cache",
        "query": query,
        "raw_sample_size": 0,
        "relevant_sample_size": None,
        "estimated_total_results": None,
        "youtube_supply_gap_score": None,
        "median_views_per_day": None,
        "small_channel_sample_size": None,
        "small_channel_hit_rate": None,
        "sample_videos": [],
        "api_error": error,
    }


def write_markdown(payload: dict[str, Any]) -> None:
    lines = [
        "# Scanner B — Catalyst Opportunities",
        "",
        f"Generated: **{payload['generated_at_utc']}**",
        "",
        f"YouTube fresh search calls used: **{payload['youtube_search_calls_used']} / {payload['youtube_search_budget_per_run']}**",
        f"Cache hits: **{payload.get('youtube_cache_hits', 0)}**; stale fallbacks: **{payload.get('youtube_stale_fallback_hits', 0)}**; API failures: **{payload.get('youtube_api_failures', 0)}**",
        "",
        "| # | Event | Ticker | Judge | Discovery | Burst | Sources | YT gap | B final |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for i, row in enumerate(payload.get("events") or [], 1):
        yt = row.get("youtube_metrics") or {}
        lines.append(
            f"| {i} | {row.get('event_title','')} | {row.get('ticker') or '—'} | "
            f"{row.get('judge_score','—')} | {row.get('discovery_score','—')} | {row.get('news_burst_score','—')} | "
            f"{row.get('source_diversity_score','—')} | {yt.get('youtube_supply_gap_score','—')} | "
            f"{row.get('scanner_b_score','—')} |"
        )
    (OUT / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()
    config = load_config()
    selected = json.loads((DATA / "selected_events.json").read_text(encoding="utf-8"))
    events = list(selected.get("events") or [])
    budget = int(config.get("youtube_search_budget_per_run", 20))
    hard_limit = min(budget, int(config.get("candidate_limit_before_youtube", 20)), len(events))
    events = events[:hard_limit]
    lookback_days = max(1, int(config.get("youtube_lookback_days", 3)))

    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()
    session = requests.Session()
    enriched: list[dict[str, Any]] = []
    search_calls = 0
    cache_hits = 0
    stale_hits = 0
    api_failures = 0
    api_blocked_error: str | None = None

    cache = load_cache()
    seeded = seed_cache_from_latest(cache, lookback_days, STALE_FALLBACK_HOURS)
    if seeded:
        print(f"[cache] bootstrapped {seeded} entries from scanner_b/output/latest.json")

    for index, event in enumerate(events, 1):
        row = dict(event)
        query = str(row.get("youtube_query") or row.get("entity") or "").strip()
        terms = clean_terms(row.get("youtube_event_terms"))
        row["youtube_query"] = query
        row["youtube_event_terms"] = terms

        yt = cached_metrics(cache, query, terms, lookback_days, CACHE_TTL_HOURS)
        if yt is not None:
            yt["cache_status"] = "fresh"
            cache_hits += 1
            print(f"[cache] {index}/{len(events)} fresh: {query}")
        elif not api_key:
            yt = cached_metrics(cache, query, terms, lookback_days, STALE_FALLBACK_HOURS)
            if yt is not None:
                yt["cache_status"] = "stale_fallback"
                yt["api_error"] = "YOUTUBE_API_KEY missing"
                stale_hits += 1
            else:
                yt = failure_metrics(query, "YOUTUBE_API_KEY missing")
        elif api_blocked_error:
            yt = cached_metrics(cache, query, terms, lookback_days, STALE_FALLBACK_HOURS)
            if yt is not None:
                yt["cache_status"] = "stale_fallback"
                yt["api_error"] = api_blocked_error
                stale_hits += 1
            else:
                yt = failure_metrics(query, api_blocked_error)
        elif search_calls >= budget:
            yt = cached_metrics(cache, query, terms, lookback_days, STALE_FALLBACK_HOURS)
            if yt is not None:
                yt["cache_status"] = "stale_fallback"
                yt["api_error"] = "fresh search budget exhausted"
                stale_hits += 1
            else:
                yt = {
                    "status": "skipped_budget_exhausted",
                    "youtube_supply_gap_score": None,
                    "query": query,
                }
        else:
            try:
                yt = enrich_event(session, row, api_key, config)
                search_calls += 1
                cache[cache_key(query, terms, lookback_days)] = {
                    "cached_at_utc": datetime.now(timezone.utc).isoformat(),
                    "metrics": yt,
                }
                print(f"[youtube] {index}/{len(events)} fresh search: {query}")
            except Exception as exc:
                api_failures += 1
                error = str(exc)
                print(f"[warn] YouTube enrichment failed for {query}: {error}")
                if quota_exhausted_error(exc):
                    api_blocked_error = error
                    print("[warn] YouTube search quota exhausted; remaining events will use cache/fallback only.")
                yt = cached_metrics(cache, query, terms, lookback_days, STALE_FALLBACK_HOURS)
                if yt is not None:
                    yt["cache_status"] = "stale_fallback"
                    yt["api_error"] = error
                    stale_hits += 1
                else:
                    yt = failure_metrics(query, error)

        row["youtube_metrics"] = yt
        gap = yt.get("youtube_supply_gap_score")
        discovery = float(row.get("discovery_score") or 0.0)
        judge = row.get("judge_score")
        judge_value = float(judge) if judge is not None else None
        if judge_value is not None:
            row["scanner_b_score"] = round(
                clamp(0.65 * judge_value + 0.35 * discovery)
                if gap is None
                else clamp(0.50 * judge_value + 0.30 * discovery + 0.20 * float(gap)),
                1,
            )
        else:
            row["scanner_b_score"] = round(
                discovery if gap is None else clamp(0.80 * discovery + 0.20 * float(gap)),
                1,
            )
        enriched.append(row)

    save_cache(cache)
    enriched.sort(key=lambda x: float(x.get("scanner_b_score") or 0), reverse=True)
    payload = {
        "scanner": "B",
        "judge_version": selected.get("judge_version"),
        "source_candidates_generated_at_utc": selected.get("source_candidates_generated_at_utc"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "youtube_search_budget_per_run": budget,
        "youtube_search_calls_used": search_calls,
        "youtube_cache_hits": cache_hits,
        "youtube_stale_fallback_hits": stale_hits,
        "youtube_api_failures": api_failures,
        "cache_ttl_hours": CACHE_TTL_HOURS,
        "stale_fallback_hours": STALE_FALLBACK_HOURS,
        "events": enriched,
    }
    write_json(OUT / "latest.json", payload)
    write_markdown(payload)
    print(
        f"Wrote output/latest.json; fresh YouTube search calls used: {search_calls}/{budget}; "
        f"cache hits={cache_hits}; stale fallbacks={stale_hits}; api failures={api_failures}"
    )


if __name__ == "__main__":
    main()
