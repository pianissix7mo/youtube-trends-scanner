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
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import requests
from trendspyg import download_google_trends_explore

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RSS_URL = "https://trends.google.com/trending/rss"
RAW_LIMIT = max(100, int(os.getenv("RAW_LIMIT", "1000")))
RSS_HOURS = max(4, int(os.getenv("TRENDING_RSS_HOURS", "48")))
TIMEFRAME = os.getenv("TRENDS_TIMEFRAME", "now 7-d")
YT_ANCHORS_PER_REGION = max(0, int(os.getenv("YT_TRENDS_ANCHORS_PER_REGION", "2")))
YT_DELAY_SECONDS = max(0.0, float(os.getenv("YT_TRENDS_DELAY_SECONDS", "12")))
YT_MAX_CONSECUTIVE_429 = max(1, int(os.getenv("YT_TRENDS_MAX_CONSECUTIVE_429", "2")))

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
    return status == 429 or "429" in str(exc)


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


def fetch_youtube_related(geo: str, anchor: str) -> list[dict[str, Any]]:
    env = download_google_trends_explore(
        anchor,
        geo=geo,
        timeframe=TIMEFRAME,
        gprop="youtube",
        cache=False,
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
    consecutive_429 = 0
    explore_stopped_for_429 = False

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

    # Light-touch YouTube Search layer. Round-robin regions so US/CA/TW get a
    # fair chance before any region receives a second Explore request.
    if YT_ANCHORS_PER_REGION > 0:
        for anchor_index in range(YT_ANCHORS_PER_REGION):
            for geo, cfg in REGIONS.items():
                anchors = cfg["anchors"]
                if anchor_index >= len(anchors):
                    continue
                if explore_stopped_for_429:
                    break

                anchor = anchors[anchor_index]
                explore_attempted += 1
                print(f"[youtube trends] {geo} / {anchor!r} (attempt {explore_attempted})")
                try:
                    rows = fetch_youtube_related(geo, anchor)
                    print(f"[youtube trends] {geo} / {anchor!r}: {len(rows)} rows")
                    all_rows.extend(rows)
                    explore_succeeded += 1
                    consecutive_429 = 0
                except Exception as exc:
                    msg = f"YouTube Trends {geo}/{anchor}: {exc}"
                    print(f"[warn] {msg}")
                    errors.append(msg)
                    if is_rate_limited(exc):
                        consecutive_429 += 1
                        print(f"[rate-limit] consecutive 429s: {consecutive_429}")
                        if consecutive_429 >= YT_MAX_CONSECUTIVE_429:
                            explore_stopped_for_429 = True
                            print("[rate-limit] stopping further Explore calls; RSS data will still be used")
                    else:
                        consecutive_429 = 0

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
        "rss_hours": RSS_HOURS,
        "raw_limit": RAW_LIMIT,
        "regions": REGIONS,
        "row_count_before_dedupe": len(all_rows),
        "candidate_count": len(candidates),
        "candidate_region_counts": region_counts,
        "youtube_trends": {
            "anchors_per_region": YT_ANCHORS_PER_REGION,
            "delay_seconds": YT_DELAY_SECONDS,
            "calls_attempted": explore_attempted,
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
