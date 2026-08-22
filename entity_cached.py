#!/usr/bin/env python3
"""Entity-focused wrapper for the hybrid YouTube trend scanner.

Discovery stays broad, but before exact Trends benchmarks / YouTube API calls we
collapse all long-tail queries about the same stock/company/asset into one slot.
The strongest discovered query represents the entity for scoring; the final
report shows the canonical entity name.
"""

from __future__ import annotations

import re
from typing import Any

# Importing hybrid_cached installs the YouTube metrics cache patch.
import hybrid_cached  # noqa: F401
import hybrid_scan
import scan


ORIGINAL_PRESELECT = hybrid_scan.hybrid_preselect
ORIGINAL_WRITE_OUTPUTS = scan.write_outputs
ORIGINAL_FINAL_SCORE = scan.final_score

# Canonical display name -> aliases. Chinese aliases are matched after removing
# spaces; Latin ticker aliases are token-matched to avoid accidental substrings.
ENTITY_ALIASES: dict[str, tuple[str, ...]] = {
    "TSMC": ("台積電", "台积电", "tsmc", "tsm"),
    "Apple": ("蘋果", "苹果", "apple", "aapl"),
    "NVIDIA": ("英偉達", "英伟达", "nvidia", "nvda"),
    "Micron": ("美光", "micron", "mu"),
    "SanDisk": ("閃迪", "闪迪", "sandisk", "sndk"),
    "AMD": ("amd",),
    "Broadcom": ("博通", "broadcom", "avgo"),
    "Marvell": ("marvell", "mrvl"),
    "Arm": ("arm holdings", "arm"),
    "ASML": ("asml",),
    "Applied Materials": ("應用材料", "应用材料", "applied materials", "amat"),
    "Lam Research": ("lam research", "lrcx"),
    "KLA": ("kla", "klac"),
    "Intel": ("intel", "intc"),
    "Qualcomm": ("qualcomm", "qcom"),
    "Applied Optoelectronics": ("applied optoelectronics", "aaoi"),
    "Lumentum": ("lumentum", "lite"),
    "Coherent": ("coherent", "cohr"),
    "Vertiv": ("vertiv", "vrt"),
    "Arista Networks": ("arista networks", "anet"),
    "CoreWeave": ("coreweave", "crwv"),
    "Dell": ("dell technologies", "dell"),
    "Super Micro Computer": ("super micro computer", "supermicro", "smci"),
    "Alphabet": ("谷歌", "google", "alphabet", "googl", "goog"),
    "Microsoft": ("微軟", "微软", "microsoft", "msft"),
    "Amazon": ("亞馬遜", "亚马逊", "amazon", "amzn"),
    "Meta": ("meta platforms", "meta"),
    "Tesla": ("特斯拉", "tesla", "tsla"),
    "Palantir": ("palantir", "pltr"),
    "Oracle": ("oracle", "orcl"),
    "Netflix": ("netflix", "nflx"),
    "Salesforce": ("salesforce", "crm"),
    "Adobe": ("adobe", "adbe"),
    "Uber": ("uber",),
    "Shopify": ("shopify", "shop"),
    "Alibaba": ("阿里巴巴", "alibaba", "baba"),
    "Walmart": ("walmart", "wmt"),
    "Costco": ("costco", "cost"),
    "Robinhood": ("robinhood", "hood"),
    "SoFi": ("sofi",),
    "Reddit": ("reddit", "rddt"),
    "Rocket Lab": ("rocket lab", "rklb"),
    "AST SpaceMobile": ("ast spacemobile", "asts"),
    "GE Vernova": ("ge vernova", "gev"),
    "Vistra": ("vistra", "vst"),
    "Constellation Energy": ("constellation energy", "ceg"),
    "Oklo": ("oklo",),
    "Coinbase": ("coinbase", "coin"),
    "Circle": ("circle internet", "circle", "crcl"),
    "Strategy": ("microstrategy", "strategy", "mstr"),
    "Bitcoin": ("比特幣", "比特币", "bitcoin", "btc"),
    "Ethereum": ("以太坊", "ethereum", "eth"),
    "Solana": ("solana", "sol"),
    "SPY": ("spy",),
    "QQQ": ("qqq",),
    "TQQQ": ("tqqq",),
    "VIX": ("vix", "恐慌指數", "恐慌指数"),
}

GENERIC_NON_ENTITY = {
    "美股", "股票", "股市", "美股分析", "美股投資", "美股投资", "美股直播",
    "美股期權", "美股期权", "美股泡沫", "科技股", "成長股", "成长股",
    "財報", "财报", "降息", "加息", "利率", "通膨", "通胀", "新聞", "新闻",
    "etf", "stock", "stocks", "stockmarket", "market", "crypto", "cryptocurrency",
}

COMPANYISH_MARKERS = (
    " group", " holdings", " corporation", " corp", " technologies", " technology",
    " semiconductor", " bank", " energy", " systems", " networks", " inc", " ltd",
    "集團", "集团", "科技", "公司", "控股", "銀行", "银行", "股份", "能源",
)

# Stores the canonical display name for each representative Candidate object.
ENTITY_DISPLAY: dict[int, str] = {}


def compact_text(text: str) -> str:
    return re.sub(r"[\s\-_·•|]+", "", (text or "").strip().lower())


def latin_tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9&]+", (text or "").lower()))


def alias_matches(query: str, alias: str) -> bool:
    alias_l = alias.lower()
    if re.search(r"[^\x00-\x7f]", alias_l):
        return compact_text(alias_l) in compact_text(query)

    alias_tokens = re.findall(r"[a-z0-9&]+", alias_l)
    if len(alias_tokens) == 1 and len(alias_tokens[0]) <= 5:
        return alias_tokens[0] in latin_tokens(query)
    return alias_l in query.lower()


def canonical_entity(candidate: scan.Candidate) -> str | None:
    query = candidate.keyword
    for display, aliases in ENTITY_ALIASES.items():
        if any(alias_matches(query, alias) for alias in aliases):
            return display

    compact = compact_text(query)
    if compact in {compact_text(x) for x in GENERIC_NON_ENTITY}:
        return None

    # Unknown broad-list terms only survive when the name itself looks like a
    # company. This keeps discovery open to new stocks without admitting sports,
    # celebrities, how-to queries, or other accidental finance-context matches.
    if "trending" in candidate.source:
        lowered = f" {query.lower()}"
        if any(marker in lowered for marker in COMPANYISH_MARKERS):
            return query.strip()

    return None


def entity_preselect(
    track: dict[str, Any],
    pool: dict[str, scan.Candidate],
    broad_meta: dict[str, hybrid_scan.BroadMeta],
    limit: int,
) -> list[scan.Candidate]:
    """Return at most one strongest query per stock/company/asset entity."""
    wide_limit = min(len(pool), max(120, limit * 6))
    ranked = ORIGINAL_PRESELECT(track, pool, broad_meta, wide_limit)

    selected: list[scan.Candidate] = []
    seen_entities: set[str] = set()
    ENTITY_DISPLAY.clear()

    for candidate in ranked:
        entity = canonical_entity(candidate)
        if not entity:
            continue
        entity_key = compact_text(entity)
        if entity_key in seen_entities:
            print(f"[entity] duplicate removed: {candidate.keyword!r} -> {entity}")
            continue

        seen_entities.add(entity_key)
        ENTITY_DISPLAY[id(candidate)] = entity
        selected.append(candidate)
        print(f"[entity] keep: {candidate.keyword!r} -> {entity}")
        if len(selected) >= limit:
            break

    return selected


def entity_final_score(candidate: scan.Candidate, has_youtube: bool) -> float:
    # If the YouTube deep check did not complete, do not let a pure Trends proxy
    # outrank fully checked entities. Cached metrics count as completed checks.
    if has_youtube and candidate.recent_video_estimate is None:
        return 0.0
    return ORIGINAL_FINAL_SCORE(candidate, has_youtube)


def entity_write_outputs(
    rows: list[scan.Candidate],
    api_enabled: bool,
    pool_size: int,
    exact_benchmarks: int,
) -> None:
    # Scoring/cache calls use the strongest representative long-tail query.
    # Only the final report is renamed to one clean canonical entity per row.
    originals: list[tuple[scan.Candidate, str]] = []
    for candidate in rows:
        display = ENTITY_DISPLAY.get(id(candidate))
        if display:
            originals.append((candidate, candidate.keyword))
            candidate.keyword = display
    try:
        ORIGINAL_WRITE_OUTPUTS(rows, api_enabled, pool_size, exact_benchmarks)
    finally:
        for candidate, original in originals:
            candidate.keyword = original


hybrid_scan.hybrid_preselect = entity_preselect
scan.final_score = entity_final_score
scan.write_outputs = entity_write_outputs


if __name__ == "__main__":
    hybrid_scan.main()
