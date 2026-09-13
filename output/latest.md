# YouTube Entity Enrichment

Generated: **2026-09-13T12:06:45.418527+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Oracle | Oracle ORCL earnings AI cloud | 43/50 | 86.0% | 125 | 33 | 6.9% | 10.0% | ok |
| 2 | Adobe | Adobe ADBE earnings AI | 26/50 | 52.0% | 114 | 37 | 5.3% | 30.0% | ok |
| 3 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 4 | Copart | Copart CPRT earnings | 7/24 | 29.2% | 18 | 18 | 0.0% | 85.7% | ok_low_relevance |
| 5 | Hewlett Packard Enterprise | HPE Hewlett Packard Enterprise earnings AI servers | 5/20 | 25.0% | 14 | 14 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Alphabet / Google | Google GOOGL earnings AI | 12/50 | 24.0% | 26 | 17 | 10.0% | 80.0% | ok_low_relevance |
| 7 | Meta Platforms | Meta META earnings AI | 10/50 | 20.0% | 202 | 65 | 0.0% | 70.0% | ok_low_relevance |
| 8 | TSMC | TSMC TSM AI chips semiconductor | 30/50 | 60.0% | 17 | 13 | 3.7% | 70.0% | ok |
| 9 | Anthropic | Anthropic Claude AI chips IPO | 9/27 | 33.3% | 4 | 4 | 0.0% | 100.0% | ok |
| 10 | OpenAI | OpenAI ChatGPT AI infrastructure | 36/50 | 72.0% | 29 | 19 | 9.1% | 70.0% | ok |
| 11 | Apple Siri AI | Apple AAPL Siri AI | 26/50 | 52.0% | 623 | 422 | 25.0% | 50.0% | ok |
| 12 | Semiconductor supply chain | semiconductor supply chain AI chips | 1/50 | 2.0% | 24 | 24 | 0.0% | 100.0% | ok_low_relevance |
| 13 | Tower Semiconductor | Tower Semiconductor TSEM stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 14 | onsemi | onsemi ON semiconductor stock | 3/3 | 100.0% | 14 | 14 | 0.0% | 100.0% | ok |
| 15 | Navitas Semiconductor | Navitas Semiconductor NVTS GaN stock | 0/4 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 16 | Quantum computing stocks | quantum computing stocks IONQ RGTI QBTS QUBT | 9/10 | 90.0% | 8 | 8 | 11.1% | 100.0% | ok |
| 17 | Canadian bank stocks | Canadian bank stocks RY TD BMO BNS CM | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 18 | Pegatron / AI server supply chain | Pegatron AI servers Apple supply chain | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 19 | Strait of Hormuz / oil supply | Strait of Hormuz oil attack Iran markets | 22/50 | 44.0% | 1147 | 452 | 12.5% | 10.0% | ok |
| 20 | Huawei U.S. racketeering trial | Huawei US racketeering trial chips | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Copart — ok_low_relevance
Relevance groups: `[["Copart", "CPRT"], ["earnings", "results", "guidance", "财报"]]`
- Rejected: Copart Stock (CPRT): Is Copart now a Buy?
- Rejected: Copart Acquires ACV in Major Cash Deal: Margins Pressured but Expansion Ahead
- Rejected: CPRT vs META: Which Stock Deserves Your Next Dollar?
- Rejected: Copart Forensic Equity Research: Salvage Market Leadership and Valuation Analysis
- Rejected: Copart (CPRT): 🚗 The $1.9B Takeover & The 19x Value Play

### Hewlett Packard Enterprise — ok_low_relevance
Relevance groups: `[["HPE", "Hewlett Packard Enterprise"], ["earnings", "results", "guidance", "AI", "server", "networking"]]`
- Rejected: HPE Stock Is Back in Focus — Here’s What to Watch This Week
- Rejected: Hewlett Packard (HPE) +12%, NuScale Power (SMR) -16%: Two Five-Year Stories | September 11, 2026
- Rejected: AI Server Stocks Surge as Nuclear Names Tumble | Market Recap Sep. 11
- Rejected: The 60% Cloud Shift: How Enterprise AI Is Minting Billions
- Rejected: Oracle Said $95B. These 3 Stocks Jumped Instead

### Alphabet / Google — ok_low_relevance
Relevance groups: `[["Google", "Alphabet", "GOOGL", "GOOG"], ["earnings", "results", "guidance", "AI", "cloud"]]`
- Rejected: Google Stock Fell After Buffett’s Bet. What Is the Market Seeing?
- Rejected: Nvidia Leads the Day as AI's Power Buildout Takes Center Stage: NVDA's 2 GW Australia AI Push Could…
- Rejected: From NVDA & MSFT to ETN: Names to Benefit Long-Term from AI
- Rejected: Is Apple Making Google And Micron Rich? The Real Stocks Affected!
- Rejected: Nvidia Leads the Day as AI's Power Buildout Takes Center Stage: NVDA's 2 GW Australia AI Push Could…

### Meta Platforms — ok_low_relevance
Relevance groups: `[["Meta"], ["earnings", "results", "AI", "guidance"]]`
- Rejected: Huge News for Meta Stock Investors
- Rejected: Meta Settles for $17.1 Billion - Why Advertisers May Pay the Price
- Rejected: Meta Just Fired 20,000 People to Fund a Bet That Isn't Working
- Rejected: How I Grew My Business From $0 to $200M+ with Meta Ads (Full Playbook)
- Rejected: Gene Munster: $META Muse Signals The End Of "The Algorithm"

### Semiconductor supply chain — ok_low_relevance
Relevance groups: `[["semiconductor supply chain", "semiconductor manufacturing", "chip supply chain", "半導體製程", "半导体制造"]]`
- Rejected: Why Can’t Nvidia Get Enough AI Chips?
- Rejected: Why The U.S. AI Chip Ban on China Just Backfired
- Rejected: Explainer: What To Know About SEMICON Taiwan 2026 | TaiwanPlus News
- Rejected: The Silicon Bottleneck: The Physics and Economics of Global Chip Dependence
- Rejected: SEMICON Taiwan 2026: The Country's Chip Footprint Expanding Abroad | TaiwanPlus News

### Navitas Semiconductor — ok_no_relevant_videos
Relevance groups: `[["Navitas Semiconductor", "Navitas", "NVTS"], ["GaN", "power semiconductor", "power chip"]]`
- Rejected: Navitas (NVTS): The Next Big AI Stock—or Overpriced?
- Rejected: NVTS Stock Before 2027: BUY, HOLD or AVOID? | Navitas Semiconductor Stock Prediction
- Rejected: Navitas Semiconductor Stock: 310% Surge, Live Oak Deal & HUGE AI Opportunity
- Rejected: 别只盯着GPU！这只被严重低估的AI芯片股，正迎来十倍重构点？｜深度拆解第三代半导体黑马 Navitas 的千亿算力逻辑

### Huawei U.S. racketeering trial — ok_no_relevant_videos
Relevance groups: `[["Huawei", "華為", "华为"], ["trial", "racketeering", "lawsuit", "court", "U.S.", "US"]]`
- Rejected: Traído pela ex, ativo Cashback SSS, enriqueço numa noite e caso com a deusa do meu primeiro amor!

