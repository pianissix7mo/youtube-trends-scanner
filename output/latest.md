# YouTube Entity Enrichment

Generated: **2026-08-27T13:03:49.891819+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NVIDIA earnings | NVIDIA NVDA earnings 财报 輝達 | 18/31 | 58.1% | 93 | 34 | 7.1% | 60.0% | ok |
| 2 | CrowdStrike earnings | CrowdStrike CRWD earnings 财报 | 1/2 | 50.0% | 43 | 43 | 0.0% | 100.0% | ok |
| 3 | Salesforce earnings | Salesforce CRM earnings call 财报 | 1/1 | 100.0% | 43 | 43 | 0.0% | 100.0% | ok |
| 4 | Dick's Sporting Goods earnings | Dick's Sporting Goods DKS earnings | 5/50 | 10.0% | 49 | 49 | 0.0% | 100.0% | ok_low_relevance |
| 5 | Intuit earnings | Intuit INTU earnings 财报 | 1/6 | 16.7% | 9 | 9 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Lattice Semiconductor | Lattice Semiconductor LSCC stock | 1/1 | 100.0% | 4 | 4 | 0.0% | 100.0% | ok |
| 7 | Semiconductor supply chain | semiconductor supply chain AI chips 半导体 供应链 | 1/41 | 2.4% | 752 | 752 | 0.0% | 100.0% | ok_low_relevance |
| 8 | Semiconductor ETFs | semiconductor ETF SMH SOXX XSD | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | U.S. semiconductor manufacturing | US semiconductor manufacturing fabs CHIPS | 2/50 | 4.0% | 77 | 77 | 0.0% | 100.0% | ok_low_relevance |
| 10 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 5/8 | 62.5% | 30 | 30 | 0.0% | 100.0% | ok |
| 11 | ON Semiconductor | ON Semiconductor onsemi ON stock | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 12 | TSMC | TSMC TSM Taiwan Semiconductor 台积电 台積電 | 6/9 | 66.7% | 42 | 42 | 16.7% | 100.0% | ok |
| 13 | indie Semiconductor | indie Semiconductor INDI stock | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 14 | Taiwan drone / defense stocks | 雷虎 世紀 無人機 軍工股 台股 | 2/3 | 66.7% | 2436 | 0 | 0.0% | 0.0% | ok |
| 15 | AU Optronics | 友達 AUO 股票 display | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 16 | Copper stocks | copper stocks copper miners 铜矿股 | 0/16 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 17 | AI agents | AI agents agentic AI stocks 智能体 | 19/50 | 38.0% | 20 | 20 | 0.0% | 100.0% | ok |
| 18 | Claude / Anthropic | Claude AI Anthropic stocks | 26/50 | 52.0% | 145 | 43 | 0.0% | 20.0% | ok |
| 19 | Canada-U.S. retaliatory tariffs | Canada US retaliatory tariffs trade stocks | 37/50 | 74.0% | 8677 | 697 | 33.3% | 10.0% | ok |
| 20 | Power semiconductors | power semiconductor SiC GaN 功率半導體 | 3/4 | 75.0% | 9 | 9 | 0.0% | 100.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Dick's Sporting Goods earnings — ok_low_relevance
Relevance groups: `[["Dick's Sporting Goods", "DKS"], ["earnings", "results", "财报", "財報"]]`
- Rejected: Dick's Sporting Goods Stock Is Down -50%. Is It A Buy Yet? $DKS
- Rejected: DICKS STOCK FALLS 28%! IS THIS STOCK A BUY? DICKS SPORTING GOODS STOCK ANALYSIS
- Rejected: DKS Fumbles: Double Miss & Lowered Guidance Plunges Stock
- Rejected: Why Is DKS Stock Down? $DKS Stock Crashed 30.6% — Full Breakdown
- Rejected: DICK’S Sporting Goods (DKS) Stock CRASHES! Is This a MASSIVE Buying Opportunity?

### Intuit earnings — ok_low_relevance
Relevance groups: `[["Intuit", "INTU", "QuickBooks", "TurboTax"], ["earnings", "results", "财报", "財報"]]`
- Rejected: 最佳卖出时机 vs 最完美的买入？| Your $$$ Is Ready To Move! | HelloYFi
- Rejected: Intuit财捷集团深度分析｜收入增长14%却裁员17%，股价从高点腰斩！AI正在摧毁TurboTax，还是逼出40年软件巨头的第二次转型？
- Rejected: 2026/08/26(三) 美債空頭回補，科技股警報解除？
- Rejected: 中东局势骤变油价跳水，芯片股绝地大反击！DKS暴跌30%敲响消费警钟，还有哪些公司要被AI砸盘？#turbotax #quickbooks #dks
- Rejected: NVIDIA $96.2B Q2 Revenue & Salesforce Anthropic Claudeforce Rotation [Aug 26, 2026]

### Semiconductor supply chain — ok_low_relevance
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"], ["supply chain", "供应链", "供應鏈"]]`
- Rejected: 一顆晶片都不給賣！華為搶進埃及AI標案 川普急Call輝達組聯盟火線攔截【關鍵時刻】張炤和 ⁨@ebcCTime⁩
- Rejected: 機器人崛起｜張振驊ft.工研院南分院執行長 周大鑫｜#shorts｜台灣大時代｜2026.08.29｜
- Rejected: ST’s Third 2026 Price Hike Warns on Power Chips #Semiconductors #SupplyChain
- Rejected: 台股科技脈動｜AI算力衝向太空！從液冷散熱、CPO矽光子到SpaceX星際台廠供應鏈全解析 (2026-08-26)
- Rejected: 需求明明還在，美光與費半為什麼一直跌？機構正在悄悄切換定價邏輯！英偉達財報前必看！

### U.S. semiconductor manufacturing — ok_low_relevance
Relevance groups: `[["semiconductor", "chip", "fab", "foundry"], ["US", "U.S.", "manufacturing", "reshoring", "CHIPS"]]`
- Rejected: Musk Is Betting Against 40 Years of Chip History
- Rejected: Dylan Patel – Two labs will soon control most of the world's workforce
- Rejected: OpenAI Says New Jalapeno Chips Outperformed Nvidia in Testing
- Rejected: Nvidia Earnings, Apple’s AI Macs and OpenAI’s Chip Push | Bloomberg Tech 8/25/2026
- Rejected: Why 1 Chip Can Stop Cars? ​#Shorts #Semiconductor

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "ON Semi"]]`
- Rejected: Semiconductor Stocks Drop 20%: Should Investors Be Worried? | Weekly Market Update

### indie Semiconductor — ok_no_relevant_videos
Relevance groups: `[["indie Semiconductor", "INDI"]]`
- Rejected: Best Penny Stocks Under $4 to Buy Right Now (Day 4 Challenge)

### Copper stocks — ok_no_relevant_videos
Relevance groups: `[["copper", "铜", "銅"], ["stock", "stocks", "miner", "miners", "mining"]]`
- Rejected: 窮學生被大哥供養出國十年，歸鄉當天卻發現哥哥為搶救新娘，被仇人用電棍打到瀕死！他當場亮出無冕之王身份，一分鐘凍結煤老闆全部資產，再拿一百億元重查父母礦難
- Rejected: 穷小伙被女上司抢功羞辱踢出局，怎料项目离了他直接自毁，公司瞬间蒸发百亿！原来他竟是第一黑客，女总裁亲自上门高薪挖人，逆袭开启！ #短剧 #男频 #爽剧 #逆袭 | 我的功劳，你夺不走
- Rejected: 女孩回歸豪門卻被親生父母再一次拋棄，重生後她直接回到養父母家，憑借預知能力帶著全家發家致富！#family #face #drama #cute #逆襲 #親情 #都市
- Rejected: [FULL]玄门废柴少女被逼献祭神明，她却当场卸下伪装撕碎上古禁制，掀翻祭坛展露无敌实力，献祭大典让心机仇人跪地求饶【低調廢柴其實超神】
- Rejected: 最新爽文逆袭动漫来袭！穷小伙觉醒情报系统强势反杀各路强敌！剧情越看越上头，快来一起围观吧！ #修仙 #动漫

