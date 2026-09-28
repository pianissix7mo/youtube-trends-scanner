# YouTube Entity Enrichment

Generated: **2026-09-28T23:22:05.184636+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Snowflake | Snowflake SNOW earnings | 0/26 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 2 | Tower Semiconductor | Tower Semiconductor TSEM stock | 4/4 | 100.0% | 11 | 11 | 0.0% | 100.0% | ok |
| 3 | iShares Semiconductor ETF | SOXX iShares Semiconductor ETF | 2/5 | 40.0% | 209 | 209 | 0.0% | 100.0% | ok |
| 4 | SpaceX | SpaceX stock SPCX | 35/50 | 70.0% | 446 | 83 | 16.7% | 30.0% | ok |
| 5 | Netflix | Netflix NFLX stock | 22/37 | 59.5% | 34 | 39 | 9.5% | 100.0% | ok |
| 6 | Magnachip Semiconductor | Magnachip MX stock | 2/3 | 66.7% | 157 | 157 | 0.0% | 100.0% | ok |
| 7 | Oracle | Oracle ORCL stock | 38/50 | 76.0% | 70 | 57 | 15.2% | 60.0% | ok |
| 8 | Valens Semiconductor | Valens Semiconductor VLN stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | Micron | Micron MU earnings | 25/50 | 50.0% | 112 | 104 | 15.0% | 70.0% | ok |
| 10 | AI stocks | AI stocks | 27/50 | 54.0% | 252 | 100 | 6.2% | 20.0% | ok |
| 11 | Tariffs and stocks | tariffs stocks trade war | 15/50 | 30.0% | 958 | 37 | 0.0% | 10.0% | ok |
| 12 | Amazon | Amazon AMZN stock | 23/50 | 46.0% | 46 | 38 | 22.2% | 60.0% | ok |
| 13 | U.S. stock market today | stock market today SPY QQQ | 37/50 | 74.0% | 129 | 93 | 21.9% | 80.0% | ok |
| 14 | Mortgage rates | mortgage rates Treasury yields | 5/50 | 10.0% | 12 | 12 | 0.0% | 100.0% | ok_low_relevance |
| 15 | AI agents | AI agents agentic AI | 42/50 | 84.0% | 87 | 55 | 15.2% | 40.0% | ok |
| 16 | Anthropic Claude | Claude Anthropic AI | 49/50 | 98.0% | 1046 | 583 | 38.2% | 30.0% | ok |
| 17 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 3/4 | 75.0% | 75 | 75 | 0.0% | 100.0% | ok |
| 18 | Tesla | Tesla TSLA earnings | 1/50 | 2.0% | 4985 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 19 | NVIDIA | NVIDIA NVDA earnings | 4/50 | 8.0% | 3056 | 1128 | 66.7% | 75.0% | ok_low_relevance |
| 20 | TSMC | TSMC TSM stock | 5/23 | 21.7% | 15 | 11 | 0.0% | 40.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Snowflake — ok_no_relevant_videos
Relevance groups: `[["Snowflake", "SNOW"], ["earnings", "results", "财报", "財報"]]`
- Rejected: Growth Acceleration: When the Business Changes Gears | Spotting the Inflection | Chapter 17
- Rejected: The Economics of Owning a Ski Resort
- Rejected: He Slaps His Enemy Away With One Hit and Lives Like an Ordinary Man While Hiding Infinite Power
- Rejected: 窮小夥把身上僅剩的5塊錢給了乞丐老頭，竟覺醒吹牛系統，別人吹牛他美夢成真超爽打臉！#短劇 #爽劇 #穿越 #重生
- Rejected: 辽宁沈阳东北饺子，抻面拌鸡架，老式泥炉烧烤，阿星逛故宫大帅府Traditional northeast cuisine from Shenyang, Liaoning

### Mortgage rates — ok_low_relevance
Relevance groups: `[["mortgage rates", "mortgage rate", "房贷利率", "房貸利率"], ["Treasury", "yield", "yields", "利率", "收益率"]]`
- Rejected: The US Bond Market Is Breaking: Why the 10-Year Treasury Yield Matters in 2026 📉
- Rejected: Bond Yields Hit a 19-Year High. Why Aren't Stocks Falling?
- Rejected: The 10-Year Treasury Yield: The Number That Moves Gold, Mortgages and Your 401k
- Rejected: Mortgage Rates HIT 7.45%...A Seller Could Cut Your Payment
- Rejected: 3. Why Mortgage Rates Don't Follow the Fed

### Tesla — ok_low_relevance
Relevance groups: `[["Tesla", "TSLA"], ["earnings", "results", "财报", "財報"]]`
- Rejected: We NEED to Discuss Tesla Optimus Robots NOW.
- Rejected: TSLA This Week: SOMETHING BIG IS DEVELOPING
- Rejected: Tesla Model Y L Delivery: Surprising Changes You Should Know
- Rejected: ChargePoint (CHPT) CFO on EV Future in AI Robotaxi Age, Earnings Outperformance
- Rejected: Tesla Cybercab Gets a Flat Tire, and Grok Builds FSD!

### NVIDIA — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA", "英伟达", "輝達"], ["earnings", "results", "财报", "財報"]]`
- Rejected: NVIDIA's Stock is "Incredibly Misunderstood" — The 2026 Deep Dive
- Rejected: NVDA Stock - Whats Next For NVIDIA? (NVDA/AMD/TSM/AVGO)
- Rejected: Micron Nvidia AMD SanDisk Broadcom STOCKS The Warning Nobody Sees ($MU $NVDA $AMD $SNDK $AVGO)
- Rejected: The Market May Be Wrong About These 2 AI Stocks
- Rejected: Why I Own NVIDIA After 8x Revenue Growth

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "Taiwan Semiconductor", "TSM", "台积电", "台積電"]]`
- Rejected: 3 Incredible Stocks to Buy and Hold for Years!!
- Rejected: The Top Stocks in My $100K Portfolio
- Rejected: Weekly Outlook Tech Stock Breakout or Fakeout? QQQ, MAG7 & Tesla Chart Analysis
- Rejected: ⁨ ممكن تختار الشركة الصح… وتدخل بالسعر الغلط. #investwithsanad #employeefirst
- Rejected: Die krasseste Firma der Welt

