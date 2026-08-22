# youtube-trends-scanner

A hybrid, entity-focused topic radar for a Chinese-language investing channel.

## What it does

The scanner uses two discovery layers, then collapses long-tail queries into unique stocks/companies/assets:

1. **Broad-net layer:** fetches Google Trending RSS across several relevant markets and cheaply filters for finance/investing topics using the trend title plus related news headlines.
2. **YouTube layer:** uses Google Trends **YouTube Search** (`gprop="youtube"`) with **Worldwide** geography to discover Rising and Top related searches from curated finance anchors.
3. Merges both pools and filters creator/channel names plus known low-value queries.
4. Maps related searches to canonical entities. For example, `台積電 亞利桑那州廠`, `台積電 工安 意外`, `TSM`, and `台積電 股票` all count as one **TSMC** entity.
5. Keeps only the strongest discovered query for each entity before expensive validation.
6. Runs exact Google Trends benchmarks and YouTube Data API checks only on the final unique entities.
7. Produces `output/latest.md`, `output/latest.csv`, and `output/latest.json` with clean canonical entity names.

The broad Google Trending layer is used for discovery. The final Opportunity Score is still driven by YouTube Search Trends plus recent YouTube competition/performance data.

## Why entity-focused

A topic can generate many highly similar searches. Without entity deduplication, one company such as TSMC can occupy a large part of the final ranking with variants about factories, accidents, employees, stock price, and news.

The scanner now searches broadly first, then gives each stock/company/asset only **one final slot**. This preserves discovery coverage while making the final list much more diverse and useful for choosing videos.

## Default scan

- Worldwide Chinese YouTube Search validation
- 5 Google Trends YouTube discovery anchors
- Google Trending RSS broad scan: `US, CA, TW, HK, SG`
- Broad Trending lookback: 48 hours
- Broad Trending feeds fetched in parallel
- Wide cheap preselection before entity deduplication
- One final row per stock/company/asset entity
- **20 final unique entities**
- 3 exact YouTube Trends benchmark groups (up to 12 entities)
- 7-day YouTube lookback
- 12-hour YouTube metrics cache for repeated manual runs
- Up to 48-hour stale-cache fallback if YouTube search quota is exhausted
- Workflow timeout: 20 minutes

## Candidate priority

The hybrid discovery roughly prioritizes:

1. Found in both Google Trending and YouTube Rising
2. YouTube Rising
3. Broad Google Trending finance candidates
4. YouTube Top related searches
5. Curated seeds

After that ranking, queries are collapsed by entity. Only the strongest representative query for TSMC, Apple, NVIDIA, Micron, Bitcoin, etc. advances to the expensive checks.

The final report displays the clean entity name, while the strongest underlying long-tail query is still used internally for scoring.

## GitHub Actions

Manual run:

`Actions → YouTube Trend Scan → Run workflow`

Automatic run:

- once per day at **12:00 UTC**
- **20:00 Taiwan**
- **08:00 Toronto during EDT / 07:00 during EST**

The scheduled run defaults to **20 unique entities** and a 7-day YouTube Search Trends window.

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

Repeated runs reuse cached YouTube metrics when possible, which avoids spending another expensive YouTube search call for the same recent query. If a deep check has no live or cached YouTube data, its score is forced to zero rather than allowing a Trends-only proxy to rank above fully checked entities.

## Tune the scan

- `creator_blocklist.txt` — creator/channel names and explicit low-value queries to exclude
- `keywords.json` — discovery anchors and curated seed queries
- `entity_cached.py` — canonical entity aliases used to merge query variants

Environment variables:

- `TOP_N` — final unique entity count, default `20`
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
- `YOUTUBE_CACHE_TTL_HOURS` — fresh YouTube-metrics cache window, default `12`
- `YOUTUBE_STALE_FALLBACK_HOURS` — stale cache allowed after quota failure, default `48`
- `YOUTUBE_API_KEY` — optional YouTube Data API v3 key

## Local run

```bash
pip install -r requirements.txt
python entity_cached.py
```

`scan.py` remains the base scanner, `hybrid_scan.py` adds broad discovery, `hybrid_cached.py` adds YouTube metrics caching, and `entity_cached.py` adds entity deduplication plus final-report cleanup.
