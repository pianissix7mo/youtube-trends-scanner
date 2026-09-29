# YouTube Entity Enrichment

Generated: **2026-09-29T12:42:35.317410+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Micron Technology | Micron MU earnings | 31/50 | 62.0% | 64 | 46 | 4.2% | 50.0% | ok |
| 2 | Snowflake | Snowflake SNOW earnings | 0/24 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 3 | SpaceX | SpaceX 股票 Starship | 40/50 | 80.0% | 1032 | 25 | 5.9% | 0.0% | ok |
| 4 | Foxconn / Hon Hai | 鴻海 Foxconn 股票 AI | 2/6 | 33.3% | 196 | 196 | 0.0% | 100.0% | ok |
| 5 | Anthropic / Claude | Anthropic Claude AI | 50/50 | 100.0% | 37 | 31 | 4.3% | 70.0% | ok |
| 6 | AI agents | AI agents agentic AI | 42/50 | 84.0% | 42 | 7 | 10.0% | 30.0% | ok |
| 7 | Magnachip Semiconductor | Magnachip semiconductor MX | 2/2 | 100.0% | 77 | 77 | 0.0% | 100.0% | ok |
| 8 | Power semiconductors | power semiconductor 功率半導體 | 3/27 | 11.1% | 145 | 145 | 0.0% | 100.0% | ok_low_relevance |
| 9 | Global Unichip / 創意電子 | 創意 3443 Global Unichip AI | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 10 | Super Micro Computer | SMCI earnings Supermicro | 0/24 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Tower Semiconductor | Tower Semiconductor TSEM | 3/4 | 75.0% | 1 | 1 | 0.0% | 100.0% | ok |
| 12 | NVIDIA | NVIDIA NVDA | 46/50 | 92.0% | 1299 | 72 | 34.5% | 30.0% | ok |
| 13 | DoorDash | DoorDash DASH earnings | 2/31 | 6.5% | 545 | 545 | 0.0% | 100.0% | ok_low_relevance |
| 14 | TSMC | TSMC 台積電 semiconductor | 30/50 | 60.0% | 498 | 249 | 9.1% | 30.0% | ok |
| 15 | ON Semiconductor | ON Semiconductor ON Semi | 1/50 | 2.0% | 155 | 155 | 0.0% | 100.0% | ok_low_relevance |
| 16 | Navitas Semiconductor | Navitas Semiconductor NVTS | 13/14 | 92.9% | 12 | 11 | 0.0% | 90.0% | ok |
| 17 | Meta Platforms | Meta META earnings | 3/50 | 6.0% | 2172 | 126 | 0.0% | 33.3% | ok_low_relevance |
| 18 | Silver mining stocks | silver mining stocks 白银 | 1/50 | 2.0% | 4 | 4 | 0.0% | 100.0% | ok_low_relevance |
| 19 | Uranium stocks | uranium stocks uranium miners | 2/50 | 4.0% | 123 | 123 | 0.0% | 100.0% | ok_low_relevance |
| 20 | Costco | Costco COST earnings | 6/50 | 12.0% | 7 | 7 | 0.0% | 100.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Snowflake — ok_no_relevant_videos
Relevance groups: `[["Snowflake", "SNOW"], ["earnings", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: I co‑founded a business, got only $0.01! I returned countryside and created my huge supply chain!
- Rejected: Growth Acceleration: When the Business Changes Gears | Spotting the Inflection | Chapter 17
- Rejected: Bloomberg Surveillance 9/28/2026
- Rejected: The Economics of Owning a Ski Resort
- Rejected: Snowflake Soars 55% in 2026: AI Cloud Boom 🚀 #SNOW #Stocks #Investing

### Power semiconductors — ok_low_relevance
Relevance groups: `[["power semiconductor", "power semiconductors", "功率半導體", "功率半导体", "SiC", "GaN"]]`
- Rejected: 공장 가동률 98% 돌파 글로벌 큰손들이 DB하이텍에 목매는 진짜 이유#파운드리 #전력반도체#반도체사이클
- Rejected: How to Power Amplifier Diagram Using Transistor 🔌⚡ #diy #shortsfeed #trending #viral #shorts
- Rejected: AI研究室｜GPU再多也沒用？AI真正的隱藏瓶頸，竟然是「電網」#華城 #高力
- Rejected: Top 4 NPN Transistors Voltage & Current Rating ⚡🔌 #diy #shortsfeed #trending #viral #shorts
- Rejected: Microtek inverter V8 model PCB in Lowest price #microtekinverter #battery

### Super Micro Computer — ok_no_relevant_videos
Relevance groups: `[["SMCI", "Super Micro", "Supermicro", "超微"], ["earnings", "results", "财报", "財報", "业绩", "業績", "earnings call"]]`
- Rejected: Supermicro This Week: $60B+ ORDERS — WHAT HAPPENS NEXT?
- Rejected: $SMCI Super Micro Computer · Trade Analysis: three buys, one ceiling, a stop that only rises
- Rejected: The SMCI Story Everyone is Missing
- Rejected: SMCI Stock: Affordable Blackwell Valuation Explained
- Rejected: SMCI's $60 Billion AI Gamble: Massive Backlog vs. DOJ Nightmare

### DoorDash — ok_low_relevance
Relevance groups: `[["DoorDash", "DASH"], ["earnings", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: I Stopped Doing These 5 Things on DoorDash — I Make More Now
- Rejected: Doordash Delivery Vs Shipt Shopper | Which Gig Apps Makes The Most Money ?!?
- Rejected: 9 Superinvestors Cut DoorDash. A Director Bought $100M
- Rejected: How Much Can I Make on a Saturday Afternoon? DoorDash, Uber Eats & Grubhub
- Rejected: How I Made $53 Per Hour on Friday Night with Uber Eats!

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "ON Semi", "onsemi", "ON"]]`
- Rejected: The Future of Semiconductor #ai #investing #tech #business #education #podcast
- Rejected: $NVTS: Selected to Develop 10 KV SiC Power Semiconductors by U.S Army
- Rejected: 2 BEST SEMI CONDUCTOR STOCKS TO ADD WHILE STOCKS CRASH📉
- Rejected: When AI Designs Chips, What’s Left for Humans?
- Rejected: Will Nations Become NVIDIA’s Next Big Customers?

### Meta Platforms — ok_low_relevance
Relevance groups: `[["Meta", "Facebook", "脸书", "臉書"], ["earnings", "results", "财报", "財報", "业绩", "業績", "earnings call"]]`
- Rejected: META (Meta Platforms) After 4.7% Drop - 3 Price Cases + Tuesday Predicted Opening 🔥
- Rejected: MongoDB Plunges 18% as Meta Taps CEO To Lead New AI Platform | Closing Bell
- Rejected: META Muse Strengthens AI Profit Path, Trust in Platform Raises Next Roadblock
- Rejected: Meta’s Muse AI emerges as TOP-PERFORMING agent
- Rejected: Meta (META): What the Market Misses

### Silver mining stocks — ok_low_relevance
Relevance groups: `[["silver", "白银", "白銀"], ["miner", "miners", "mining", "矿业", "礦業", "矿商", "礦商"]]`
- Rejected: BULLISH or BEARISH!?! Fractal Tracking: AMC / GME / QQQ / SILVER / HYMC
- Rejected: New Secret Silver Project: Episode 1!
- Rejected: Gold & Silver Investing vs  Physical Bullion
- Rejected: Buying Silver? Here’s How to Find Better Deals! 🚨
- Rejected: 局势紧张，黄金却跌了将近 4%：避险资产这次为什么不避险

### Uranium stocks — ok_low_relevance
Relevance groups: `[["uranium", "铀", "鈾"], ["stock", "stocks", "miner", "miners", "mining", "矿业", "礦業"]]`
- Rejected: September 29, 2026: Uranium's Next Threshold
- Rejected: Energy Stocks Are the Hedge for Your Gold Miners
- Rejected: Elevate Uranium: 88% Mass Rejection, 90% Marenica Stake and What Comes Next
- Rejected: Centrus vs. Cameco: 2 Powerful Ways to Play the Nuclear Fuel Boom
- Rejected: Did uranium just put in a bottom?

### Costco — ok_low_relevance
Relevance groups: `[["Costco", "COST", "好市多"], ["earnings", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: Costco Stock is Rising: My Buy Price
- Rejected: Is Costco ($COST) a Good Long-Term Investment?
- Rejected: Costco Wholesale ($COST): 🛒 Moat Fortress or 44x Valuation Trap?
- Rejected: Why Costco Makes Billions From Memberships #costco #usashorts #business #money #finance #investing
- Rejected: Costco’s $1.50 Secret: Why It Refuses to Raise the Price

