# youtube-trends-scanner

A three-stage topic radar for a Chinese-language U.S.-stock / investing YouTube channel.

## Core idea

**Python gathers data; ChatGPT makes editorial judgements; Python measures YouTube competition; ChatGPT makes the final recommendation.**

The active daily pipeline deliberately avoids trying to encode every editorial rule into Python. Old blacklist / alias / scoring logic is kept only as legacy rollback code and is no longer the scheduled main path.

## Daily pipeline

### 1. 05:00 Toronto — collect raw trends with Python

GitHub Actions workflow: **Collect Raw Trends**

`collect_trends.py` gathers broad signals from three near-equal discovery markets:

- United States
- Canada
- Taiwan

Taiwan may be treated as only slightly more important, but it must not dominate simply because the current channel audience is Taiwan-heavy.

The collector combines:

- Google Trending RSS, 48-hour lookback
- Google Trends property = **YouTube Search**
- Rising and Top related searches from broad anchors in each market

The collector intentionally performs almost no editorial filtering. It can keep entertainment, sports, generic terms, creators, companies, crypto, macro, and other noise because ChatGPT reviews the pool later.

The default cap is **1,000 raw candidates**.

Outputs:

- `data/raw_candidates.json` — full machine-readable evidence
- `data/raw_review.jsonl` — compact one-candidate-per-line review file for ChatGPT

The workflow commits these files back to the repository.

### 2. 05:30 Toronto — ChatGPT selects up to 20 entities

A ChatGPT Scheduled Task reads all of `data/raw_review.jsonl` in chunks and applies editorial judgement.

Selection principles:

- U.S., Canada, and Taiwan are near-equal discovery markets
- prioritize topics relevant to U.S. equities / investors
- a Taiwan, Canadian, Asian, or other non-U.S. company is valid when it can materially affect U.S.-listed stocks, technology supply chains, market sentiment, macro expectations, or investor attention
- one slot per company / asset / entity
- merge long-tail searches about the same entity
- remove sports, entertainment, creator/channel names, generic evergreen terms, generic how-to searches, and other low-value noise
- macro / policy / crypto topics are allowed when materially market-relevant

Examples:

- `台積電 亞利桑那州廠`, `TSMC Arizona`, `台積電 工安` → one **TSMC** entity
- `BTC`, `Bitcoin`, `比特幣暴漲` → one **Bitcoin** entity
- a non-U.S. supplier can still qualify if its news materially affects NVIDIA, Apple, memory, semiconductors, AI infrastructure, or other U.S.-market themes

ChatGPT writes:

- `data/selected_entities.json`

Each selected row contains a canonical entity, entity type, one concise YouTube query, source regions, selection reason, and trend evidence.

### 3. Automatic — YouTube Data API enrichment

GitHub Actions workflow: **Enrich Selected Entities**

A commit to `data/selected_entities.json` automatically triggers `youtube_enrich.py`.

Only the selected **up to 20 entities** use the expensive YouTube search call.

For each entity the script measures:

- approximate number of relevant videos published in the last 7 days
- median views
- median views/day
- small-channel hit rate
- median sampled channel subscribers
- sample high-velocity videos

The Python stage does **not** compute a final editorial Opportunity Score.

Outputs:

- `output/latest.json`
- `output/latest.md`

The workflow commits the latest output back to the repository and also uploads it as an artifact.

### 4. 06:00 Toronto — ChatGPT final ranking + email

A second ChatGPT Scheduled Task reads the fresh enrichment output and performs the final review.

It combines:

- trend strength / Rising / Breakout evidence
- freshness and catalyst quality
- relevance to U.S. investors
- 7-day YouTube content supply
- median views/day
- small-channel hit rate
- whether a newer/smaller channel has a realistic content angle

The email contains:

- **今天最值得做 Top 3**
- full ranked list of up to 20 entities
- a model judgement score out of 10
- catalyst / trend explanation
- YouTube competition metrics
- one concrete Chinese video angle for each entity

## Geography philosophy

Do **not** use the channel's current audience percentages as literal weights.

The current audience may be Taiwan-heavy because the channel is still young. The intended long-run audience is more balanced across Taiwan, the United States, and Canada.

Therefore the system uses the three regions as near-equal discovery markets. A useful mental model is roughly:

- Taiwan: ~36%
- United States: ~32%
- Canada: ~32%

These are not hard mathematical weights. Model judgement should still preserve an important U.S.-first story even when Taiwan search interest has not caught up yet.

## GitHub Actions

### Collect Raw Trends

Automatic run: **05:00 America/Toronto every day**, DST-safe.

Manual run is also available from GitHub Actions.

Inputs:

- `timeframe` — default `now 7-d`
- `raw_limit` — default `1000`

### Enrich Selected Entities

Runs automatically when ChatGPT writes `data/selected_entities.json`.

It can also be launched manually.

## YouTube API

Repository secret required:

`YOUTUBE_API_KEY`

The enrichment stage uses only one `search.list` query per selected entity, so a normal daily run uses at most about 20 expensive search calls rather than spending quota on the full raw candidate pool.

A 12-hour fresh cache and 48-hour stale fallback are supported for repeated tests or quota failures.

## Active files

- `collect_trends.py` — broad US/CA/TW trend collection
- `make_review_file.py` — compact ChatGPT-readable raw view
- `youtube_enrich.py` — YouTube Data API measurement stage
- `.github/workflows/scan.yml` — 05:00 raw collection
- `.github/workflows/enrich.yml` — automatic YouTube enrichment
- `data/raw_candidates.json` — generated raw evidence
- `data/raw_review.jsonl` — generated compact review input
- `data/selected_entities.json` — generated ChatGPT selection
- `output/latest.json` / `output/latest.md` — generated YouTube measurements

## Legacy files

The previous scanner remains in the repository for rollback/reference but is not part of the scheduled main pipeline:

- `scan.py`
- `hybrid_scan.py`
- `hybrid_cached.py`
- `entity_cached.py`
- `creator_blocklist.txt`
- `keywords.json`

## Local usage

Collect raw data:

```bash
pip install -r requirements.txt
python collect_trends.py
python make_review_file.py
```

After `data/selected_entities.json` exists:

```bash
YOUTUBE_API_KEY=... python youtube_enrich.py
```
