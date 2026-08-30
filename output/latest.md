# YouTube Entity Enrichment

Generated: **2026-08-30T11:02:21.429664+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | IREN earnings | IREN stock earnings | 15/50 | 30.0% | 2855 | 1081 | 57.1% | 30.0% | ok |
| 2 | Marvell earnings | Marvell MRVL earnings | 24/50 | 48.0% | 499 | 100 | 13.3% | 20.0% | ok |
| 3 | Workday earnings | Workday WDAY earnings | 12/32 | 37.5% | 21 | 12 | 0.0% | 70.0% | ok |
| 4 | Trump semiconductor tariff | Trump semiconductor tariff | 9/50 | 18.0% | 293 | 115 | 0.0% | 66.7% | ok_low_relevance |
| 5 | Dell earnings | Dell DELL earnings | 3/50 | 6.0% | 904 | 0 | 0.0% | 33.3% | ok_low_relevance |
| 6 | Canadian bank earnings | Canadian bank earnings RBC TD BMO | 1/5 | 20.0% | 2224 | 2224 | 100.0% | 100.0% | ok_low_relevance |
| 7 | Gap earnings | Gap GAP earnings | 11/50 | 22.0% | 127 | 10 | 0.0% | 20.0% | ok_low_relevance |
| 8 | Hormel earnings | Hormel HRL earnings | 2/8 | 25.0% | 7 | 7 | 0.0% | 100.0% | ok_low_relevance |
| 9 | Rocket Lab | Rocket Lab RKLB stock | 19/33 | 57.6% | 79 | 75 | 5.9% | 80.0% | ok |
| 10 | Lattice Semiconductor | Lattice Semiconductor LSCC stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 11 | Strategy / MSTR | Strategy MSTR Bitcoin stock | 28/50 | 56.0% | 70 | 70 | 25.0% | 100.0% | ok |
| 12 | TSMC | TSMC TSM stock | 11/30 | 36.7% | 34 | 34 | 18.2% | 100.0% | ok |
| 13 | NVIDIA earnings | NVIDIA NVDA earnings | 32/50 | 64.0% | 257 | 138 | 15.8% | 10.0% | ok |
| 14 | Salesforce earnings | Salesforce CRM earnings | 14/50 | 28.0% | 294 | 72 | 0.0% | 40.0% | ok_low_relevance |
| 15 | iShares Semiconductor ETF | SOXX iShares Semiconductor ETF | 1/3 | 33.3% | 543 | 543 | 0.0% | 100.0% | ok |
| 16 | Utility stocks | utility stocks AI data center power | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 17 | Gold stocks | gold stocks miners | 7/50 | 14.0% | 1369 | 1369 | 80.0% | 71.4% | ok_low_relevance |
| 18 | Mining stocks | mining stocks Canada US | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 19 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 8/10 | 80.0% | 54 | 54 | 0.0% | 100.0% | ok |
| 20 | Apple iPhone 18 | Apple AAPL iPhone 18 | 48/50 | 96.0% | 34987 | 23449 | 100.0% | 40.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Trump semiconductor tariff — ok_low_relevance
Relevance groups: `[["Trump", "tariff", "tariffs", "关税", "關稅"], ["semiconductor", "chip", "半導體", "半导体"]]`
- Rejected: 川普再出招？電子代工五大龍頭恐面暴擊 #川普 #關稅 #電子代工 #台灣 #代工
- Rejected: Trump Targets Semiconductors As Nvidia Surges
- Rejected: 트럼프 관세 협박이 삼전닉스에 안 통하는 이유
- Rejected: 트럼프가 반도체 관세 때려도 한국 기업이 타격 없는 이유
- Rejected: 주주환원에도 못가는 삼전닉스, 트럼프 '관세폭탄'까지 터지나?

### Dell earnings — ok_low_relevance
Relevance groups: `[["Dell"], ["earnings", "results"]]`
- Rejected: World Cup Trading Champion Warns: Is the Market About to Roll Over? (NVDA, DELL, CRDO, MAGS)
- Rejected: HPE vs Dell  AI Value Play
- Rejected: Dell Ripped 262%, Broadcom 6%. Both Report Next Week. #shorts #DELL #AVGO #stocks
- Rejected: 5 Stories Moving Markets This Week Jobs Broadcom Dell Gold & Treasury
- Rejected: Should You Buy This Dell Tower? — Dell 2026 Edition Tower Computers Desktop Computer — Review

### Canadian bank earnings — ok_low_relevance
Relevance groups: `[["RBC", "Royal Bank", "TD", "BMO", "Scotiabank", "CIBC", "Canadian bank"], ["earnings", "results", "earnings call"]]`
- Rejected: JUST IN: 100,000 Jobs On The Line — Why Trump’s Trade War Just Triggered A Recession Warning
- Rejected: IT'S HAPPENING: CANADA OUTSMARTS USA As Carney EXPOSES Trump's VENEZUELA Oil Scam
- Rejected: Big Banks Post Surprising Profits as Mortgage Stress Builds
- Rejected: AI Earnings Test with NVIDIA, Marvell, CrowdStrike, Salesforce, and More

### Gap earnings — ok_low_relevance
Relevance groups: `[["Gap"], ["earnings", "results"]]`
- Rejected: Work to do at Old Navy, but Gap is hanging in there, says top retail analyst Dana Telsey
- Rejected: Gap shares jump after company names new Old Navy CEO to revive struggling brand
- Rejected: Every Earnings Winner Reversed Today
- Rejected: Wealth Gap Growing: Corporate profits at record high as worker paychecks wilt
- Rejected: GAP Just Jumped 18% — The EV Signal Nobody’s Watching Yet

### Hormel earnings — ok_low_relevance
Relevance groups: `[["Hormel", "HRL"], ["earnings", "results"]]`
- Rejected: HRL Under Pressure: Why HRL's 10.2% matters more than it looks
- Rejected: Market Recap Live | Best Buy Earnings | August 27, 2026
- Rejected: Salesforce Soars 23% on Anthropic Deal as S&P 500 Ekes Out Gain | S&P 500 (2026-08-27)
- Rejected: Week of Aug 28 | Software +5.9% vs Chips -2.2% — Warsh Hawkish Shock Triggers Massive Tech Rotation
- Rejected: Okta Soared 28% in a Day and the VIX Just Fell Asleep | Aug 27, 2026 #Shorts

### Salesforce earnings — ok_low_relevance
Relevance groups: `[["Salesforce", "CRM"], ["earnings", "results"]]`
- Rejected: Bull Market SURGE As Nvidia, Salesforce and Crowdstrike BLAST! Watch For This Mega Money Rotation
- Rejected: Salesforce Eases Investor Fears
- Rejected: Nvidia’s AI Boom, Salesforce’s Anthropic Bet | Bloomberg Tech 8/27/2026
- Rejected: This Month at Salesforce | Ep 3 – Xero, Legora, and Replit
- Rejected: The Stock Market Just Went Ballistic on Major Stock Earnings

### Utility stocks — ok_no_relevant_videos
Relevance groups: `[["utility stocks", "utilities"], ["AI", "data center", "power", "electricity", "grid"]]`
- Rejected: 3 Energy Stocks Set to Double From the AI Data Center Boom
- Rejected: Nano Nuclear Energy (NNE) CEO on Role in Data Centers, Power Partnerships
- Rejected: AI Singularity Is Here: AI Infra, $100K Bets, & The 10-Year Supercycle 🚀
- Rejected: Nvidia’s AI Boom, Salesforce’s Anthropic Bet | Bloomberg Tech 8/27/2026
- Rejected: Nvidia Ignites AI Rally Ahead of Jackson Hole | Open Interest 8/27/2026

### Gold stocks — ok_low_relevance
Relevance groups: `[["gold stocks", "gold miners", "gold mining"]]`
- Rejected: Gold & Silver Stocks: 5 Miners Riding the Treasury Buyback
- Rejected: Finding The Next 10X Gold Stock
- Rejected: Gold Bull Run Or Fakeout? Miners The Best Swing Short
- Rejected: Gold Just Broke the 200-Day — Don't Panic Yet
- Rejected: $6000 Gold by Next Year: Long-Term Playbook for Gold and Silver Mining Stocks with Jeff Clark

### Mining stocks — ok_no_relevant_videos
Relevance groups: `[["mining stocks", "miners", "mining companies"]]`
- Rejected: Stocks, Bonds Waver Ahead of Warsh Speech | Bloomberg Brief 08/28/2026
- Rejected: Canada-U.S. Trade War could CRIPPLE American Metal Market
- Rejected: Warsh Speech from Jackson Hole on Deck | Opening Trade 8/28/2026
- Rejected: CANADA DELIVERS DEVASTATING WAKE UP CALL as Trump's Trade War Backfires In His Face
- Rejected: 川普50%關稅逼加拿大翻臉！能源、美債到中國市場 卡尼準備打持久戰！一條海峽讓川普贏不了！伊朗扣住全球能源命脈【#寰宇全視界】20260829-完整版 謝忠岳 介文汲 林郁方 戴志言

