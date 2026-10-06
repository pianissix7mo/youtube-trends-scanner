# YouTube Entity Enrichment

Generated: **2026-10-06T11:49:11.273775+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Applied Digital | Applied Digital APLD earnings AI data centers | 8/20 | 40.0% | 97 | 97 | 0.0% | 100.0% | ok |
| 2 | Oracle | Oracle ORCL stock cloud AI | 12/27 | 44.4% | 29 | 29 | 0.0% | 100.0% | ok |
| 3 | Costco | Costco COST earnings | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 4 | Applied Optoelectronics | Applied Optoelectronics AAOI stock AI optics | 1/5 | 20.0% | 3 | 3 | 0.0% | 100.0% | ok_low_relevance |
| 5 | Uber | Uber UBER earnings Uber Eats | 7/50 | 14.0% | 256 | 256 | 28.6% | 100.0% | ok_low_relevance |
| 6 | Tesla | Tesla TSLA earnings call Elon Musk | 1/50 | 2.0% | 24 | 24 | 0.0% | 100.0% | ok_low_relevance |
| 7 | Foxconn / Hon Hai | Foxconn Hon Hai 2317 stock AI servers | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 8 | Data center stocks | data center stocks AI infrastructure | 4/50 | 8.0% | 14 | 14 | 33.3% | 75.0% | ok_low_relevance |
| 9 | NVIDIA | NVIDIA NVDA earnings AI chips | 12/50 | 24.0% | 60 | 39 | 0.0% | 60.0% | ok_low_relevance |
| 10 | UMC | UMC UMC stock semiconductor foundry | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Circle Internet Group | Circle CRCL stock USDC stablecoin | 4/5 | 80.0% | 12 | 12 | 0.0% | 100.0% | ok |
| 12 | MediaTek | MediaTek 2454 AI chips news | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 13 | Semiconductor industry | semiconductor industry AI chips stocks | 4/50 | 8.0% | 1422 | 1422 | 50.0% | 100.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Costco — ok_no_relevant_videos
Relevance groups: `[["Costco", "COST"], ["earnings", "results"]]`
- Rejected: Costco (COST): why investors still pay up for the stock
- Rejected: Costco’s Best and Worst Values (What Bulk Pricing Hides)
- Rejected: Why Costco Makes Half Its Profit From a $65 Card
- Rejected: Why Costco Is Being Valued Like a Tech Giant (It’s Not Just Hot Dogs)
- Rejected: Who Actually Gets Paid When You Shop at Costco

### Applied Optoelectronics — ok_low_relevance
Relevance groups: `[["Applied Optoelectronics", "AAOI"], ["optics", "AI", "stock", "股票"]]`
- Rejected: $AAOI: Concerns Ease Owing to Rebound after $588 Million Raise
- Rejected: $200M in Orders It Can't Build Fast Enough: How Applied Optoelectronics (AAOI) Makes Money
- Rejected: FCC Ban on Chinese Optical Modules: The 65% Rule and Lumentum (LITE)
- Rejected: 'STILL GOING HIGHER': We haven't seen the TOP of this yet, analyst says

### Uber — ok_low_relevance
Relevance groups: `[["Uber", "Uber Eats"], ["earnings", "delivery"]]`
- Rejected: How Much Can You Make on a Busy Saturday? DoorDash, Uber Eats & Grubhub
- Rejected: How Much Can I Make Delivering Uber Eats, DoorDash & Grubhub on a Sunday?
- Rejected: REALISTIC UberEats Shift in LA | Trying to make $300 in 12 Hours (Unfiltered Earnings)
- Rejected: $46+/HR + I Couldn’t Believe the Tips! | Friday Uber Eats Ride Along!
- Rejected: We Did Uber Eats for ONLY 3 HOURS… How Much did We Make! Vlogtober day 2!!💰🚗😱

### Tesla — ok_low_relevance
Relevance groups: `[["Tesla", "TSLA", "Elon Musk"], ["earnings call", "earnings"]]`
- Rejected: Elon Musk Becomes A Trillionaire—Again—After SpaceX Stock Jumps
- Rejected: Elon Just Built Something Bigger Than The ISS
- Rejected: Young Elon Musk Talks Tesla in 2008 #elonmusk #shorts
- Rejected: Nobody Expected What Tesla Just Reported
- Rejected: In 2008 Elon could have saved one company. He refused to pick. #shorts

### Foxconn / Hon Hai — ok_no_relevant_videos
Relevance groups: `[["Foxconn", "Hon Hai", "鴻海", "2317"], ["stock", "股票", "AI server"]]`
- Rejected: Foxconn's Q3 Up 47%: Will the AI Streak Hold in Q4? | Two Supports, One Warning, Three Checks

### Data center stocks — ok_low_relevance
Relevance groups: `[["data center stocks", "AI infrastructure", "data centers"]]`
- Rejected: Advanced Micro Devices (AMD): AI Data Center Growth | #AIDataCenters #AIstocks
- Rejected: This Data Center SmallCap Export Play is Unstoppable! | Sadhan
- Rejected: Why Building a 1-Gigawatt AI Data Center Costs $10,000,000,000
- Rejected: AI Data Center Boom: Bubble or Lasting Infrastructure!?
- Rejected: AI Data Center Power Crunch Could Send Renewables Soaring Next Year—First Stock to Move?

### NVIDIA — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA"], ["earnings", "AI", "chips"]]`
- Rejected: Why this is going to be a transformative earnings season
- Rejected: NVIDIA Made Me Rich. I'm Buying This Stock Next.
- Rejected: NVIDIA: The Next Dividend Compounder? My $309 Fair Value
- Rejected: If You Missed Nvidia Stock, This is Way Bigger
- Rejected: Watch SPX as NVDA Nears Record High, MU Consolidates #shorts

### UMC — ok_no_relevant_videos
Relevance groups: `[["UMC", "United Microelectronics", "聯電"], ["stock", "股票", "foundry"]]`
- Rejected: 00927本季配息升至2元創新高 年化配息率達20.1% 訂10/19除息 10/16日最後買進.11/13發放｜20261005｜非凡財經新聞

### Semiconductor industry — ok_low_relevance
Relevance groups: `[["semiconductor industry", "半導體", "半導體 元件", "chips"]]`
- Rejected: PTC Rallies on Deal; Qualcomm Up on Chip Patent Licensing | Stock Movers
- Rejected: Dan Ives Was Right! - 3 AI Stocks For The Next Wave: 2 Immediate Buys & 1 Dip Target! Act Fast
- Rejected: NVDA Boosts Share Buyback to $235B: Reinforcing AI Stack, Monetizing Tech Businesses
- Rejected: Nvidia Just Delivered Massive News for These 10 Stocks
- Rejected: Can Nvidia hit $6 trillion? Wedbush's Matt Bryson on memory, open-weight AI and Intel

