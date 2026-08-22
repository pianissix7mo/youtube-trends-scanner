#!/usr/bin/env python3
"""Create a compact JSONL view of raw trend candidates for ChatGPT review."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def compact_signal(signal: dict[str, Any]) -> str:
    region = signal.get("region") or "?"
    source = signal.get("source") or "?"
    text = signal.get("signal") or ""
    anchor = signal.get("anchor")
    rank = signal.get("rank")
    parts = [str(region), str(source)]
    if text:
        parts.append(str(text))
    if anchor:
        parts.append(f"via={anchor}")
    if rank is not None:
        parts.append(f"rank={rank}")
    return ":".join(parts)


def main() -> None:
    src = DATA / "raw_candidates.json"
    payload = json.loads(src.read_text(encoding="utf-8"))
    rows = payload.get("candidates") or []
    out = DATA / "raw_review.jsonl"

    lines: list[str] = []
    for i, row in enumerate(rows, 1):
        signals = sorted(
            row.get("signals") or [],
            key=lambda x: float(x.get("strength") or 0),
            reverse=True,
        )[:4]
        compact = {
            "i": i,
            "q": row.get("query"),
            "r": row.get("regions") or [],
            "p": row.get("raw_priority"),
            "s": [compact_signal(x) for x in signals],
            "n": (row.get("news_titles") or [])[:4],
        }
        lines.append(json.dumps(compact, ensure_ascii=False, separators=(",", ":")))

    out.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    print(f"[done] wrote {len(lines)} review lines to {out}")


if __name__ == "__main__":
    main()
