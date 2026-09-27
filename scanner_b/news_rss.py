#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import urlparse

import requests

GOOGLE_NEWS_RSS = "https://news.google.com/rss/search"
GOOGLE_NEWS_MAX_ATTEMPTS = max(1, int(os.getenv("GOOGLE_NEWS_MAX_ATTEMPTS", "3")))
GOOGLE_NEWS_RETRY_BASE_SECONDS = max(0.0, float(os.getenv("GOOGLE_NEWS_RETRY_BASE_SECONDS", "2")))
GOOGLE_NEWS_RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def _retry_delay_seconds(response: requests.Response | None, attempt: int) -> float:
    if response is not None:
        retry_after = str(response.headers.get("Retry-After") or "").strip()
        try:
            return max(0.0, float(retry_after))
        except ValueError:
            pass
    return GOOGLE_NEWS_RETRY_BASE_SECONDS * (2 ** max(0, attempt - 1))


def _get_google_news_with_retry(
    session: requests.Session,
    *,
    params: dict[str, str],
    timeout: int,
) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(1, GOOGLE_NEWS_MAX_ATTEMPTS + 1):
        response: requests.Response | None = None
        try:
            response = session.get(
                GOOGLE_NEWS_RSS,
                params=params,
                timeout=timeout,
            )
            if response.status_code not in GOOGLE_NEWS_RETRYABLE_STATUS:
                response.raise_for_status()
                return response
            if attempt >= GOOGLE_NEWS_MAX_ATTEMPTS:
                response.raise_for_status()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as exc:
            last_error = exc
            status = response.status_code if response is not None else None
            retryable = status in GOOGLE_NEWS_RETRYABLE_STATUS or isinstance(
                exc, (requests.Timeout, requests.ConnectionError)
            )
            if not retryable or attempt >= GOOGLE_NEWS_MAX_ATTEMPTS:
                raise
            delay = _retry_delay_seconds(response, attempt)
            print(
                f"Google News RSS transient failure"
                f"{f' HTTP {status}' if status else ''}; "
                f"retry {attempt}/{GOOGLE_NEWS_MAX_ATTEMPTS - 1} after {delay:.1f}s"
            )
            if delay:
                time.sleep(delay)

    if last_error is not None:
        raise last_error
    raise RuntimeError("Google News RSS request failed without an error")


def parse_pubdate(value: str) -> datetime:
    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return datetime.now(timezone.utc)


def clean_headline(title: str, source_name: str) -> str:
    title = str(title or "").strip()
    source_name = str(source_name or "").strip()
    if source_name:
        suffix = f" - {source_name}"
        if title.endswith(suffix):
            return title[: -len(suffix)].strip()
    return title


def story_key(title: str) -> str:
    """Normalize a headline so syndicated copies count as one story.

    Google News often returns the same wire/local-copy headline from many
    domains.  Those are useful evidence that a story is spreading, but they are
    not independent information events and should not inflate burst/source
    diversity.  Keep the first copy and collapse obvious title duplicates.
    """
    value = str(title or "").lower().strip()
    value = re.sub(r"\(\s*copy\s*\)$", "", value, flags=re.I)
    value = re.sub(r"\bcopy\b$", "", value, flags=re.I)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def fetch_google_news(
    session: requests.Session,
    query: str,
    when: str = "1d",
    timeout: int = 20,
) -> list[dict[str, Any]]:
    # Google News RSS accepts normal News-search syntax but is less predictable
    # with database-style nested parentheses. Keep the query broad here and let
    # our own entity matching / event clustering do the precision work later.
    q = f"{query} when:{when}".strip()
    r = _get_google_news_with_retry(
        session,
        params={
            "q": q,
            "hl": "en-US",
            "gl": "US",
            "ceid": "US:en",
        },
        timeout=timeout,
    )
    root = ET.fromstring(r.content)

    output: list[dict[str, Any]] = []
    seen_story_keys: set[str] = set()
    for item in root.findall("./channel/item"):
        source_el = item.find("source")
        source_name = (source_el.text or "").strip() if source_el is not None else ""
        source_url = str(source_el.attrib.get("url") or "") if source_el is not None else ""
        title = clean_headline(item.findtext("title", default=""), source_name)
        link = (item.findtext("link", default="") or "").strip()
        guid = (item.findtext("guid", default="") or "").strip()
        published = parse_pubdate(item.findtext("pubDate", default=""))
        domain = urlparse(source_url).netloc.lower().removeprefix("www.") if source_url else ""
        if not title:
            continue

        key = story_key(title)
        if key and key in seen_story_keys:
            continue
        if key:
            seen_story_keys.add(key)

        output.append(
            {
                "title": title,
                "link": link,
                "guid": guid,
                "published_at_utc": published.isoformat(),
                "source_name": source_name,
                "source_url": source_url,
                "domain": domain or re.sub(r"\s+", "-", source_name.lower()),
            }
        )
    return output
