# YouTube Entity Enrichment

Generated: **2026-09-30T11:38:28.071977+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | OpenAI DevDay / Dots | OpenAI DevDay Dots GPT-6.1 | 37/50 | 74.0% | 4598 | 1784 | 55.6% | 30.0% | ok |
| 2 | Micron Technology | Micron MU earnings | 34/50 | 68.0% | 185 | 60 | 28.0% | 50.0% | ok |
| 3 | Robinhood Markets | Robinhood HOOD stock | 30/50 | 60.0% | 34 | 27 | 11.5% | 60.0% | ok |
| 4 | VanEck Semiconductor ETF | VanEck Semiconductor ETF SMH | 1/6 | 16.7% | 10 | 10 | 0.0% | 100.0% | ok_low_relevance |
| 5 | ON Semiconductor | ON Semiconductor onsemi ON stock | 2/4 | 50.0% | 4 | 4 | 0.0% | 100.0% | ok |
| 6 | Valens Semiconductor | Valens Semiconductor VLN | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 7 | Magnachip Semiconductor | Magnachip Semiconductor MX | 2/2 | 100.0% | 17 | 17 | 0.0% | 100.0% | ok |
| 8 | Navitas Semiconductor | Navitas Semiconductor NVTS | 18/20 | 90.0% | 122 | 102 | 0.0% | 70.0% | ok |
| 9 | NVIDIA | NVIDIA NVDA earnings | 44/50 | 88.0% | 93 | 41 | 21.2% | 50.0% | ok |
| 10 | TSMC | TSMC TSM semiconductor | 37/50 | 74.0% | 718 | 207 | 22.7% | 10.0% | ok |
| 11 | Semiconductor packaging | semiconductor advanced packaging AI chips | 3/50 | 6.0% | 14 | 14 | 33.3% | 100.0% | ok_low_relevance |
| 12 | AI agents | AI agents agentic AI | 40/50 | 80.0% | 110 | 76 | 6.5% | 40.0% | ok |
| 13 | Trump AI policy | Trump AI policy tech stocks | 19/50 | 38.0% | 15515 | 0 | 0.0% | 0.0% | ok |
| 14 | Bill Gates / AI | Bill Gates AI Microsoft | 39/50 | 78.0% | 636 | 12 | 0.0% | 0.0% | ok |
| 15 | AI semiconductor stocks | AI semiconductor stocks 2026 | 15/50 | 30.0% | 50 | 28 | 15.4% | 80.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### VanEck Semiconductor ETF — ok_low_relevance
Relevance groups: `[["VanEck Semiconductor ETF", "SMH"]]`
- Rejected: 8 ETFs I’d Actually Pay Attention to in 2026
- Rejected: Want to profit from the AI boom? #dividendinvesting
- Rejected: Will the Nasdaq Head to a New High from Here?
- Rejected: 엔비디아는 내렸는데 반도체 ETF는 상승, 무엇이 달랐나? #엔비디아 #반도체ETF
- Rejected: Focus #03 | Taiwan: A Ilha que Pode Parar a Economia Mundial

### Semiconductor packaging — ok_low_relevance
Relevance groups: `[["semiconductor packaging", "advanced packaging", "CoWoS", "chip packaging", "先進封裝", "先进封装"]]`
- Rejected: AI Chips Are Getting Too Big for ASML’s Most Advanced Machine
- Rejected: ASML monopoly on advanced chipmaking equipment
- Rejected: Chip War 2026: The Geopolitical Chokepoints Weaponizing Advanced Silicon
- Rejected: The Trillion-Dollar Semiconductor Race: Who Will Build the Chips of the Future?
- Rejected: TSMC’s Chiayi Move Signals a New AI Bottleneck #TSMC #AIInfrastructure #Semiconductors

