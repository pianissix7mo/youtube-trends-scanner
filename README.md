# youtube-trends-scanner

A small YouTube topic radar for a Chinese-language US-stock channel.

## What it does

1. Uses Google Trends **YouTube Search** (`gprop="youtube"`) to discover rising related searches.
2. Scores English and Chinese keyword tracks separately, using a shared anchor inside each track so Trends values are comparable.
3. Optionally uses YouTube Data API v3 to estimate recent content supply and sampled video performance.
4. Produces `output/latest.md`, `output/latest.csv`, and `output/latest.json`.

The current Opportunity Score combines Google Trends demand/momentum with recent YouTube supply, median views/day, and a small-channel success signal. It is a ranking heuristic, not an estimate of absolute search volume.

## Run in GitHub Actions

Go to **Actions → YouTube Trend Scan → Run workflow**.

The workflow works without a YouTube API key, but then it only reports Google Trends demand signals.

### Add YouTube Data API

Create a YouTube Data API v3 key in Google Cloud, then add it to this repository as:

`Settings → Secrets and variables → Actions → New repository secret`

Name:

`YOUTUBE_API_KEY`

After that, the same workflow automatically adds:

- estimated number of videos published in the last 7 days for each query
- median views and median views/day from the sampled relevant videos
- share of sampled videos where a channel under 50k subscribers still reached at least 1k views
- combined Opportunity Score

## Tune keywords

Edit `keywords.json`. English and Chinese are intentionally separate because Google Trends values are relative, and Chinese YouTube search behavior is much smaller/different from English search behavior.

Environment variables:

- `TOP_N` — final result count, default `20`
- `TRENDS_TIMEFRAME` — default `now 7-d`
- `MAX_CANDIDATES_PER_LANGUAGE` — limits Google Trends browser calls, default `16`
- `YOUTUBE_API_KEY` — optional YouTube Data API v3 key

## Local run

```bash
pip install -r requirements.txt
python scan.py
```
