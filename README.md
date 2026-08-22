# youtube-trends-scanner

A hybrid topic radar for a Chinese-language investing channel.

## What it does

The scanner now uses two discovery layers and merges them into one candidate pool:

1. **Broad-net layer:** fetches Google Trending RSS across several relevant markets and cheaply filters for finance/investing topics using the trend title plus its related news headlines.
2. **YouTube layer:** uses Google Trends **YouTube Search** (`gprop="youtube"`) with **Worldwide** geography to discover Rising and Top related searches from curated finance anchors.
3. Merges and deduplicates both pools.
4. Gives priority to terms found by both methods, then strong YouTube Rising terms, then a capped number of broad Trending candidates.
5. Keeps the first exact Trends benchmark groups diverse so broad-net ideas also get real YouTube Search validation.
6. Uses YouTube Data API v3 for every final candidate to estimate recent content supply and sampled performance.
7. Produces `output/latest.md`, `output/latest.csv`, and `output/latest.json`.

The Google Trending layer is used only for **discovery**, not as a substitute for YouTube demand. A broad trend gets into the funnel, but the final Opportunity Score is still driven by the existing YouTube Search Trends and YouTube performance logic.

## Why hybrid

The original anchor-based method is precise but can miss an unexpected ticker, company, macro event, policy story, crypto move, or sector that is not closely related to the configured anchors.

The hybrid method adds a cheap large-net scan first, then sends only a limited number of candidates into the expensive validation steps. This improves coverage without making the workflow dramatically slower.

## Default scan

- Worldwide Chinese YouTube Search validation
- 5 Google Trends YouTube discovery anchors
- Google Trending RSS broad scan: `US, CA, TW, HK, SG`
- Broad Trending lookback: 48 hours
- Broad Trending feeds fetched in parallel
- Up to 16 broad-only candidates admitted to the final preselection pool
- 3 exact YouTube Trends benchmark groups (up to 12 keywords)
- 40 final keywords sent through YouTube Data API
- 7-day YouTube lookback
- Workflow timeout: 20 minutes

The seed list in `keywords.json` contains broad market, macro, US tech, semiconductors, AI, crypto, and Taiwan-relevant terms in both Simplified and Traditional Chinese, plus commonly searched ticker symbols.

## Candidate priority

The hybrid preselection roughly follows:

1. Found in both Google Trending and YouTube Rising
2. YouTube Rising
3. Broad Google Trending finance candidates
4. YouTube Top related searches
5. Curated seeds

The first benchmark slots deliberately mix strong YouTube Rising terms with broad Trending candidates so the latter are tested against real YouTube Search demand instead of being trusted just because they are hot on Google Search.

In the report, `source=trending` means the term entered through the broad Google Trending layer. A broad-only candidate may show a signal such as `GTrend 100,000+ [US,CA]` in the Rising column; that label is informational and does **not** count as YouTube Rising momentum.

## GitHub Actions

Manual run:

`Actions → YouTube Trend Scan → Run workflow`

Automatic run:

- once per day at **12:00 UTC**
- **20:00 Taiwan**
- **08:00 Toronto during EDT / 07:00 during EST**

The scheduled run defaults to 40 final keywords and a 7-day YouTube Search Trends window.

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
- `TRENDS_TIMEFRAME` — YouTube Search Trends window, default `now 7-d`
- `DISCOVERY_ANCHORS` — default `5`
- `TREND_BENCHMARK_GROUPS` — default `3`; each group measures up to 4 candidates against the shared anchor
- `TRENDS_MAX_ATTEMPTS` — default `1`
- `TRENDS_RETRY_WAIT` — default `5`
- `TRENDING_RSS_GEOS` — broad-net regions, default `US,CA,TW,HK,SG`
- `TRENDING_RSS_HOURS` — broad-net lookback, default `48`
- `TRENDING_RSS_TIMEOUT` — per-feed timeout, default `10`
- `TRENDING_RSS_PER_GEO` — maximum RSS rows inspected per region, default `50`
- `TRENDING_PRESELECT_LIMIT` — maximum broad-only candidates admitted before Top/seeds, default `16`
- `YOUTUBE_API_KEY` — optional YouTube Data API v3 key

## Local run

```bash
pip install -r requirements.txt
python hybrid_scan.py
```

The original `scan.py` remains in the repository as the non-hybrid base scanner and is imported by `hybrid_scan.py`.
