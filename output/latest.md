# YouTube Entity Enrichment

Generated: **2026-09-04T11:32:14.917675+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Broadcom earnings | Broadcom AVGO earnings AI guidance | 26/50 | 52.0% | 502 | 77 | 26.3% | 30.0% | ok |
| 2 | Lululemon earnings | Lululemon LULU earnings outlook | 11/29 | 37.9% | 263 | 187 | 10.0% | 90.0% | ok |
| 3 | Semiconductor stocks | semiconductor stocks AI chips | 7/50 | 14.0% | 3368 | 537 | 40.0% | 71.4% | ok_low_relevance |
| 4 | Hewlett Packard Enterprise earnings | HPE earnings Oracle AI data center | 2/25 | 8.0% | 5635 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 5 | Snowflake earnings | Snowflake SNOW earnings AI guidance | 27/50 | 54.0% | 31 | 16 | 0.0% | 50.0% | ok |
| 6 | Japan semiconductor industry | Japan semiconductor industry AI chips | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 7 | VanEck Semiconductor ETF / SMH | SMH VanEck Semiconductor ETF | 3/6 | 50.0% | 14 | 14 | 0.0% | 100.0% | ok |
| 8 | Credo Technology earnings | Credo CRDO earnings AI networking | 4/12 | 33.3% | 851 | 503 | 0.0% | 50.0% | ok |
| 9 | Planet Labs earnings | Planet Labs PL earnings | 4/50 | 8.0% | 272 | 106 | 0.0% | 75.0% | ok_low_relevance |
| 10 | UiPath earnings | UiPath PATH earnings AI automation | 8/19 | 42.1% | 171 | 171 | 12.5% | 100.0% | ok |
| 11 | MongoDB earnings | MongoDB MDB earnings | 7/42 | 16.7% | 24 | 23 | 0.0% | 85.7% | ok_low_relevance |
| 12 | Palo Alto Networks earnings | Palo Alto PANW earnings | 24/50 | 48.0% | 157 | 37 | 6.2% | 20.0% | ok |
| 13 | Dell earnings | Dell DELL earnings AI server | 25/50 | 50.0% | 23 | 4 | 0.0% | 30.0% | ok |
| 14 | Zscaler earnings | Zscaler ZS earnings | 14/29 | 48.3% | 175 | 147 | 8.3% | 80.0% | ok |
| 15 | Gold | gold price Fed rates payrolls | 9/50 | 18.0% | 42 | 42 | 14.3% | 77.8% | ok_low_relevance |
| 16 | Quantum computing stocks | quantum computing stocks US | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 17 | U.S. nonfarm payrolls | US nonfarm payrolls jobs report Fed | 1/50 | 2.0% | 37 | 37 | 0.0% | 100.0% | ok_low_relevance |
| 18 | UMC / United Microelectronics | UMC United Microelectronics semiconductor | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 19 | Phison / NAND memory | Phison NAND flash memory AI | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 20 | TSMC | TSMC TSM stock AI semiconductor | 3/16 | 18.8% | 1 | 0 | 0.0% | 66.7% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor stocks", "chip stocks", "半导体股", "半導體股"]]`
- Rejected: 👀 This AI Stock Is Flying Under the Radar $AMKR
- Rejected: Nvidia Just Revealed Something HUGE Everyone Is Missing ($2 Trillion Backlog Explained!)
- Rejected: AVGO Adds AI Muscle in Earnings, Guidance & GOOGL Concentration Show Risks
- Rejected: NVIDIA Just Broke the AI Market — NVDA’s $96 BILLION Shocknvda
- Rejected: Crude Rises & 10-Year Yield Taps January 2025 Highs, AI Chips Lead Decline

### Hewlett Packard Enterprise earnings — ok_low_relevance
Relevance groups: `[["HPE", "Hewlett Packard Enterprise"], ["earnings", "财报", "財報", "Oracle", "AI data center", "guidance"]]`
- Rejected: $HPE: Dips Owing to Data Centre Networking Revenue Weakness.
- Rejected: HPE CFO on Company "Drinking Its Own Champagne" Thanks to AI Demand
- Rejected: AI Spending Ripples Across Tech Stack; Nvidia Acquires Hugging Face | Bloomberg Tech 9/03/2026
- Rejected: OpenAI’s Altman Unveils Astra as a New Step Toward AGI | The Close 9/3/2026
- Rejected: Professional Trading Roundtable: “A 50% Market Crash Is Mathematically Inevitable!”

### Japan semiconductor industry — ok_no_relevant_videos
Relevance groups: `[["Japan semiconductor", "Japanese semiconductor", "日本半导体", "日本半導體"]]`
- Rejected: Inside the AI Hardware Engine – Full Semiconductor Supply Chain Course
- Rejected: This New Chip Factory Is Coming for TSMC
- Rejected: Broadcom Sees AI Chip Boom as It Takes On Nvidia | The Pulse 9/3/2026
- Rejected: OpenAI’s Altman Unveils Astra as a New Step Toward AGI | The Close 9/3/2026
- Rejected: AI Spending Ripples Across Tech Stack; Nvidia Acquires Hugging Face | Bloomberg Tech 9/03/2026

### Planet Labs earnings — ok_low_relevance
Relevance groups: `[["Planet Labs", "PL"], ["earnings", "results", "财报", "財報"]]`
- Rejected: $PL: Posts Record Q2 FY27 Revenue Building on Previously Disclosed Record Quarterly Performance
- Rejected: $PL Undervalued--Stock Analysis! #planetlabs #pl #investing #stocks #ai #money
- Rejected: PL Stock Could Be MASSIVE… But There’s One Big Risk
- Rejected: $19 Make or Break Point #planetlabs #pl #investing #stocks #ai #money
- Rejected: Planet Labs Heading Towards Profit #planetlabs #pl #investing #techstocks #money #stocks

### MongoDB earnings — ok_low_relevance
Relevance groups: `[["MongoDB", "MDB"], ["earnings", "earnings call", "财报", "財報"]]`
- Rejected: MongoDB Inc ($MDB) — BEARISH | Full Deep Dive | StockTok
- Rejected: MDB Stock: 91% RPO Growth! 🚨 Is Something BIG Happening?
- Rejected: MDB Stock -13.8% | MongoDB stock drops 13.8 percent despite a 771.8 million dollar... #Shorts
- Rejected: MDB Stock -14.7% | Mongodb stock drops 14.7% despite a $772 million revenue beat. #Shorts
- Rejected: MDB vs. S&P 500

### Gold — ok_low_relevance
Relevance groups: `[["gold", "黄金", "黃金"], ["Fed", "rates", "payrolls", "yields", "利率", "非农", "非農"]]`
- Rejected: Will NFP Send Gold to $4,600 or Trigger a Selloff?
- Rejected: Gold’s Big Night Is Here! 🚨 Can Weak US Jobs Data Push Gold Back Above $4,500 & Toward $4,600?
- Rejected: 🔥 NFP COULD TRIGGER A BIG MOVE — GOLD & SILVER NEXT?
- Rejected: GOLD WARNING: Jobs Report Could Send Gold to $5,000 — Or $4,500! new gold price
- Rejected: IF YOU OWN GOLD OR SILVER, WATCH THIS BEFORE THURSDAY & FRIDAY | JAMIE DIMON'S WARNING

### Quantum computing stocks — ok_no_relevant_videos
Relevance groups: `[["quantum computing stocks", "quantum stocks", "量子计算股", "量子計算股"]]`
- Rejected: Before You Buy a Quantum Stock, Watch This (Rigetti $RGTI)
- Rejected: LAES Reveals How Its $24.5M Quantum Strategy Could Generate Revenue
- Rejected: Quantum Computing: The Next Big Disruptor for Indian Finance?
- Rejected: D-Wave Quantum Stock: $13 to $43… What's Next?? 🚀 #qbts #quantum #nyse
- Rejected: The Nobel Winner Who Built Google's Quantum Computer: Why I'm Building NVIDIA of Quantum

### U.S. nonfarm payrolls — ok_low_relevance
Relevance groups: `[["nonfarm payrolls", "jobs report", "非农", "非農"], ["Fed", "Federal Reserve", "美联储", "聯準會"]]`
- Rejected: Good Jobs Report… Bad for Stocks?
- Rejected: Is This The End of the Bull Run? PRE NFP Analysis
- Rejected: 🔴NFP JOBS REPORT 8:30AM! PAYROLL SHOCK MARKETS? | LIVE TRADING
- Rejected: How U.S. Jobs and Inflation Could Shape the Fed’s Next Decision
- Rejected: NFP AND UNEMPLOYMENT RATE Release Today: What to Expect

### UMC / United Microelectronics — ok_no_relevant_videos
Relevance groups: `[["UMC", "United Microelectronics", "聯華電子", "联华电子"]]`
- Rejected: 從花大錢丟垃圾到靠垃圾年賺1億，聯電砸18億打造創生中心，把半導體廢料變黃金 #永續是門好生意
- Rejected: This Company Wins when Memory Prices go UP

### Phison / NAND memory — ok_no_relevant_videos
Relevance groups: `[["Phison", "群聯", "群联", "潘健成"], ["NAND", "Flash", "memory", "記憶體", "存储"]]`
- Rejected: AI Storage: The Duopoly Nobody Noticed
- Rejected: 智慧移動的低功耗晶片架構與平台設計 | TO Talk EP159
- Rejected: The Art of the Deal Eludes Trump on Iran as Oil Gains | Insight with Haslinda Amin 9/2/2026

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "TSM", "台積電", "台积电", "Taiwan Semiconductor"]]`
- Rejected: Is One of the World's Best AI Stocks Cheap? Two Experts Can't Agree
- Rejected: NVIDIA vs. Google's Chips: The Fight Everyone Gets Wrong
- Rejected: EP.49: Why the AI Boom Is Still Early with Daniel Pilling from Sands Capital
- Rejected: How to Invest in China’s AI Revolution
- Rejected: Cybercab Robotaxi到底是不是特斯拉下一次“命运转折点”？#tsla #特斯拉 #cybercab #robotaxi #马斯克 #股票 #股市

