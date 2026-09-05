# YouTube Entity Enrichment

Generated: **2026-09-05T11:34:08.510028+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Broadcom earnings | Broadcom AVGO earnings AI guidance | 23/50 | 46.0% | 754 | 45 | 6.7% | 20.0% | ok |
| 2 | Lululemon earnings | Lululemon LULU earnings outlook | 16/50 | 32.0% | 230 | 175 | 8.3% | 60.0% | ok |
| 3 | Planet Labs earnings | Planet Labs PL earnings | 5/50 | 10.0% | 325 | 76 | 0.0% | 60.0% | ok_low_relevance |
| 4 | VanEck Semiconductor ETF / SMH | SMH VanEck Semiconductor ETF | 3/6 | 50.0% | 17 | 17 | 0.0% | 100.0% | ok |
| 5 | U.S. semiconductor tariffs | US semiconductor tariffs chip stocks | 3/50 | 6.0% | 1262 | 1262 | 100.0% | 33.3% | ok_low_relevance |
| 6 | UiPath earnings | UiPath PATH earnings AI automation | 12/24 | 50.0% | 235 | 184 | 9.1% | 90.0% | ok |
| 7 | Snowflake earnings | Snowflake SNOW earnings AI guidance | 29/50 | 58.0% | 24 | 14 | 4.2% | 50.0% | ok |
| 8 | Zscaler earnings | Zscaler ZS earnings | 20/43 | 46.5% | 162 | 68 | 6.7% | 50.0% | ok |
| 9 | Hewlett Packard Enterprise earnings | HPE earnings AI data center | 6/37 | 16.2% | 1067 | 576 | 0.0% | 16.7% | ok_low_relevance |
| 10 | Quantum computing stocks | quantum computing stocks US | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Foxconn / Hon Hai | Foxconn Hon Hai AI servers stock | 1/1 | 100.0% | 3081 | 0 | 0.0% | 0.0% | ok |
| 12 | Robinhood tokenized stocks | Robinhood HOOD tokenized stocks | 2/33 | 6.1% | 19887 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 13 | Meta AI glasses | Meta META AI glasses | 20/50 | 40.0% | 601 | 59 | 23.1% | 50.0% | ok |
| 14 | Oil stocks | oil stocks crude oil US equities | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | Uranium stocks | uranium stocks nuclear power US | 0/26 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 16 | Apple iPhone 18 launch | Apple AAPL iPhone 18 launch | 38/50 | 76.0% | 3455 | 682 | 36.8% | 10.0% | ok |
| 17 | TSMC | TSMC TSM stock AI semiconductor | 6/21 | 28.6% | 7 | 3 | 20.0% | 83.3% | ok_low_relevance |
| 18 | Memory stocks | memory stocks DRAM NAND HBM | 8/36 | 22.2% | 686 | 674 | 28.6% | 87.5% | ok_low_relevance |
| 19 | Samsara earnings | Samsara IOT earnings | 6/18 | 33.3% | 31 | 31 | 0.0% | 100.0% | ok |
| 20 | OpenAI Astra | OpenAI Astra AI model | 33/50 | 66.0% | 12446 | 3159 | 66.7% | 20.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Planet Labs earnings — ok_low_relevance
Relevance groups: `[["Planet Labs", "PL"], ["earnings", "results", "财报", "財報"]]`
- Rejected: $PL Double Bottom Pattern Forming #planetlabs #pl #investing #stocks #money
- Rejected: $PL Undervalued--Stock Analysis! #planetlabs #pl #investing #stocks #ai #money
- Rejected: Planet Labs Contradicting Stories #planetlabs #pl #investing #ai #money
- Rejected: $19 Make or Break Point #planetlabs #pl #investing #stocks #ai #money
- Rejected: $PL: Posts Record Q2 FY27 Revenue Building on Previously Disclosed Record Quarterly Performance

### U.S. semiconductor tariffs — ok_low_relevance
Relevance groups: `[["semiconductor", "chip", "半导体", "半導體"], ["tariff", "tariffs", "关税", "關稅"]]`
- Rejected: Trump Sees Iran Strikes Short-Lived as Oil, Dollar Fall | Daybreak Europe 9/3/2026
- Rejected: US and Iran Renew Fighting, Global Bond Rout Deepens
- Rejected: Stocks Steady Ahead of Jobs Report; US Retail Diesel Hits Record High | Bloomberg Brief 09/04/2026
- Rejected: Oil Stabilizes As Trump Says Iran Strikes To Be Short | The Opening Trade 9/3/2026
- Rejected: Commerce Secretary Lutnick on AI, Anthropic and Canada Talks

### Hewlett Packard Enterprise earnings — ok_low_relevance
Relevance groups: `[["HPE", "Hewlett Packard Enterprise"], ["earnings", "AI data center", "guidance", "财报", "財報"]]`
- Rejected: AI Spending Ripples Across Tech Stack; Nvidia Acquires Hugging Face | Bloomberg Tech 9/03/2026
- Rejected: Earnings Confirm the AI Memory Shortage Is Getting Worse!
- Rejected: HPE CFO on Company "Drinking Its Own Champagne" Thanks to AI Demand
- Rejected: HPE Stock -11.2% | hp enterprise server $12.2 B revenue vs 11.2% stock plunge #Shorts
- Rejected: $HPE: Dips Owing to Data Centre Networking Revenue Weakness.

### Quantum computing stocks — ok_no_relevant_videos
Relevance groups: `[["quantum computing stocks", "quantum stocks", "量子计算股", "量子計算股"]]`
- Rejected: D-Wave Stock Could EXPLODE 5x After This Massive Quantum Breakthrough
- Rejected: IONQ Stock Analysis: Don't Buy Until You See This
- Rejected: LAES Reveals How Its $24.5M Quantum Strategy Could Generate Revenue
- Rejected: RGTI Revenue Soars 183%, Is It Time to Buy This Quantum Stock! RGTI Stock Analysis
- Rejected: 6 ETFs to Know in 2026 | VDY, VOO, XEQT, ZSP, QTUM & SPSM Compared

### Robinhood tokenized stocks — ok_low_relevance
Relevance groups: `[["Robinhood", "HOOD"], ["tokenized stocks", "tokenized equities", "代币化股票", "代幣化股票"]]`
- Rejected: Solana vs Robinhood Chain💥The Bull-Run Tokens To Watch🚀
- Rejected: ROBINHOOD JUST SAVED CRYPTO 🚨 ARBITRUM EXPLODES 30%  🚨 $111M RWA VOLUME + $1.92M REVENUE!
- Rejected: I Put $1000 Into 7 Robinhood Chain Tokens! PONS, $AI, CASHCAT, STONKBROKER & More
- Rejected: 🚨 Robinhood Meme Coins I'm Buying Right Now with Huge Potential...
- Rejected: Robinhood Just Created Crypto's BIGGEST Bull Market

### Oil stocks — ok_no_relevant_videos
Relevance groups: `[["oil stocks", "energy stocks", "石油股", "原油股"]]`
- Rejected: Fed Comments & $93 Crude Oil Creates Mixed Rate Picture, NVDA Buys Hugging Face
- Rejected: Gas prices volatile after crude oil hits $97 per barrel
- Rejected: The Stock Market Is About To Go Crazy: Crude Oil Approaches $100
- Rejected: 🔴 Final Trade Live Updates: Stock Market Update | Crude Oil | Latest Business News | CNBC Awaaz
- Rejected: 🔴 Final Trade Live Updates: Stock Market Update | Crude Oil | Latest Business News | CNBC Awaaz

### Uranium stocks — ok_no_relevant_videos
Relevance groups: `[["uranium stocks", "uranium miners", "铀矿股", "鈾礦股"]]`
- Rejected: "The $1 Trillion AI Power Play: 5 Stocks That Won't Overheat"
- Rejected: Why Energy Fuels Is the Most Underestimated Critical Minerals Play! UUUU Stock Analysis
- Rejected: UUUU: Can Energy Fuels Handle a $1.8B Bet After a Brutal Q2! UUUU Stock Analysis
- Rejected: AI Is Winning. But Are AI Stocks Too Expensive?
- Rejected: Peter Boockvar & Dana Lyons - Commodities Hit 14-Year Highs as the 40-Year Bond Bull Dies

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "TSM", "Taiwan Semiconductor", "台積電", "台积电"]]`
- Rejected: Is One of the World's Best AI Stocks Cheap? Two Experts Can't Agree
- Rejected: NVIDIA vs. Google's Chips: The Fight Everyone Gets Wrong
- Rejected: EP.49: Why the AI Boom Is Still Early with Daniel Pilling from Sands Capital
- Rejected: GPT-6 Astra: Why OpenAI’s 99.9% Score Triggers a Silicon Run (NVDA, AVGO)
- Rejected: 5 FUTURE STOCKS to Hold for 10 YEARS 5 FUTURE STOCKS to Hold for 10 YEAR future stocks for long term

### Memory stocks — ok_low_relevance
Relevance groups: `[["memory stocks", "DRAM", "NAND", "HBM", "記憶體", "存储"]]`
- Rejected: The Memory War Just Entered Its Next Phase!
- Rejected: Earnings Confirm the AI Memory Shortage Is Getting Worse!
- Rejected: Micron's Back! The Hidden Pattern That Wall Street Missed
- Rejected: AI Memory Explained: Why AI Is Starving for RAM (HBM4, GDDR7, SRAM & PagedAttention)
- Rejected: Seoul's Silicon Trap: Why Korea's $173B Chip Boom Could Crash [Sources in description]

