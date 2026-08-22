#!/usr/bin/env python3
"""Hybrid entry point: broad Google Trending discovery + existing YouTube scanner."""

from __future__ import annotations

import math
import os
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Any

import requests

import scan


TRENDING_RSS_URL = "https://trends.google.com/trending/rss"
TRENDING_RSS_GEOS = [
    x.strip().upper()
    for x in os.getenv("TRENDING_RSS_GEOS", "US,CA,TW,HK,SG").split(",")
    if x.strip()
]
TRENDING_RSS_HOURS = max(4, int(os.getenv("TRENDING_RSS_HOURS", "48")))
TRENDING_RSS_TIMEOUT = float(os.getenv("TRENDING_RSS_TIMEOUT", "10"))
TRENDING_RSS_PER_GEO = max(1, int(os.getenv("TRENDING_RSS_PER_GEO", "50")))
TRENDING_PRESELECT_LIMIT = max(0, int(os.getenv("TRENDING_PRESELECT_LIMIT", "16")))

# These terms are checked against both the trend title and the related news
# headlines embedded in Google's Trending RSS. That lets a trend such as an
# unfamiliar company name pass the filter when its news context says
# "stock jumps after earnings".
BROAD_FINANCE_HINTS = {
    "stock", "stocks", "share price", "shares", "earnings", "revenue", "profit",
    "guidance", "investor", "wall street", "nasdaq", "dow jones", "s&p 500",
    "market cap", "price target", "analyst", "upgrade", "downgrade", "dividend",
    "buyback", "ipo", "merger", "acquisition", "sec filing", "bankruptcy",
    "short squeeze", "federal reserve", "fed rate", "interest rate", "inflation",
    "jobs report", "payroll", "unemployment", "gdp", "treasury", "bond yield",
    "tariff", "trade war", "semiconductor", "chipmaker", "data center",
    "artificial intelligence", "bitcoin", "ethereum", "crypto", "stablecoin",
    "etf", "jackson hole", "powell", "nvidia", "micron", "sandisk", "tesla",
    "palantir", "broadcom", "marvell", "alphabet", "google stock", "apple stock",
    "microsoft stock", "amazon stock", "meta stock",
    "美股", "股票", "股市", "財報", "财报", "聯準會", "美聯儲", "美联储",
    "降息", "加息", "利率", "通膨", "通胀", "非農", "非农", "鮑威爾",
    "鲍威尔", "國債", "国债", "美債", "美债", "衰退", "英偉達",
    "英伟达", "美光", "閃迪", "闪迪", "台積電", "台积电", "博通",
    "蘋果", "苹果", "谷歌", "微軟", "微软", "亞馬遜", "亚马逊", "特斯拉",
    "半導體", "半导体", "晶片", "芯片", "記憶體", "内存", "資料中心",
    "数据中心", "光通訊", "光通信", "機器人", "机器人", "人工智慧",
    "人工智能", "比特幣", "比特币", "以太坊", "加密貨幣", "加密货币",
    "穩定幣", "稳定币", "關稅", "关税", "川普", "特朗普", "中美貿易",
    "中美贸易", "台股", "台灣科技股", "台湾科技股", "目標價", "目标价",
    "估值",
}


@dataclass
class BroadMeta:
    rank: int
    traffic: int
    geos: set[str]

    @property
    def score(self) -> float:
        traffic_units = max(1.0, self.traffic / 1_000.0)
        return min(
            70.0,
            18.0
            + 10.0 * math.log10(traffic_units)
            + 7.0 * max(0, len(self.geos) - 1),
        )

    @property
    def signal(self) -> str:
        traffic = f"{self.traffic:,}+" if self.traffic else "unknown"
        return f"GTrend {traffic} [{','.join(sorted(self.geos))}]"


def parse_compact_number(text: str) -> int:
    s = (text or "").strip().upper().replace(",", "").replace("+", "")
    m = re.search(r"([\d.]+)\s*([KMB]?)", s)
    if not m:
        return 0
    value = float(m.group(1))
    multiplier = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}[m.group(2)]
    return int(value * multiplier)


def looks_finance_context(text: str) -> bool:
    if scan.looks_finance(text):
        return True
    lowered = text.lower()
    return any(h.lower() in lowered for h in BROAD_FINANCE_HINTS)


def fetch_trending_geo(geo: str) -> list[dict[str, Any]]:
    r = requests.get(
        TRENDING_RSS_URL,
        params={"geo": geo, "hours": TRENDING_RSS_HOURS},
        headers={"User-Agent": "youtube-trends-scanner/1.0"},
        timeout=TRENDING_RSS_TIMEOUT,
    )
    r.raise_for_status()

    root = ET.fromstring(r.text)
    ns = {"ht": "https://trends.google.com/trending/rss"}
    rows: list[dict[str, Any]] = []

    for rank, item in enumerate(root.findall(".//item")[:TRENDING_RSS_PER_GEO], 1):
        title = scan.clean_query(item.findtext("title", default=""))
        if not title:
            continue

        traffic_text = item.findtext(
            "ht:approx_traffic",
            default="",
            namespaces=ns,
        )
        news_titles = [
            scan.clean_query(node.text or "")
            for node in item.findall(".//ht:news_item_title", ns)
            if scan.clean_query(node.text or "")
        ]
        context = " ".join([title] + news_titles)
        if not looks_finance_context(context):
            continue

        rows.append(
            {
                "query": title,
                "rank": rank,
                "geo": geo,
                "traffic": parse_compact_number(traffic_text),
            }
        )

    return rows


def discover_broad_trends(track: dict[str, Any]) -> tuple[dict[str, scan.Candidate], dict[str, BroadMeta]]:
    """Collect a cheap, broad candidate net from Google Trending RSS."""
    candidates: dict[str, scan.Candidate] = {}
    metadata: dict[str, BroadMeta] = {}

    if not TRENDING_RSS_GEOS:
        return candidates, metadata

    print(
        "[hybrid] Broad Google Trending scan: "
        f"{','.join(TRENDING_RSS_GEOS)} / {TRENDING_RSS_HOURS}h"
    )

    rows: list[dict[str, Any]] = []
    workers = min(5, len(TRENDING_RSS_GEOS))
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(fetch_trending_geo, geo): geo
            for geo in TRENDING_RSS_GEOS
        }
        for future in as_completed(futures):
            geo = futures[future]
            try:
                found = future.result()
                print(f"[hybrid] {geo}: {len(found)} finance-related broad trends")
                rows.extend(found)
            except Exception as exc:
                print(f"[warn] Trending RSS failed for {geo}: {exc}")

    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(row["query"].lower(), []).append(row)

    for key, hits in grouped.items():
        best = min(hits, key=lambda x: int(x["rank"]))
        meta = BroadMeta(
            rank=min(int(x["rank"]) for x in hits),
            traffic=max(int(x["traffic"]) for x in hits),
            geos={str(x["geo"]) for x in hits},
        )
        metadata[key] = meta
        candidates[key] = scan.Candidate(
            keyword=str(best["query"]),
            language=track["language"],
            geo=track["geo"],
            source="trending",
            discovery_rank=meta.rank,
            # Keep rising_boost at zero: Google Search gets a seat in the
            # candidate funnel but does not masquerade as YouTube Rising.
            rising_signal=meta.signal,
            rising_boost=0.0,
        )

    return candidates, metadata


def merge_broad(
    pool: dict[str, scan.Candidate],
    broad: dict[str, scan.Candidate],
    metadata: dict[str, BroadMeta],
) -> None:
    for key, incoming in broad.items():
        old = pool.get(key)
        if old is None:
            pool[key] = incoming
            continue

        old.source = scan.add_source(old.source, "trending")
        old.discovery_rank = min(old.discovery_rank, incoming.discovery_rank)

        # Preserve a real YouTube Rising signal when one exists. Otherwise show
        # the broad Google signal in the report for transparency.
        if not old.rising_signal:
            old.rising_signal = metadata[key].signal


def hybrid_preselect(
    track: dict[str, Any],
    pool: dict[str, scan.Candidate],
    broad_meta: dict[str, BroadMeta],
    limit: int,
) -> list[scan.Candidate]:
    """Both > YouTube Rising > capped broad trends > YouTube Top > seeds."""
    anchor_key = track["comparison_anchor"].lower()
    selected: list[scan.Candidate] = []
    seen: set[str] = set()

    def take(items: list[scan.Candidate], item_limit: int | None = None) -> bool:
        taken = 0
        for candidate in items:
            key = candidate.keyword.lower()
            if key == anchor_key or key in seen:
                continue
            selected.append(candidate)
            seen.add(key)
            taken += 1
            if len(selected) >= limit:
                return True
            if item_limit is not None and taken >= item_limit:
                break
        return len(selected) >= limit

    both = sorted(
        (
            c for c in pool.values()
            if c.rising_boost > 0 and c.keyword.lower() in broad_meta
        ),
        key=lambda c: (
            -c.rising_boost,
            -broad_meta[c.keyword.lower()].score,
            c.discovery_rank,
        ),
    )
    if take(both):
        return selected

    youtube_rising = sorted(
        (
            c for c in pool.values()
            if c.rising_boost > 0 and c.keyword.lower() not in broad_meta
        ),
        key=lambda c: (-c.rising_boost, c.discovery_rank),
    )

    broad_only = sorted(
        (
            pool[key] for key in broad_meta
            if key in pool and pool[key].rising_boost == 0
        ),
        key=lambda c: (
            -broad_meta[c.keyword.lower()].score,
            -broad_meta[c.keyword.lower()].traffic,
            broad_meta[c.keyword.lower()].rank,
        ),
    )

    # Keep the first exact Trends benchmark groups diverse. Six strong YouTube
    # Rising terms and up to six broad trends usually land inside the first
    # 12 candidates, so the broad-net ideas get genuine YouTube validation
    # instead of only a seed-like proxy.
    if take(youtube_rising[:6]):
        return selected
    broad_head = min(6, TRENDING_PRESELECT_LIMIT)
    if broad_head and take(broad_only[:broad_head]):
        return selected

    if take(youtube_rising[6:]):
        return selected

    if TRENDING_PRESELECT_LIMIT > broad_head:
        if take(broad_only[broad_head:TRENDING_PRESELECT_LIMIT]):
            return selected

    related_top = sorted(
        (
            c for c in pool.values()
            if "top" in c.source and c.rising_boost == 0
        ),
        key=lambda c: c.discovery_rank,
    )
    if take(related_top):
        return selected

    curated = [
        pool[seed.lower()]
        for seed in track["seeds"]
        if seed.lower() in pool
    ]
    if take(curated):
        return selected

    take(list(pool.values()))
    return selected


def main() -> None:
    config = scan.load_config()
    tracks = config.get("tracks") or []
    if not tracks:
        raise RuntimeError("keywords.json has no tracks")

    track = tracks[0]
    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()

    # Existing method: YouTube Search Rising/Top + curated seeds.
    pool = scan.discover(track)

    # New broad method: Google Trending list across multiple relevant regions,
    # filtered cheaply using titles + news context, then merged into the same pool.
    broad, broad_meta = discover_broad_trends(track)
    merge_broad(pool, broad, broad_meta)

    selected = hybrid_preselect(track, pool, broad_meta, scan.TOP_N)
    exact_benchmarks = scan.benchmark_trends(track, selected)

    for candidate in selected:
        candidate.opportunity_score = scan.final_score(candidate, False)

    if api_key:
        for i, candidate in enumerate(selected, 1):
            print(f"[youtube] {i}/{len(selected)} {candidate.keyword!r}")
            try:
                scan.youtube_competition(candidate, api_key)
            except Exception as exc:
                print(f"[warn] YouTube API failed for {candidate.keyword!r}: {exc}")
            candidate.opportunity_score = scan.final_score(candidate, True)

    print(
        f"[hybrid] merged pool={len(pool)} | broad finance candidates={len(broad_meta)} "
        f"| selected={len(selected)}"
    )
    scan.write_outputs(
        selected,
        bool(api_key),
        pool_size=len(pool),
        exact_benchmarks=exact_benchmarks,
    )


if __name__ == "__main__":
    main()
