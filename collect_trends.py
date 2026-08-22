#!/usr/bin/env python3
"""Collect a broad, mostly-unfiltered Google Trends candidate pool.

Python gathers raw discovery signals only. RSS is the reliable broad layer.
Google Trends Explore (YouTube Search) is deliberately light-touch so the
collector does not hammer Google's unofficial endpoint and trigger 429s.
ChatGPT later reviews the resulting pool and selects the investable entities.
"""

from __future__ import annotations

import json
import math
import os
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests
from trendspyg import download_google_trends_explore

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RSS_URL = "https://trends.google.com/trending/rss"
RAW_LIMIT = max(100, int(os.getenv("RAW_LIMIT", "1000")))
RSS_HOURS = max(4, int(os.getenv("TRENDING_RSS_HOURS", "48")))
TIMEFRAME = os.getenv("TRENDS_TIMEFRAME", "now 3-d")
YT_ANCHORS_PER_REGION = max(0, int(os.getenv("YT_TRENDS_ANCHORS_PER_REGION", "2")))
YT_DELAY_SECONDS = max(0.0, float(os.getenv("YT_TRENDS_DELAY_SECONDS", "12")))
YT_CACHE_TTL_SECONDS = max(3600.0, float(os.getenv("YT_TRENDS_CACHE_TTL_SECONDS", "86400")))
ROTATION_TZ = ZoneInfo("America/Toronto")

REGIONS = {
    "US": {
        "name": "United States",
        "anchors": ["stock market", "AI", "semiconductor", "earnings", "bitcoin", "stocks"],
    },
    "CA": {
        "name": "Canada",
        "anchors": ["stock market", "AI", "semiconductor", "earnings", "bitcoin", "stocks"],
    },
    "TW": {
        "name": "Taiwan",
        "anchors": ["美股", "AI", "半導體", "財報", "比特幣", "股票"],
    },
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


def key_for(text: str) -> str:
    return re.sub(r"[\s\-_·•|]+", "", clean(text).lower())


def parse_compact_number(text: str) -> int:
    s = clean(text).upper().replace(",", "").replace("+", "")
    m = re.search(r"([\d.]+)\s*([KMB]?)", s)
    if not m:
        return 0
    n = float(m.group(1))
    mult = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}[m.group(2)]
    return int(n * mult)


def rising_strength(item: dict[str, Any]) -> tuple[str, float]:
    raw = str(item.get("formatted_value") or item.get("value") or "")
    if "breakout" in raw.lower():
        return "Breakout", 100.0
    m = re.search(r"([\d,.]+)%", raw)
    if m:
        pct = float(m.group(1).replace(",", ""))
        return raw, min(90.0, 18.0 + 18.0 * math.log10(max(1.0, pct)))
    value = item.get("value")
    if isinstance(value, (int, float)) and value > 0:
        return raw or str(value), min(80.0, 15.0 + 15.0 * math.log10(float(value)))
    return raw or "Rising", 20.0


def is_rate_limited(exc: Exception) -> bool:
    status = getattr(getattr(exc, "response", None), "status_code", None)
    text = str(exc).lower()
    return status == 429 or "429" in text or "too many requests" in text or "unusual traffic" in text


def resolve_explore_timeframe() -> str:
    """Translate the semantic 3-day setting into Google's exact hourly custom range.

    Google Explore's preset list has 1 day and 7 days but not a native 3-day
    preset. A custom hourly range is supported within the past week, so
    ``now 3-d`` is expressed as an exact rolling 72-hour window instead of
    relying on an unsupported preset string. Other caller-supplied timeframes
    pass through unchanged.
    """
    if TIMEFRAME.strip().lower() != "now 3-d":
        return TIMEFRAME
    end = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    start = end - timedelta(hours=72)
    return f"{start:%Y-%m-%dT%H} {end:%Y-%m-%dT%H}"


def anchor_rotation() -> tuple[int, int, dict[str, list[str]], str]:
    """Choose one rotating anchor group per Toronto calendar day.

    With six anchors and two anchors per region this creates three daily groups,
    covering the full anchor set once every three days while keeping each run to
    at most six logical Explore requests across US/CA/TW.
    """
    today = datetime.now(ROTATION_TZ).date()
    if YT_ANCHORS_PER_REGION <= 0:
        return 0, 1, {geo: [] for geo in REGIONS}, today.isoformat()

    max_anchor_count = max(len(cfg["anchors"]) for cfg in REGIONS.values())
    group_count = max(1, math.ceil(max_anchor_count / YT_ANCHORS_PER_REGION))
    group_index = today.toordinal() % group_count
    selected: dict[str, list[str]] = {}

    for geo, cfg in REGIONS.items():
        anchors = list(cfg["anchors"])
        if not anchors:
            selected[geo] = []
            continue
        start = group_index * YT_ANCHORS_PER_REGION
        count = min(YT_ANCHORS_PER_REGION, len(anchors))
        selected[geo] = [anchors[(start + i) % len(anchors)] for i in range(count)]

    return group_index, group_count, selected, today.isoformat()


def fetch_rss(geo: str) -> list[dict[str, Any]]:
    r = requests.get(
        RSS_URL,
        params={"geo": geo, "hours": RSS_HOURS},
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0 youtube-trends-scanner/3.0"},
    )
    r.raise_for_status()
    root = ET.fromstring(r.text)
    ns = {"ht": "https://trends.google.com/trending/rss"}
    rows: list[dict[str, Any]] = []

    for rank, item in enumerate(root.findall(".//item"), 1):
        title = clean(item.findtext("title", default=""))
        if not title:
            continue
        traffic_text = item.findtext("ht:approx_traffic", default="", namespaces=ns)
        news_titles = [
            clean(node.text or "")
            for node in item.findall(".//ht:news_item_title", ns)
            if clean(node.text or "")
        ]
        pub = clean(item.findtext("pubDate", default=""))
        try:
            published_at = parsedate_to_datetime(pub).astimezone(timezone.utc).isoformat() if pub else None
        except Exception:
            published_at = pub or None
        traffic = parse_compact_number(traffic_text)
        strength = 25.0 + min(50.0, 10.0 * math.log10(max(1, traffic))) - min(rank, 50) * 0.15
        rows.append({
            "query": title,
            "region": geo,
            "source": "google_trending",
            "rank": rank,
            "signal": f"GTrend {traffic_text or 'unknown'}",
            "strength": round(max(0.0, strength), 2),
            "traffic": traffic,
            "published_at": published_at,
            "news_titles": news_titles[:8],
        })
    return rows


def fetch_youtube_related(geo: str, anchor: str, explore_timeframe: str) -> list[dict[str, Any]]:
    env = download_google_trends_explore(
        anchor,
        geo=geo,
        timeframe=explore_timeframe,
        gprop="youtube",
        cache="disk",
        cache_ttl=YT_CACHE_TTL_SECONDS,
        cookies="disk",
        max_retries=1,
        retry_wait=4,
    )
    related = env.get("related_queries") or {}
    rows: list[dict[str, Any]] = []

    for rank, item in enumerate((related.get("rising") or [])[:25], 1):
        q = clean(str(item.get("query") or ""))
        if not q:
            continue
        signal, strength = rising_strength(item)
        rows.append({
            "query": q,
            "region": geo,
            "source": "youtube_rising",
            "anchor": anchor,
            "rank": rank,
            "signal": signal,
            "strength": round(strength + max(0, 12 - rank * 0.4), 2),
        })

    for rank, item in enumerate((related.get("top") or [])[:25], 1):
        q = clean(str(item.get("query") or ""))
        if not q:
            continue
        rows.append({
            "query": q,
            "region": geo,
            "source": "youtube_top",
            "anchor": anchor,
            "rank": rank,
            "signal": "Top",
            "strength": round(max(8.0, 35.0 - rank * 0.8), 2),
        })
    return rows


def aggregate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = key_for(str(row["query"]))
        if not key:
            continue
        g = grouped.setdefault(key, {
            "query": row["query"],
            "regions": [],
            "signals": [],
            "news_titles": [],
            "max_strength": 0.0,
        })
        if row["region"] not in g["regions"]:
            g["regions"].append(row["region"])
        g["signals"].append({k: v for k, v in row.items() if k not in {"query", "news_titles"}})
        for title in row.get("news_titles") or []:
            if title not in g["news_titles"]:
                g["news_titles"].append(title)
        g["max_strength"] = max(float(g["max_strength"]), float(row.get("strength") or 0))

    out: list[dict[str, Any]] = []
    for g in grouped.values():
        g["raw_priority"] = round(float(g["max_strength"]) + 8.0 * max(0, len(g["regions"]) - 1), 2)
        g["news_titles"] = g["news_titles"][:12]
        out.append(g)

    out.sort(key=lambda x: (-x["raw_priority"], -len(x["regions"]), x["query"].lower()))
    return out[:RAW_LIMIT]


def main() -> None:
    all_rows: list[dict[str, Any]] = []
    errors: list[str] = []
    explore_attempted = 0
    explore_succeeded = 0
    explore_stopped_for_429 = False
    explore_timeframe = resolve_explore_timeframe()
    rotation_index, rotation_groups, selected_anchors, rotation_date = anchor_rotation()

    print(f"[youtube trends] configured timeframe: {TIMEFRAME}")
    print(f"[youtube trends] Explore timeframe: {explore_timeframe}")
    print(
        f"[youtube trends] rotation {rotation_index + 1}/{rotation_groups} "
        f"for Toronto date {rotation_date}: {selected_anchors}"
    )

    # Reliable broad layer first.
    for geo in REGIONS:
        print(f"[rss] {geo}")
        try:
            rows = fetch_rss(geo)
            print(f"[rss] {geo}: {len(rows)} rows")
            all_rows.extend(rows)
        except Exception as exc:
            msg = f"RSS {geo}: {exc}"
            print(f"[warn] {msg}")
            errors.append(msg)

    # Light-touch YouTube Search layer. At two anchors per region this is at most
    # six logical requests per run. The group rotates daily, so all six anchors
    # per region are covered across the same three-day window.
    max_rounds = max((len(v) for v in selected_anchors.values()), default=0)
    for anchor_index in range(max_rounds):
        for geo in REGIONS:
            anchors = selected_anchors.get(geo) or []
            if anchor_index >= len(anchors) or explore_stopped_for_429:
                continue

            anchor = anchors[anchor_index]
            explore_attempted += 1
            print(f"[youtube trends] {geo} / {anchor!r} (logical request {explore_attempted})")
            try:
                rows = fetch_youtube_related(geo, anchor, explore_timeframe)
                print(f"[youtube trends] {geo} / {anchor!r}: {len(rows)} rows")
                all_rows.extend(rows)
                explore_succeeded += 1
            except Exception as exc:
                msg = f"YouTube Trends {geo}/{anchor}: {exc}"
                print(f"[warn] {msg}")
                errors.append(msg)
                if is_rate_limited(exc):
                    explore_stopped_for_429 = True
                    print("[rate-limit] first 429/block detected; stopping Explore immediately and keeping RSS results")

            if not explore_stopped_for_429 and YT_DELAY_SECONDS > 0:
                time.sleep(YT_DELAY_SECONDS)

        if explore_stopped_for_429:
            break

    candidates = aggregate(all_rows)
    now = datetime.now(timezone.utc)
    region_counts = {
        geo: sum(1 for c in candidates if geo in c["regions"])
        for geo in REGIONS
    }
    payload = {
        "generated_at_utc": now.isoformat(),
        "timeframe": TIMEFRAME,
        "explore_timeframe": explore_timeframe,
        "rss_hours": RSS_HOURS,
        "raw_limit": RAW_LIMIT,
        "regions": REGIONS,
        "row_count_before_dedupe": len(all_rows),
        "candidate_count": len(candidates),
        "candidate_region_counts": region_counts,
        "youtube_trends": {
            "anchors_per_region": YT_ANCHORS_PER_REGION,
            "rotation_date_toronto": rotation_date,
            "rotation_group": rotation_index + 1,
            "rotation_group_count": rotation_groups,
            "anchors_used": selected_anchors,
            "delay_seconds": YT_DELAY_SECONDS,
            "cache_ttl_seconds": YT_CACHE_TTL_SECONDS,
            "logical_requests_attempted": explore_attempted,
            "calls_succeeded": explore_succeeded,
            "stopped_after_429": explore_stopped_for_429,
        },
        "errors": errors,
        "selection_guidance": {
            "geo": "Treat US, Canada, and Taiwan as near-equal discovery markets; Taiwan may be only slightly higher, not dominant.",
            "relevance": "Prefer entities/events that matter to US equities, technology supply chains, macro, rates, or major crypto assets. A non-US company is valid if it can materially affect US-listed stocks or investor attention.",
            "dedupe": "One final slot per company/asset/entity. Merge long-tail queries about the same entity.",
            "target": 20,
        },
        "candidates": candidates,
    }

    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / "raw_candidates.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] wrote {len(candidates)} candidates to {path}")


if __name__ == "__main__":
    main()
