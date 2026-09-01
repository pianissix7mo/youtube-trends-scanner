#!/usr/bin/env python3
"""YouTube enrichment for Scanner C (editorial news) and Scanner D (Reddit attention).

Input:  data/selected_external.json
Output: output/latest_c.json / output/latest_c.md
        output/latest_d.json / output/latest_d.md

The selection-stage model supplies up to 10 items for each scanner.
This script reuses Scanner A's YouTube measurement logic so A/C/D are
comparable on the same 3-day small-channel metrics.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import youtube_enrich as base

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "output"
INPUT = DATA / "selected_external.json"
MAX_ITEMS_PER_SCANNER = 10


def failed_metrics(relevance_groups: list[list[str]], error: str) -> dict[str, Any]:
    return {
        "recent_video_estimate": None,
        "raw_recent_video_estimate": None,
        "raw_sample_size": 0,
        "relevant_sample_size": None,
        "relevance_ratio": None,
        "median_views": None,
        "median_views_per_day": None,
        "small_channel_sample_size": None,
        "small_channel_median_views_per_day": None,
        "small_channel_hit_rate": None,
        "top10_small_channel_share": None,
        "top10_small_channel_count": None,
        "top10_known_channels": None,
        "median_channel_subscribers": None,
        "small_channel_max_subscribers": base.SMALL_CHANNEL_MAX_SUBS,
        "small_channel_hit_vpd_threshold": base.SMALL_CHANNEL_HIT_VPD,
        "relevance_filter_applied": bool(relevance_groups),
        "rejected_sample_titles": [],
        "status": "api_failed_no_cache",
        "api_error": error,
    }


def enrich_items(
    items: list[dict[str, Any]],
    cache: dict[str, Any],
    api_key: str,
) -> tuple[list[dict[str, Any]], int]:
    enriched: list[dict[str, Any]] = []
    search_calls = 0

    for i, item in enumerate(items[:MAX_ITEMS_PER_SCANNER], 1):
        row = dict(item)
        entity = str(row.get("entity") or row.get("company") or row.get("ticker") or "").strip()
        query = str(row.get("youtube_query") or entity).strip()
        relevance_groups = base.normalize_relevance_groups(row.get("relevance_groups"))

        if not entity or not query:
            print(f"[skip] malformed external row {i}: {item}")
            continue

        row["entity"] = entity
        row["youtube_query"] = query
        row["relevance_groups"] = relevance_groups

        metrics = base.cached_metrics(cache, query, relevance_groups, base.CACHE_TTL_HOURS)
        if metrics is not None:
            metrics = dict(metrics)
            metrics["cache_status"] = "fresh"
        else:
            try:
                metrics = base.fetch_metrics(query, relevance_groups, api_key)
                search_calls += 1
                cache[base.cache_key(query, relevance_groups)] = {
                    "cached_at_utc": datetime.now(timezone.utc).isoformat(),
                    "metrics": metrics,
                }
            except Exception as exc:
                stale = base.cached_metrics(
                    cache, query, relevance_groups, base.STALE_FALLBACK_HOURS
                )
                if stale is not None:
                    metrics = dict(stale)
                    metrics["cache_status"] = "stale_fallback"
                    metrics["api_error"] = str(exc)
                else:
                    metrics = failed_metrics(relevance_groups, str(exc))

        row["youtube_metrics"] = metrics
        enriched.append(row)

    return enriched, search_calls


def write_markdown(payload: dict[str, Any], letter: str) -> None:
    title = (
        "Scanner C — Editorial News + YouTube Enrichment"
        if letter == "C"
        else "Scanner D — Reddit Attention + YouTube Enrichment"
    )
    lines = [
        f"# {title}",
        "",
        f"Generated: **{payload['generated_at_utc']}**",
        f"Selection generated: **{payload.get('selection_generated_at_utc') or '—'}**",
        f"YouTube search calls used: **{payload.get('youtube_search_calls_used', 0)}**",
        "",
        "| # | Entity | Ticker | YouTube query | Relevant sample | Small-channel median VPD | Small-channel hit | Top-10 small share | Status |",
        "|---:|---|---|---|---:|---:|---:|---:|---|",
    ]

    for i, row in enumerate(payload.get("items") or [], 1):
        m = row.get("youtube_metrics") or {}
        lines.append(
            f"| {i} | {row.get('entity','')} | {row.get('ticker') or '—'} | "
            f"{row.get('youtube_query','')} | "
            f"{m.get('relevant_sample_size','—')}/{m.get('raw_sample_size','—')} | "
            f"{m.get('small_channel_median_views_per_day','—')} | "
            f"{m.get('small_channel_hit_rate','—')}% | "
            f"{m.get('top10_small_channel_share','—')}% | {m.get('status','—')} |"
        )

    lines.extend([
        "",
        f"- Window: last {base.LOOKBACK_DAYS} days.",
        f"- Small channel: fewer than {base.SMALL_CHANNEL_MAX_SUBS:,} subscribers.",
        f"- Small-channel hit: at least {base.SMALL_CHANNEL_HIT_VPD:,} views/day.",
        "- This is measurement only; the final model ranking happens later across A+B+C+D.",
    ])
    (OUT / f"latest_{letter.lower()}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_payload(
    letter: str,
    selection_generated_at_utc: Any,
    source: Any,
    notes: Any,
    items: list[dict[str, Any]],
    search_calls: int,
) -> None:
    payload = {
        "scanner": letter,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "selection_generated_at_utc": selection_generated_at_utc,
        "source": source,
        "selection_notes": notes,
        "lookback_days": base.LOOKBACK_DAYS,
        "small_channel_max_subscribers": base.SMALL_CHANNEL_MAX_SUBS,
        "small_channel_hit_vpd_threshold": base.SMALL_CHANNEL_HIT_VPD,
        "youtube_search_calls_used": search_calls,
        "items": items,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"latest_{letter.lower()}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(payload, letter)


def main() -> None:
    if not INPUT.exists():
        raise RuntimeError("data/selected_external.json does not exist")

    selected = json.loads(INPUT.read_text(encoding="utf-8"))
    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("YOUTUBE_API_KEY secret is missing")

    cache = base.load_cache()
    selection_generated = selected.get("generated_at_utc")

    total_items = 0
    total_calls = 0
    for letter, key in (("C", "scanner_c"), ("D", "scanner_d")):
        section = selected.get(key) or {}
        items = section.get("items") or []
        if not isinstance(items, list):
            raise RuntimeError(f"{key}.items must be a list")
        items = items[:MAX_ITEMS_PER_SCANNER]
        total_items += len(items)

        enriched, calls = enrich_items(items, cache, api_key)
        total_calls += calls
        write_payload(
            letter=letter,
            selection_generated_at_utc=selection_generated,
            source=section.get("source"),
            notes=section.get("notes"),
            items=enriched,
            search_calls=calls,
        )

    if total_items == 0:
        raise RuntimeError("selected_external.json contains no Scanner C or D items")

    base.save_cache(cache)
    print(
        f"[done] external enrichment: {total_items} items, "
        f"{total_calls} fresh YouTube search calls"
    )


if __name__ == "__main__":
    main()
