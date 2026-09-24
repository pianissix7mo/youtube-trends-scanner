# YouTube Entity Enrichment

Generated: **2026-09-24T11:38:29.042089+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | CoreWeave | crwv earnings call | 2/11 | 18.2% | 19 | 19 | 0.0% | 100.0% | ok_low_relevance |
| 2 | Yageo | 國巨 股票 | 15/50 | 30.0% | 1725 | 568 | 33.3% | 20.0% | ok |
| 3 | Costco | costco earnings | 45/50 | 90.0% | 18 | 17 | 20.0% | 70.0% | ok |
| 4 | Tesla | tsla earnings call | 29/50 | 58.0% | 872 | 20 | 13.3% | 20.0% | ok |
| 5 | Meta Muse AI | meta muse ai | 40/50 | 80.0% | 56 | 38 | 7.1% | 10.0% | ok |
| 6 | Cannabis stocks | cannabis stocks | 7/50 | 14.0% | 2638 | 43 | 0.0% | 42.9% | ok_low_relevance |
| 7 | AUO | 友達 股票 | 44/50 | 88.0% | 7682 | 4333 | 58.3% | 10.0% | ok |
| 8 | TSMC | taiwan semiconductor stock | 18/50 | 36.0% | 2538 | 6613 | 100.0% | 30.0% | ok |
| 9 | Super Micro Computer | smci earnings call | 4/8 | 50.0% | 38 | 38 | 0.0% | 100.0% | ok |
| 10 | Semiconductor stocks | semiconductor stocks | 12/50 | 24.0% | 62 | 52 | 20.0% | 80.0% | ok_low_relevance |
| 11 | Micron Technology | micron earnings | 44/50 | 88.0% | 182 | 82 | 34.3% | 70.0% | ok |
| 12 | ON Semiconductor | on semiconductor | 6/50 | 12.0% | 1180 | 118 | 0.0% | 33.3% | ok_low_relevance |
| 13 | AI glasses | ai 眼鏡 | 17/50 | 34.0% | 11816 | 13028 | 83.3% | 30.0% | ok |
| 14 | Amazon | amzn earnings call | 8/50 | 16.0% | 360 | 171 | 28.6% | 87.5% | ok_low_relevance |
| 15 | Intel | intc earnings call | 6/14 | 42.9% | 5 | 5 | 16.7% | 100.0% | ok |
| 16 | NVIDIA | nvda earnings call | 8/20 | 40.0% | 11 | 11 | 12.5% | 100.0% | ok |
| 17 | Trump AI policy | trump ai | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 18 | Navitas Semiconductor | navitas semiconductor stock | 10/16 | 62.5% | 31 | 31 | 0.0% | 100.0% | ok |
| 19 | Meta Platforms | meta earnings | 48/50 | 96.0% | 4067 | 356 | 36.8% | 0.0% | ok |
| 20 | AMD | amd earnings call | 15/50 | 30.0% | 17 | 17 | 30.8% | 90.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### CoreWeave — ok_low_relevance
Relevance groups: `[["CRWV", "CoreWeave"]]`
- Rejected: Nebius Just Became a 10-Bagger — Here's What's Next
- Rejected: AI Just Got 60% Cheaper. So Why Did The Chips Get More Expensive?
- Rejected: He Lost $35 Billion In One Morning. He's Back.
- Rejected: 62 Companies Just Declared a Sale! (Sep 22, 2026)
- Rejected: Unusual Whales: How to Tell Good Options Flow From Bad Flow

### Cannabis stocks — ok_low_relevance
Relevance groups: `[["cannabis stocks", "marijuana stocks"]]`
- Rejected: Cannabis Clemency Progress, and the Work Still Ahead | TTB Presented by Flowhub
- Rejected: AMC IS MOVING AGAIN 🚨 Market Talk LIVE | MSOS, Copper & More
- Rejected: Cannabis Goes Corporate: Who Wins If Washington Legalizes? | The Money Path LIVE
- Rejected: “They’re circling.”
- Rejected: 475% Short Squeeze in 30 Minutes

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor stocks", "chip stocks"]]`
- Rejected: Is Western Digital an Undervalued Semiconductor Stock to Buy Right Now? | WDC STock Analysis
- Rejected: Agentic AI Just Changed the Memory Trade
- Rejected: TSM Taiwan Semiconductor Stock: Thursday Predicted Opening Price (Ahead of A14 traction) - 5 Signals
- Rejected: MICRON STOCK EXPLOSION: MU’S AI MEMORY BOOM COULD SEND IT TO $1,500! 🚀
- Rejected: MU Stock: SEPTEMBER 30 COULD CHANGE EVERYTHING | Micron

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: Semiconductor Stocks Explode as Oil and Yields Fall
- Rejected: Is Western Digital an Undervalued Semiconductor Stock to Buy Right Now? | WDC STock Analysis
- Rejected: Semiconductor Stocks BREAKOUT! Time To BUY, or WAIT?
- Rejected: How are Semiconductor Chips made? The complete story from sand to 2nm chip
- Rejected: India’s Chip Dream Is Getting Real. But Is The Semiconductor Boom Creating A New Security Threat?

### Amazon — ok_low_relevance
Relevance groups: `[["Amazon", "AMZN"]]`
- Rejected: US Unveils Truce Extension, Trump Greets Xi on Tarmac in Rare Protocol Shift
- Rejected: How To Turn 1 Self-Published Book Into 7 Income Streams
- Rejected: Rates, Oil & Big Tech: Where the Value Is Hiding Now | Value Options Letter
- Rejected: Xi Arrives in US for High-Stakes Summit With Trump
- Rejected: Target Stock Is Skyrocketing After Boycott

### Trump AI policy — ok_no_relevant_videos
Relevance groups: `[["Trump AI", "AI policy"]]`
- Rejected: Trump may bail out AI. You'll pay for it.
- Rejected: Apparently, artificial intelligence needs a rebrand. #shorts
- Rejected: Trump wants to “cherish” and “watch over" AI? He didn’t even do that for his kids! #DailyShow #Trump
- Rejected: Responding to President Trump's "Full Steam Ahead" Approach to AI
- Rejected: First lady on "Fostering the Future Together" initiative

