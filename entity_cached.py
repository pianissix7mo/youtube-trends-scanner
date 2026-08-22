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

# Stores the canonical display name for each representative Candidate object.
ENTITY_DISPLAY: dict[int, str] = {}


def compact_text(text: str) -> str:
    return re.sub(r"[\s\-_·•|]+", "", (text or "").strip().lower())


def latin_tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9&]+", (text or "").lower()))


def alias_matches(query: str, alias: str) -> bool:
    alias_l = alias.lower()
    # CJK aliases: removing spaces is important because Trends often returns
    # queries like "比特 幣" or "台積電 亞利桑那 州 廠".
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

    # Broad Google Trending candidates have already passed the finance/news
    # context filter. Keep an unfamiliar proper-name trend as its own entity so
    # the scanner can still discover stocks that are not in our curated map.
    if "trending" in candidate.source:
        return query.strip()

    # Related-query candidates that do not map to a known company/asset are
    # usually generic intents (analysis, how-to, options, live stream, etc.).
    # Dropping them is intentional: the final list is entity-focused.
    return None


def entity_preselect(
    track: dict[str, Any],
    pool: dict[str, scan.Candidate],
    broad_meta: dict[str, hybrid_scan.BroadMeta],
    limit: int,
) -> list[scan.Candidate]:
    """Return at most one strongest query per stock/company/asset entity."""
    # Ask the original selector for a much wider cheap shortlist. Only the
    # deduped final list gets exact Trends benchmarks and YouTube API calls.
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
            print(
                f"[entity] duplicate removed: {candidate.keyword!r} -> {entity}"
            )
            continue

        seen_entities.add(entity_key)
        ENTITY_DISPLAY[id(candidate)] = entity
        selected.append(candidate)
        print(f"[entity] keep: {candidate.keyword!r} -> {entity}")
        if len(selected) >= limit:
            break

    return selected


def entity_write_outputs(
    rows: list[scan.Candidate],
    api_enabled: bool,
    pool_size: int,
    exact_benchmarks: int,
) -> None:
    # All scoring and cache calls have already used the strongest representative
    # long-tail query. Only now replace it with the clean canonical entity name.
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
scan.write_outputs = entity_write_outputs


if __name__ == "__main__":
    hybrid_scan.main()
