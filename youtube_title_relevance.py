#!/usr/bin/env python3
"""Shared, conservative YouTube TITLE relevance checks for scanners A/B/C/D.

A YouTube search result is a candidate, not evidence of demand for the named
stock or the specific news event.  No external API or LLM calls are made here.
"""
from __future__ import annotations

import re
import unicodedata

FILTER_VERSION = "entity_event_v2"

# Short words and common vocabulary are unsafe as standalone company evidence.
AMBIGUOUS_TICKERS = {
    "A", "AI", "ALL", "AM", "ARE", "AT", "BE", "BIG", "BP", "BY",
    "C", "CAN", "CAT", "CO", "D", "DO", "F", "FOR", "GO", "IT",
    "L", "LOW", "M", "ON", "OR", "T", "U", "US", "NOW",
}
ALIASES = {
    "BP": ("bp plc", "british petroleum", "英国石油", "英國石油"),
    "MSFT": ("microsoft", "微软", "微軟"),
    "TSM": ("tsmc", "台积电", "台積電", "taiwan semiconductor"),
    "NVDA": ("nvidia", "英伟达", "英偉達", "輝達", "辉达"),
    "AAPL": ("apple", "苹果公司", "蘋果公司"),
    "META": ("meta platforms", "facebook", "脸书", "臉書"),
    "WOLF": ("wolfspeed",),
    "RTX": ("raytheon", "雷神公司"),
    "SBUX": ("starbucks", "星巴克"),
    "DAL": ("delta air lines", "delta airlines", "达美航空", "達美航空"),
    "HOOD": ("robinhood",),
    "PRU": ("prudential financial", "保德信"),
}
# Financial/company context alone cannot justify an event match, but it can
# disambiguate common-word stock symbols.
MARKET_CONTEXT = (
    "stock", "stocks", "shares", "share price", "trading", "earnings",
    "nyse", "nasdaq", "investor", "dividend", "guidance", "market cap",
    "股价", "股價", "股票", "财报", "財報", "证券", "證券", "投资", "投資",
)
BP_ENERGY_CONTEXT = (
    "oil", "petroleum", "energy", "crude", "refinery", "gas field",
    "gulf of mexico", "offshore", "drilling", "production platform",
    "石油", "原油", "油气", "油氣", "炼油", "煉油", "墨西哥湾", "墨西哥灣",
)
# Generic event words may match unrelated company coverage and require two
# distinct matched words if no identifiable counterparty/specific event term.
GENERIC_EVENT_TERMS = {
    "earnings", "guidance", "profit", "revenue", "sales", "forecast",
    "fuel", "production", "orders", "investment", "power", "loan",
    "regulator", "japan", "insurance", "contract", "stock", "stocks",
    "shares", "takeover", "acquisition", "buyout", "hurricane",
    "gulf", "etf", "bitcoin", "ether", "gpu", "ai", "deal", "growth",
    "interest", "rates", "market", "company", "results", "new",
}
EVENT_SYNONYMS = {
    "vulnerability": ("vulnerability", "security flaw", "critical bug", "bug fix",
                      "exploit", "安全漏洞", "安全缺陷", "漏洞"),
    "tokenized": ("tokenized", "tokenization", "代币化", "代幣化"),
    "interposer": ("interposer", "中介层", "中介層"),
    "d-matrix": ("d-matrix", "dmatrix"),
    "sm-3": ("sm-3", "sm3"),
}


def normalize(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", str(text or "")).casefold().split())


def has_phrase(text: str, term: str) -> bool:
    """Whole-token Latin match; contiguous CJK phrases match without spaces."""
    needle = normalize(term)
    if not needle:
        return False
    hay = normalize(text)
    if re.search(r"[a-z0-9]", needle):
        return re.search(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", hay) is not None
    return needle in hay


def any_phrase(title: str, terms: tuple[str, ...] | list[str]) -> bool:
    return any(has_phrase(title, x) for x in terms)


def entity_aliases(entity: str, ticker: str = "") -> tuple[str, ...]:
    ticker = normalize(ticker).upper()
    cleaned = re.sub(r"\b(?:incorporated|inc|corporation|corp|company|co|ltd|plc|holdings|group)\b[.,]*", " ", entity, flags=re.I)
    cleaned = " ".join(cleaned.split()).strip(" ,.")
    aliases = [*ALIASES.get(ticker, ())]
    if len(cleaned) >= 4 and "/" not in cleaned:
        aliases.append(cleaned)
    if len(entity.strip()) >= 4 and "/" not in entity:
        aliases.append(entity)
    return tuple(dict.fromkeys(normalize(a) for a in aliases if a.strip()))


def company_in_title(title: str, entity: str, ticker: str = "") -> bool:
    """Reject incidental ticker mentions and ambiguous ticker homonyms."""
    ticker = normalize(ticker).upper()
    aliases = entity_aliases(entity, ticker)
    # For titles with several tickers, the company must be a material focus.
    head = title[:110]
    if any_phrase(head, aliases):
        # Apple is also a fruit; an Apple stock/iPhone video needs a tech or
        # investing cue before its metrics can influence an equity report.
        if ticker == "AAPL" and has_phrase(head, "apple"):
            return any_phrase(title, MARKET_CONTEXT + (
                "iphone", "ipad", "macbook", "mac", "ios", "airpods",
                "苹果手机", "蘋果手機", "苹果公司", "蘋果公司",
            ))
        return True
    if not ticker or not has_phrase(head, ticker):
        return False
    if ticker == "BP":
        return any_phrase(title, BP_ENERGY_CONTEXT)
    if ticker in AMBIGUOUS_TICKERS:
        return any_phrase(title, MARKET_CONTEXT)
    return True


def groups_relevant(title: str, groups: list[list[str]], entity: str = "", ticker: str = "") -> bool:
    if groups and not all(any(has_phrase(title, term) for term in group) for group in groups):
        return False
    # A/C/D theme searches need not mention the theme's exact editorial label.
    if ticker and not company_in_title(title, entity, ticker):
        return False
    return True


def event_relevant(title: str, event: dict) -> bool:
    """Require the named subject AND actual event specificity (not just company)."""
    entity = str(event.get("entity") or "")
    ticker = str(event.get("ticker") or "")
    entity_type = str(event.get("entity_type") or "").lower()
    terms = [str(t).strip() for t in (event.get("youtube_event_terms") or []) if str(t).strip()]
    is_company = bool(ticker) or entity_type in {"company", "private_company", "foreign_company"}
    if is_company and not company_in_title(title, entity, ticker):
        return False
    if not terms:
        # A broad company search is not evidence of a SPECIFIC news event.
        return False

    aliases = (*entity_aliases(entity, ticker), normalize(ticker))
    meaningful = [
        t for t in terms
        if not any(normalize(t) == a for a in aliases if a)
    ]
    if not meaningful:
        return False

    specific = [t for t in meaningful if normalize(t) not in GENERIC_EVENT_TERMS]
    generic = [t for t in meaningful if normalize(t) in GENERIC_EVENT_TERMS]
    def matched(term: str) -> bool:
        return any_phrase(title, EVENT_SYNONYMS.get(normalize(term), (term,)))

    if specific:
        # Proper names / product models / unique catalysts are the strongest proof.
        if not any(matched(term) for term in specific):
            return False
        if not is_company:
            # On a macro/theme row, require more than an incidental named mention.
            return sum(bool(matched(t)) for t in meaningful) >= 2
        return True
    # If everything is generic, do not accept company-only coverage just
    # because it contains one word such as "earnings" or "power".
    return sum(bool(matched(t)) for t in generic) >= 2
