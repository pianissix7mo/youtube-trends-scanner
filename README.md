# youtube-trends-scanner

A YouTube topic radar for a Chinese-language investing channel.

## What it does

1. Uses Google Trends **YouTube Search** (`gprop="youtube"`) with **Worldwide** geography.
2. Searches Chinese, Traditional Chinese, and ticker-symbol queries used by Chinese-speaking investors.
3. Discovers Rising and Top related searches from several Chinese anchors.
4. Uses shared-anchor Google Trends comparisons for a subset of candidates, then YouTube Data API v3 for every final candidate.
5. Produces `output/latest.md`, `output/latest.csv`, and `output/latest.json`.

The Opportunity Score combines Google Trends demand/momentum with recent YouTube content supply, median views/day, and a small-channel success signal. It is a ranking heuristic, not an estimate of absolute search volume.

## Default scan

- Worldwide Chinese YouTube Search
- 5 Google Trends discovery anchors
- 3 exact benchmark groups (up to 12 keywords)
- 40 final keywords sent through YouTube Data API
- 7-day YouTube lookback
- Workflow timeout: 20 minutes

The seed list in `keywords.json` contains broad market, macro, US tech, semiconductors, AI, crypto, and Taiwan-relevant terms in both Simplified and Traditional Chinese, plus commonly searched ticker symbols.

## GitHub Actions

Manual run:

`Actions → YouTube Trend Scan → Run workflow`

Automatic run:

- once per day at **12:00 UTC**
- **20:00 Taiwan**
- **08:00 Toronto during EDT / 07:00 during EST**

The scheduled run defaults to 40 final keywords and a 7-day Google Trends window.

## YouTube Data API

Add the repository secret:

`Settings → Secrets and variables → Actions → New repository secret`

Name:

`YOUTUBE_API_KEY`

With the key enabled, the report adds:

- estimated number of relevant videos published in the last 7 days
- median views and median views/day from up to 50 sampled videos
- share of sampled videos where a channel under 50k subscribers still reached at least 1k views
- combined Opportunity Score

## Tune the scan

Edit `keywords.json` to change discovery anchors or curated seeds.

Environment variables:

- `TOP_N` — final result count, default `40`
- `TRENDS_TIMEFRAME` — default `now 7-d`
- `DISCOVERY_ANCHORS` — default `5`
- `TREND_BENCHMARK_GROUPS` — default `3`; each group measures up to 4 candidates against the shared anchor
- `TRENDS_MAX_ATTEMPTS` — default `1`
- `TRENDS_RETRY_WAIT` — default `5`
- `YOUTUBE_API_KEY` — optional YouTube Data API v3 key

## Local run

```bash
pip install -r requirements.txt
python scan.py
```
