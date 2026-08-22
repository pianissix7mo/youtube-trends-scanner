#!/usr/bin/env python3
"""Find YouTube-search opportunities for a Chinese-language US-stock channel."""

from __future__ import annotations

import csv
import json
import math
import os
import re
import statistics
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests
from trendspyg import download_google_trends_comparison, download_google_trends_explore

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
YT_API = "https://www.googleapis.com/youtube/v3"
TIMEFRAME = os.getenv("TRENDS_TIMEFRAME", "now 7-d")
TOP_N = int(os.getenv("TOP_N", "20"))
MAX_CANDIDATES_PER_LANGUAGE = int(os.getenv("MAX_CANDIDATES_PER_LANGUAGE", "16"))

FINANCE_HINTS = {
    "stock", "stocks", "market", "nasdaq", "sp500", "s&p", "earnings", "fed", "rate", "rates",
    "inflation", "bitcoin", "btc", "ethereum", "eth", "nvidia", "nvda", "micron", "mu", "sandisk",
    "sndk", "google", "googl", "alphabet", "tesla", "tsla", "palantir", "pltr", "amd", "broadcom",
    "avgo", "semiconductor", "chip", "ai", "ipo", "etf", "recession", "trump", "tariff",
    "美股", "股票", "股市", "财报", "財報", "美联储", "美聯儲", "降息", "加息", "利率", "通胀",
    "通膨", "英伟达", "英偉達", "美光", "闪迪", "閃迪", "比特币", "比特幣", "以太坊", "谷歌",
    "特斯拉", "半导体", "半導體", "芯片", "晶片", "人工智能", "人工智慧", "估值", "目标价", "目標價",
}


@dataclass
class Candidate:
    keyword: str
    language: str
    geo: str
    source: str = "seed"
    rising_signal: str = ""
    rising_boost: float = 0.0
    trend_avg: float = 0.0
    anchor_avg: float = 0.0
    trend_score: float = 0.0
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
    s = q.lower().replace(" ", "")
    return any(h.lower().replace(" ", "") in s for h in FINANCE_HINTS)


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


def discover(track: dict[str, Any]) -> dict[str, Candidate]:
    candidates: dict[str, Candidate] = {}
    geo, lang = track["geo"], track["language"]
    for seed in track["seeds"]:
        candidates[seed.lower()] = Candidate(seed, lang, geo)

    for anchor in track["discovery_anchors"]:
        print(f"[trends] Discovering related YouTube searches: {anchor!r} ({geo})")
        try:
            env = download_google_trends_explore(
                anchor,
                geo=geo,
                timeframe=TIMEFRAME,
                gprop="youtube",
                cache=False,
            )
        except Exception as exc:
            print(f"[warn] discovery failed for {anchor!r}: {exc}")
            continue
        rising = (env.get("related_queries") or {}).get("rising") or []
        for item in rising[:20]:
            q = clean_query(str(item.get("query") or ""))
            if not q or not looks_finance(q):
                continue
            key = q.lower()
            signal, boost = parse_rising(item)
            old = candidates.get(key)
            if old is None:
                candidates[key] = Candidate(q, lang, geo, "rising", signal, boost)
            elif boost > old.rising_boost:
                old.source = "seed+rising"
                old.rising_signal, old.rising_boost = signal, boost
    return candidates


def chunks(items: list[str], n: int) -> list[list[str]]:
    return [items[i : i + n] for i in range(0, len(items), n)]


def score_trends(track: dict[str, Any], pool: dict[str, Candidate]) -> list[Candidate]:
    anchor = track["comparison_anchor"]
    keys = list(pool.keys())
    keys.sort(key=lambda k: (pool[k].rising_boost, pool[k].source != "seed"), reverse=True)
    keys = keys[:MAX_CANDIDATES_PER_LANGUAGE]
    if anchor.lower() not in keys:
        keys.insert(0, anchor.lower())
        pool.setdefault(anchor.lower(), Candidate(anchor, track["language"], track["geo"]))

    results: list[Candidate] = []
    terms = [pool[k].keyword for k in keys if k != anchor.lower()]
    for group in chunks(terms, 4):
        query = [anchor] + group
        print(f"[trends] Comparing YouTube searches: {query}")
        try:
            env = download_google_trends_comparison(
                query,
                geo=track["geo"],
                timeframe=TIMEFRAME,
                gprop="youtube",
                cache=False,
            )
        except Exception as exc:
            print(f"[warn] comparison failed: {exc}")
            continue
        avgs = env.get("averages") or {}
        series = env.get("interest_over_time") or []
        anchor_avg = float(avgs.get(anchor, 0) or 0)
        for term in group:
            c = pool[term.lower()]
            c.trend_avg = float(avgs.get(term, 0) or 0)
            c.anchor_avg = anchor_avg
            ratio = c.trend_avg / max(1.0, anchor_avg)
            c.trend_score = round(100.0 * ratio / (1.0 + ratio), 1)
            values = [float((p.get("values") or {}).get(term, 0) or 0) for p in series]
            if len(values) >= 4:
                w = max(1, len(values) // 4)
                recent = statistics.fmean(values[-w:])
                previous = statistics.fmean(values[-2 * w : -w]) if len(values) >= 2 * w else 0
                c.momentum_pct = round(100.0 * (recent - previous) / max(1.0, previous), 1)
            results.append(c)
    return results


def youtube_get(endpoint: str, key: str, **params: Any) -> dict[str, Any]:
    params["key"] = key
    r = requests.get(f"{YT_API}/{endpoint}", params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def youtube_competition(c: Candidate, api_key: str) -> None:
    after = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat().replace("+00:00", "Z")
    params: dict[str, Any] = {
        "part": "snippet", "q": c.keyword, "type": "video", "maxResults": 50,
        "publishedAfter": after, "order": "relevance", "safeSearch": "none",
        "relevanceLanguage": "en" if c.language == "en" else "zh-Hans",
    }
    if len(c.geo) == 2:
        params["regionCode"] = c.geo
    data = youtube_get("search", api_key, **params)
    c.recent_video_estimate = int((data.get("pageInfo") or {}).get("totalResults", 0) or 0)
    items = data.get("items") or []
    ids = [x.get("id", {}).get("videoId") for x in items if x.get("id", {}).get("videoId")]
    if not ids:
        return

    vids = youtube_get("videos", api_key, part="statistics,snippet", id=",".join(ids), maxResults=50)
    views, views_per_day, channel_ids = [], [], []
    now = datetime.now(timezone.utc)
    video_rows = []
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
        chans = youtube_get("channels", api_key, part="statistics", id=",".join(sorted(set(channel_ids))), maxResults=50)
        subs = {
            x["id"]: int((x.get("statistics") or {}).get("subscriberCount", 0) or 0)
            for x in chans.get("items") or []
            if not (x.get("statistics") or {}).get("hiddenSubscriberCount")
        }
        eligible = [(view, subs.get(cid)) for view, cid in video_rows if cid in subs]
        if eligible:
            hits = sum(1 for view, sub in eligible if sub is not None and sub < 50_000 and view >= 1_000)
            c.small_channel_hit_rate = round(100.0 * hits / len(eligible), 1)


def final_score(c: Candidate, has_youtube: bool) -> float:
    momentum = max(-50.0, min(200.0, c.momentum_pct))
    demand = 0.55 * c.trend_score + 0.25 * c.rising_boost + 0.20 * max(0.0, momentum) / 2
    if not has_youtube or c.recent_video_estimate is None:
        return round(demand, 1)
    vpd = c.median_views_per_day or 0
    supply = max(1, c.recent_video_estimate)
    performance = min(100.0, 18.0 * math.log10(1.0 + vpd))
    scarcity = 100.0 / (1.0 + math.log10(1.0 + supply))
    small = c.small_channel_hit_rate or 0.0
    return round(0.45 * demand + 0.25 * performance + 0.20 * scarcity + 0.10 * small, 1)


def write_outputs(rows: list[Candidate], api_enabled: bool) -> None:
    OUT.mkdir(exist_ok=True)
    rows.sort(key=lambda x: x.opportunity_score, reverse=True)
    rows = rows[:TOP_N]
    fields = list(asdict(rows[0]).keys()) if rows else list(Candidate("", "", "").__dict__.keys())
    with open(OUT / "latest.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(asdict(r) for r in rows)
    with open(OUT / "latest.json", "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in rows], f, ensure_ascii=False, indent=2)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"# YouTube Search Opportunity Radar — {stamp}", ""]
    if not api_enabled:
        lines += ["> `YOUTUBE_API_KEY` is not set, so this run contains Google Trends demand signals only.", ""]
    lines += [
        "| # | Keyword | Lang | Trend | Momentum | Rising | 7d videos* | Median views/day | Small-channel hit | Score |",
        "|---:|---|:---:|---:|---:|---|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(rows, 1):
        lines.append(
            f"| {i} | {r.keyword} | {r.language} | {r.trend_score:.1f} | {r.momentum_pct:+.1f}% | "
            f"{r.rising_signal or '—'} | {r.recent_video_estimate if r.recent_video_estimate is not None else '—'} | "
            f"{r.median_views_per_day if r.median_views_per_day is not None else '—'} | "
            f"{(str(r.small_channel_hit_rate) + '%') if r.small_channel_hit_rate is not None else '—'} | {r.opportunity_score:.1f} |"
        )
    lines += ["", "* YouTube `search.list` totalResults is an estimate for videos published in the last 7 days.",
              "Trend values are normalized against a shared anchor within each language track; English and Chinese scores are opportunity signals, not absolute search volumes."]
    (OUT / "latest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n" + "\n".join(lines))


def main() -> None:
    config = load_config()
    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()
    all_rows: list[Candidate] = []
    for track in config["tracks"]:
        pool = discover(track)
        all_rows.extend(score_trends(track, pool))

    for c in all_rows:
        c.opportunity_score = final_score(c, False)
    all_rows.sort(key=lambda x: x.opportunity_score, reverse=True)
    per_language = max(1, TOP_N // 2)
    english = [c for c in all_rows if c.language == "en"][:per_language]
    chinese = [c for c in all_rows if c.language == "zh"][:per_language]
    yt_candidates = english + chinese
    if len(yt_candidates) < TOP_N:
        used = {id(c) for c in yt_candidates}
        yt_candidates += [c for c in all_rows if id(c) not in used][: TOP_N - len(yt_candidates)]
    if api_key:
        for i, c in enumerate(yt_candidates, 1):
            print(f"[youtube] {i}/{len(yt_candidates)} {c.keyword!r}")
            try:
                youtube_competition(c, api_key)
            except Exception as exc:
                print(f"[warn] YouTube API failed for {c.keyword!r}: {exc}")
            c.opportunity_score = final_score(c, True)
    write_outputs(yt_candidates, bool(api_key))


if __name__ == "__main__":
    main()
