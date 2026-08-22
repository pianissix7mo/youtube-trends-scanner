#!/usr/bin/env python3
"""Find worldwide Chinese-language YouTube search opportunities for investing content."""

from __future__ import annotations

import csv
import json
import math
import os
import re
import statistics
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests
import trendspyg.explore as trendspyg_explore
from trendspyg import download_google_trends_comparison, download_google_trends_explore
from trendspyg.downloader import validate_geo as _trendspyg_validate_geo

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
YT_API = "https://www.googleapis.com/youtube/v3"

TIMEFRAME = os.getenv("TRENDS_TIMEFRAME", "now 7-d")
TOP_N = int(os.getenv("TOP_N", "40"))
DISCOVERY_ANCHORS = int(os.getenv("DISCOVERY_ANCHORS", "5"))
TREND_BENCHMARK_GROUPS = int(os.getenv("TREND_BENCHMARK_GROUPS", "3"))
TRENDS_MAX_ATTEMPTS = max(1, int(os.getenv("TRENDS_MAX_ATTEMPTS", "1")))
TRENDS_RETRY_WAIT = float(os.getenv("TRENDS_RETRY_WAIT", "5"))
RELATED_RISING_PER_ANCHOR = 25
RELATED_TOP_PER_ANCHOR = 15
TREND_GROUP_SIZE = 4  # Google compares at most 5 terms; one slot is the shared anchor.
YOUTUBE_LOOKBACK_DAYS = 7
YOUTUBE_SAMPLE_SIZE = 50

# trendspyg validates only country/state codes, while Google Trends itself supports
# Worldwide with an empty geo. Its URL builder already accepts geo="", so allow it
# here without forking the dependency.
def _validate_geo_allow_worldwide(geo: str) -> str:
    if geo.strip().upper() in {"", "WW", "WORLDWIDE"}:
        return ""
    return _trendspyg_validate_geo(geo)


trendspyg_explore.validate_geo = _validate_geo_allow_worldwide

FINANCE_HINTS = {
    "美股", "股票", "股市", "財報", "财报", "盤前", "盘前", "盤後", "盘后", "納斯達克", "纳斯达克",
    "標普", "标普", "科技股", "成長股", "成长股", "聯準會", "美聯儲", "美联储", "降息", "加息", "利率",
    "通膨", "通胀", "非農", "非农", "鮑威爾", "鲍威尔", "國債", "国债", "美債", "美债", "衰退",
    "英偉達", "英伟达", "美光", "閃迪", "闪迪", "台積電", "台积电", "博通", "蘋果", "苹果", "谷歌",
    "微軟", "微软", "亞馬遜", "亚马逊", "特斯拉", "半導體", "半导体", "晶片", "芯片", "記憶體", "内存",
    "資料中心", "数据中心", "光通訊", "光通信", "機器人", "机器人", "人工智慧", "人工智能", "AI股票",
    "比特幣", "比特币", "以太坊", "加密貨幣", "加密货币", "穩定幣", "稳定币", "關稅", "关税", "川普",
    "特朗普", "中美貿易", "中美贸易", "台股", "台灣科技股", "台湾科技股", "目標價", "目标价", "估值",
}

FINANCE_TOKENS = {
    "sp500", "qqq", "spy", "tqqq", "vix", "cpi", "pce", "fomc", "nvda", "mu", "sndk", "tsm", "amd",
    "avgo", "mrvl", "arm", "asml", "amat", "lrcx", "klac", "aapl", "googl", "msft", "amzn", "meta", "tsla",
    "pltr", "orcl", "nflx", "crm", "adbe", "uber", "shop", "hbm", "dram", "nand", "cpo", "btc", "eth",
    "coin", "crcl", "sol", "mstr", "baba",
}


@dataclass
class Candidate:
    keyword: str
    language: str
    geo: str
    source: str = "seed"
    discovery_rank: int = 999
    rising_signal: str = ""
    rising_boost: float = 0.0
    trend_avg: float = 0.0
    anchor_avg: float = 0.0
    trend_score: float = 0.0
    trend_measured: bool = False
    momentum_pct: float = 0.0
    recent_video_estimate: int | None = None
    median_views: int | None = None
    median_views_per_day: int | None = None
    small_channel_hit_rate: float | None = None
    opportunity_score: float = 0.0


def load_config() -> dict[str, Any]:
    with open(ROOT / "keywords.json", encoding="utf-8") as f:
        return json.load(f)


def clean_query(q: str) -> str:
    return re.sub(r"\s+", " ", q).strip()


def looks_finance(q: str) -> bool:
    lowered = q.lower()
    compact = lowered.replace(" ", "")
    if any(h.lower().replace(" ", "") in compact for h in FINANCE_HINTS):
        return True
    tokens = set(re.findall(r"[a-z0-9&]+", lowered))
    return bool(tokens & FINANCE_TOKENS)


def parse_rising(item: dict[str, Any]) -> tuple[str, float]:
    text = str(item.get("formatted_value") or item.get("value") or "")
    if "breakout" in text.lower():
        return "Breakout", 100.0
    m = re.search(r"([\d,.]+)%", text)
    if m:
        pct = float(m.group(1).replace(",", ""))
        return text, min(80.0, 10.0 * math.log10(max(10.0, pct)))
    value = item.get("value")
    if isinstance(value, (int, float)) and value > 0:
        return str(value), min(70.0, 10.0 * math.log10(max(10.0, float(value))))
    return text, 15.0


def add_source(source: str, tag: str) -> str:
    parts = source.split("+") if source else []
    if tag not in parts:
        parts.append(tag)
    return "+".join(parts)


def trends_explore(keyword: str, geo: str) -> dict[str, Any]:
    return download_google_trends_explore(
        keyword,
        geo=geo,
        timeframe=TIMEFRAME,
        gprop="youtube",
        cache=False,
        cookies="disk",
        max_retries=TRENDS_MAX_ATTEMPTS,
        retry_wait=TRENDS_RETRY_WAIT,
    )


def trends_compare(keywords: list[str], geo: str) -> dict[str, Any]:
    return download_google_trends_comparison(
        keywords,
        geo=geo,
        timeframe=TIMEFRAME,
        gprop="youtube",
        cache=False,
        cookies="disk",
        max_retries=TRENDS_MAX_ATTEMPTS,
        retry_wait=TRENDS_RETRY_WAIT,
    )


def discover(track: dict[str, Any]) -> dict[str, Candidate]:
    geo, lang = track["geo"], track["language"]
    candidates = {
        seed.lower(): Candidate(seed, lang, geo)
        for seed in track["seeds"]
    }

    anchors = track["discovery_anchors"][:DISCOVERY_ANCHORS]
    for anchor in anchors:
        label = "Worldwide" if not geo else geo
        print(f"[trends] Explore {anchor!r} ({label}, YouTube Search)")
        try:
            env = trends_explore(anchor, geo)
        except Exception as exc:
            print(f"[warn] Explore failed for {anchor!r}: {exc}")
            continue

        rising = (env.get("related_queries") or {}).get("rising") or []
        for rank, item in enumerate(rising[:RELATED_RISING_PER_ANCHOR], 1):
            q = clean_query(str(item.get("query") or ""))
            if not q or not looks_finance(q):
                continue
            signal, boost = parse_rising(item)
            key = q.lower()
            old = candidates.get(key)
            if old is None:
                candidates[key] = Candidate(
                    q, lang, geo, "rising", rank, signal, boost
                )
            else:
                old.source = add_source(old.source, "rising")
                old.discovery_rank = min(old.discovery_rank, rank)
                if boost > old.rising_boost:
                    old.rising_signal = signal
                    old.rising_boost = boost

        top = (env.get("related_queries") or {}).get("top") or []
        for rank, item in enumerate(top[:RELATED_TOP_PER_ANCHOR], 1):
            q = clean_query(str(item.get("query") or ""))
            if not q or not looks_finance(q):
                continue
            key = q.lower()
            old = candidates.get(key)
            if old is None:
                candidates[key] = Candidate(q, lang, geo, "top", rank)
            else:
                old.source = add_source(old.source, "top")
                old.discovery_rank = min(old.discovery_rank, rank)

    return candidates


def preselect(track: dict[str, Any], pool: dict[str, Candidate], limit: int) -> list[Candidate]:
    """Prioritize Rising, then Top-related searches, then curated Chinese seeds."""
    anchor_key = track["comparison_anchor"].lower()
    selected: list[Candidate] = []
    seen: set[str] = set()

    def take(items: list[Candidate]) -> bool:
        for c in items:
            key = c.keyword.lower()
            if key == anchor_key or key in seen:
                continue
            selected.append(c)
            seen.add(key)
            if len(selected) >= limit:
                return True
        return False

    rising = sorted(
        (c for c in pool.values() if c.rising_boost > 0),
        key=lambda c: (-c.rising_boost, c.discovery_rank),
    )
    if take(rising):
        return selected

    related_top = sorted(
        (c for c in pool.values() if "top" in c.source and c.rising_boost == 0),
        key=lambda c: c.discovery_rank,
    )
    if take(related_top):
        return selected

    curated = [pool[seed.lower()] for seed in track["seeds"]]
    if take(curated):
        return selected

    take(list(pool.values()))
    return selected


def chunked(items: list[Candidate], size: int) -> list[list[Candidate]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def benchmark_trends(track: dict[str, Any], rows: list[Candidate]) -> int:
    """Measure several shared-anchor groups; remaining rows use a related-search proxy."""
    for c in rows:
        if c.rising_boost:
            c.trend_score = round(min(85.0, 12.0 + 0.70 * c.rising_boost), 1)
        elif "top" in c.source:
            c.trend_score = 20.0
        else:
            c.trend_score = 12.0

    anchor = track["comparison_anchor"]
    max_exact = max(0, TREND_BENCHMARK_GROUPS) * TREND_GROUP_SIZE
    benchmark = rows[:max_exact]
    measured = 0

    for group in chunked(benchmark, TREND_GROUP_SIZE):
        query = [anchor] + [c.keyword for c in group]
        print(f"[trends] Benchmark comparison: {query}")
        try:
            env = trends_compare(query, track["geo"])
        except Exception as exc:
            print(f"[warn] Benchmark comparison failed: {exc}")
            continue

        avgs = env.get("averages") or {}
        series = env.get("interest_over_time") or []
        anchor_avg = float(avgs.get(anchor, 0) or 0)

        for c in group:
            c.trend_avg = float(avgs.get(c.keyword, 0) or 0)
            c.anchor_avg = anchor_avg
            ratio = c.trend_avg / max(1.0, anchor_avg)
            c.trend_score = round(100.0 * ratio / (1.0 + ratio), 1)
            c.trend_measured = True
            measured += 1

            values = [
                float((p.get("values") or {}).get(c.keyword, 0) or 0)
                for p in series
            ]
            if len(values) >= 4:
                w = max(1, len(values) // 4)
                recent = statistics.fmean(values[-w:])
                previous = statistics.fmean(values[-2 * w : -w]) if len(values) >= 2 * w else 0
                c.momentum_pct = round(
                    100.0 * (recent - previous) / max(1.0, previous),
                    1,
                )

    return measured


def youtube_get(endpoint: str, key: str, **params: Any) -> dict[str, Any]:
    params["key"] = key
    r = requests.get(f"{YT_API}/{endpoint}", params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def youtube_competition(c: Candidate, api_key: str) -> None:
    after = (
        datetime.now(timezone.utc) - timedelta(days=YOUTUBE_LOOKBACK_DAYS)
    ).isoformat().replace("+00:00", "Z")
    params: dict[str, Any] = {
        "part": "snippet",
        "q": c.keyword,
        "type": "video",
        "maxResults": YOUTUBE_SAMPLE_SIZE,
        "publishedAfter": after,
        "order": "relevance",
        "safeSearch": "none",
        "relevanceLanguage": "zh",
    }
    # Empty geo intentionally means worldwide; do not send regionCode.
    if len(c.geo) == 2:
        params["regionCode"] = c.geo

    data = youtube_get("search", api_key, **params)
    c.recent_video_estimate = int((data.get("pageInfo") or {}).get("totalResults", 0) or 0)
    items = data.get("items") or []
    ids = [x.get("id", {}).get("videoId") for x in items if x.get("id", {}).get("videoId")]
    if not ids:
        return

    vids = youtube_get(
        "videos",
        api_key,
        part="statistics,snippet",
        id=",".join(ids),
        maxResults=YOUTUBE_SAMPLE_SIZE,
    )
    now = datetime.now(timezone.utc)
    views: list[int] = []
    views_per_day: list[float] = []
    channel_ids: list[str] = []
    video_rows: list[tuple[int, str | None]] = []

    for v in vids.get("items") or []:
        stats, snip = v.get("statistics") or {}, v.get("snippet") or {}
        view = int(stats.get("viewCount", 0) or 0)
        published = datetime.fromisoformat(snip["publishedAt"].replace("Z", "+00:00"))
        days = max((now - published).total_seconds() / 86400.0, 0.25)
        views.append(view)
        views_per_day.append(view / days)
        cid = snip.get("channelId")
        if cid:
            channel_ids.append(cid)
        video_rows.append((view, cid))

    c.median_views = int(statistics.median(views)) if views else None
    c.median_views_per_day = int(statistics.median(views_per_day)) if views_per_day else None

    if channel_ids:
        chans = youtube_get(
            "channels",
            api_key,
            part="statistics",
            id=",".join(sorted(set(channel_ids))),
            maxResults=50,
        )
        subs = {
            x["id"]: int((x.get("statistics") or {}).get("subscriberCount", 0) or 0)
            for x in chans.get("items") or []
            if not (x.get("statistics") or {}).get("hiddenSubscriberCount")
        }
        eligible = [(view, subs.get(cid)) for view, cid in video_rows if cid in subs]
        if eligible:
            hits = sum(
                1
                for view, sub in eligible
                if sub is not None and sub < 50_000 and view >= 1_000
            )
            c.small_channel_hit_rate = round(100.0 * hits / len(eligible), 1)


def final_score(c: Candidate, has_youtube: bool) -> float:
    momentum = max(-50.0, min(200.0, c.momentum_pct))
    demand = (
        0.55 * c.trend_score
        + 0.25 * c.rising_boost
        + 0.20 * max(0.0, momentum) / 2
    )
    if not has_youtube or c.recent_video_estimate is None:
        return round(demand, 1)

    vpd = c.median_views_per_day or 0
    supply = max(1, c.recent_video_estimate)
    performance = min(100.0, 18.0 * math.log10(1.0 + vpd))
    scarcity = 100.0 / (1.0 + math.log10(1.0 + supply))
    small = c.small_channel_hit_rate or 0.0
    return round(
        0.45 * demand
        + 0.25 * performance
        + 0.20 * scarcity
        + 0.10 * small,
        1,
    )


def write_outputs(
    rows: list[Candidate],
    api_enabled: bool,
    pool_size: int,
    exact_benchmarks: int,
) -> None:
    OUT.mkdir(exist_ok=True)
    rows.sort(key=lambda x: x.opportunity_score, reverse=True)
    rows = rows[:TOP_N]
    fields = list(asdict(rows[0]).keys()) if rows else list(asdict(Candidate("", "", "")).keys())

    with open(OUT / "latest.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(asdict(r) for r in rows)

    with open(OUT / "latest.json", "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in rows], f, ensure_ascii=False, indent=2)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# Worldwide Chinese YouTube Search Opportunity Radar — {stamp}",
        "",
        f"Candidate pool: **{pool_size}** | YouTube deep checks: **{len(rows)}** | Exact Trends benchmarks: **{exact_benchmarks}**",
        "",
    ]
    if not api_enabled:
        lines += [
            "> `YOUTUBE_API_KEY` is not set, so this run contains Google Trends demand signals only.",
            "",
        ]
    lines += [
        "| # | Keyword | Source | Trend | Momentum | Rising | 7d videos* | Median views/day | Small-channel hit | Score |",
        "|---:|---|---|---:|---:|---|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(rows, 1):
        trend = f"{r.trend_score:.1f}" if r.trend_measured else f"~{r.trend_score:.1f}"
        lines.append(
            f"| {i} | {r.keyword} | {r.source} | {trend} | {r.momentum_pct:+.1f}% | "
            f"{r.rising_signal or '—'} | "
            f"{r.recent_video_estimate if r.recent_video_estimate is not None else '—'} | "
            f"{r.median_views_per_day if r.median_views_per_day is not None else '—'} | "
            f"{(str(r.small_channel_hit_rate) + '%') if r.small_channel_hit_rate is not None else '—'} | "
            f"{r.opportunity_score:.1f} |"
        )

    lines += [
        "",
        "* Google Trends property: YouTube Search; geography: Worldwide; query pool: Chinese/traditional Chinese plus ticker symbols used by Chinese-speaking investors.",
        "* YouTube `search.list` totalResults is an estimate for videos published in the last 7 days; no regionCode is applied.",
        "* `~Trend` is a Rising/Top-related proxy for candidates not included in an exact shared-anchor comparison.",
    ]
    (OUT / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n" + "\n".join(lines))


def main() -> None:
    config = load_config()
    tracks = config.get("tracks") or []
    if not tracks:
        raise RuntimeError("keywords.json has no tracks")

    # This project intentionally runs one worldwide Chinese-audience track.
    track = tracks[0]
    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()

    pool = discover(track)
    selected = preselect(track, pool, TOP_N)
    exact_benchmarks = benchmark_trends(track, selected)

    for c in selected:
        c.opportunity_score = final_score(c, False)

    if api_key:
        for i, c in enumerate(selected, 1):
            print(f"[youtube] {i}/{len(selected)} {c.keyword!r}")
            try:
                youtube_competition(c, api_key)
            except Exception as exc:
                print(f"[warn] YouTube API failed for {c.keyword!r}: {exc}")
            c.opportunity_score = final_score(c, True)

    write_outputs(
        selected,
        bool(api_key),
        pool_size=len(pool),
        exact_benchmarks=exact_benchmarks,
    )


if __name__ == "__main__":
    main()
