# YouTube Entity Enrichment

Generated: **2026-08-28T12:31:09.376953+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NVIDIA earnings | NVIDIA NVDA earnings 财报 輝達 | 15/27 | 55.6% | 130 | 42 | 16.7% | 70.0% | ok |
| 2 | Marvell earnings | Marvell MRVL earnings guidance | 9/39 | 23.1% | 393 | 325 | 28.6% | 77.8% | ok_low_relevance |
| 3 | IREN earnings | IREN earnings AI data center | 7/50 | 14.0% | 1102 | 628 | 50.0% | 85.7% | ok_low_relevance |
| 4 | Salesforce earnings | Salesforce CRM earnings call | 16/50 | 32.0% | 1743 | 197 | 14.3% | 20.0% | ok |
| 5 | Intuit earnings | Intuit INTU earnings | 23/50 | 46.0% | 72 | 39 | 5.9% | 40.0% | ok |
| 6 | Royal Bank / Canadian bank earnings | RBC RY Canadian bank earnings | 2/3 | 66.7% | 28 | 28 | 0.0% | 100.0% | ok |
| 7 | Lattice Semiconductor | Lattice Semiconductor LSCC stock | 1/1 | 100.0% | 2 | 2 | 0.0% | 100.0% | ok |
| 8 | VanEck Semiconductor ETF | VanEck Semiconductor ETF SMH | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Taiwan drone / defense stocks | 台灣 無人機 軍工股 雷虎 世紀 | 3/4 | 75.0% | 4717 | 0 | 0.0% | 0.0% | ok |
| 10 | Coinbase | Coinbase COIN stock crypto | 7/50 | 14.0% | 49 | 10 | 0.0% | 71.4% | ok_low_relevance |
| 11 | Utility stocks | utility stocks power AI data centers | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 12 | Semiconductor packaging | semiconductor packaging advanced packaging AI chips | 2/50 | 4.0% | 6 | 6 | 0.0% | 100.0% | ok_low_relevance |
| 13 | AI agents | AI agents agentic AI stocks | 19/50 | 38.0% | 50 | 49 | 11.1% | 90.0% | ok |
| 14 | Saudi Arabia nuclear deal | Saudi Arabia US nuclear deal stocks uranium | 1/9 | 11.1% | 396 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 15 | Strait of Hormuz / oil | Strait of Hormuz oil Iran shipping stocks | 24/50 | 48.0% | 685 | 76 | 9.1% | 10.0% | ok |
| 16 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 7/10 | 70.0% | 42 | 42 | 0.0% | 100.0% | ok |
| 17 | TSMC | TSMC TSM Taiwan Semiconductor 台積電 | 3/5 | 60.0% | 718 | 718 | 33.3% | 100.0% | ok |
| 18 | ON Semiconductor | ON Semiconductor onsemi stock | 1/2 | 50.0% | 18 | 18 | 0.0% | 100.0% | ok |
| 19 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 20 | Power semiconductors | power semiconductor SiC GaN 功率半導體 | 2/4 | 50.0% | 53 | 53 | 0.0% | 100.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Marvell earnings — ok_low_relevance
Relevance groups: `[["Marvell", "MRVL"], ["earnings", "results", "guidance", "財報", "财报"]]`
- Rejected: Options Trades in CME & MRVL as NVDA Lifts Tech Sector
- Rejected: Marvell Earning Falls and NVDA Is a Better Buy!
- Rejected: Marvell Just Had a Record Quarter — and the Stock Fell Anyway
- Rejected: Ghabour: September Will Create Buy Opportunity, MU & MRVL Strong Outlook
- Rejected: MRVL Stock: How Hyperscalers Fuel Custom Silicon Demand

### IREN earnings — ok_low_relevance
Relevance groups: `[["IREN", "Iris Energy"], ["earnings", "results", "AI", "data center"]]`
- Rejected: Stock update: $IREN | Ornn H100 Volatility Index | Moonshot Approaches Hyperscalers for Kimi K#
- Rejected: Ep. 54: $NVDA Earnings, New $AAPL Macs, $MU CEO Interview, $META Settlement
- Rejected: Nvidia Earnings Call: 5 Biggest Takeaways + My Strategy
- Rejected: BLOWOUT Earnings, Marvel, AI Stock Picking & FED Talk | 8.27 | One Lucky Dog
- Rejected: Buy EVERY Share You Can: THIS $9 Stock Is at the Center of the AI Buildout

### VanEck Semiconductor ETF — ok_no_relevant_videos
Relevance groups: `[["VanEck Semiconductor", "SMH", "semiconductor ETF", "chip ETF"]]`
- Rejected: SOXS: What the Expense Ratio Costs Over a Full Cycle
- Rejected: comment ‘stocks’ for me to send everything 💸🥂#investingforbeginners #investing #finance

### Coinbase — ok_low_relevance
Relevance groups: `[["Coinbase", "COIN"], ["stock", "股票", "crypto", "Bitcoin"]]`
- Rejected: The Man Behind Coinbase: Interview with Brian Armstrong | KMP Ep.52
- Rejected: Top 7 Crypto Coins that will 7x in 30 days!?
- Rejected: Breakout Alert: $215 Level Targets $400!
- Rejected: Is This What the Future of Crypto Investing Looks Like? Shyft Finance
- Rejected: Coinbase Surges 4.3% on $2B Tokenized Stocks Shock—Is More Upside Ahead? #Cryptocurrency #NASDAQCOIN

### Utility stocks — ok_no_relevant_videos
Relevance groups: `[["utility stocks", "utilities", "power stocks"], ["AI", "data center", "rates"]]`
- Rejected: $1.4 Trillion Power Grid Boom - Which AI Stock Wins?
- Rejected: JPMorgan's Kevin Curtin on AI backlash: There's always risk with financing infrastructure projects
- Rejected: Tech Stocks Gain on AI Optimism as Nvidia Jumps | The Pulse 8/27/2026
- Rejected: Nvidia Fuels AI Trade, Warsh Countdown | Bloomberg Businessweek Daily 8/27/2026
- Rejected: Nvidia Ignites AI Rally Ahead of Jackson Hole | Open Interest 8/27/2026

### Semiconductor packaging — ok_low_relevance
Relevance groups: `[["semiconductor packaging", "advanced packaging", "CoWoS", "packaging"], ["AI", "chips", "HBM"]]`
- Rejected: AI Is Breaking Down Japan’s Invisible Barrier in Semiconductor Materials
- Rejected: Beyond Silicon: The Materials That Could Build Trillion-Transistor Chips
- Rejected: NVIDIA Just Sent a Massive Signal to the Chip Industry 🚨 #semiconductors
- Rejected: China Beats the Chip Blockade? How Beijing Is Closing the Tech Gap | Statecraft With Geeta Mohan
- Rejected: SK hynix holds groundbreaking ceremony for HBM production base in U.S.

### Saudi Arabia nuclear deal — ok_low_relevance
Relevance groups: `[["Saudi Arabia", "Saudi"], ["nuclear", "civil nuclear", "Congress", "uranium"]]`
- Rejected: 川普被「40兆國債」逼瘋了！強佔中東石油不成 轉頭勒索盟友1.5兆 狂印鈔將「引爆全球恐慌」！｜#獨家觀點 #寰宇全視界 #寰宇新聞@globalvisiontalk
- Rejected: 加拿大不當美附屬品！150萬戶電力、九成進口鉀肥全成反擊王牌！荷蘭斷供反逼安世自立門戶 12吋晶圓硬闖成功！國產化狂飆近100%【#環球大戰線】20260827-完整版 葉思敏 賴岳謙 楊永明 栗正傑
- Rejected: 美農民40年來最慘危機！630億美元蒸發、中國抽走大豆、加拿大卡住化肥！中印俄抱團反擊！川普打中、制印、封俄 反逼三國聯手【#環球大戰線】20260826-完整版 葉思敏 侯漢廷 苑舉正 彭華幹
- Rejected: 加拿大反殺川普紅州！化肥告急農民崩盤 川普50%關稅再補一刀：福特通用先中槍！殲-16再拿飆風祭旗 40架殲-10CE殺進北非！【#環球大戰線】20260825-完整版 葉思敏 介文汲 王尚智 張延廷
- Rejected: 川普被「40兆國債」逼瘋了！強佔中東石油不成 轉頭勒索盟友1.5兆 狂印鈔將「引爆全球恐慌」！｜#獨家觀點 #寰宇全視界@globalvisiontalk

