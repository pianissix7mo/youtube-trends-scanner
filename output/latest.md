# YouTube Entity Enrichment

Generated: **2026-09-12T11:31:33.293509+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Oracle | Oracle ORCL earnings AI cloud | 38/50 | 76.0% | 56 | 21 | 3.6% | 0.0% | ok |
| 2 | TSMC | TSMC TSM earnings AI chips | 11/15 | 73.3% | 18 | 12 | 0.0% | 90.0% | ok |
| 3 | Adobe | Adobe ADBE earnings AI | 27/50 | 54.0% | 59 | 47 | 14.3% | 40.0% | ok |
| 4 | AeroVironment | AeroVironment AVAV earnings defense drones | 7/19 | 36.8% | 37 | 36 | 0.0% | 85.7% | ok |
| 5 | Broadcom | Broadcom AVGO earnings AI chips | 6/18 | 33.3% | 15 | 15 | 0.0% | 100.0% | ok |
| 6 | Micron | Micron MU earnings HBM memory | 7/25 | 28.0% | 68 | 44 | 16.7% | 85.7% | ok_low_relevance |
| 7 | Marvell Technology | Marvell MRVL earnings AI networking | 1/5 | 20.0% | 5 | 5 | 0.0% | 100.0% | ok_low_relevance |
| 8 | Copart | Copart CPRT earnings ACV acquisition | 5/7 | 71.4% | 36 | 36 | 0.0% | 100.0% | ok |
| 9 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 10 | Apple Siri AI | Apple AAPL Siri AI | 14/50 | 28.0% | 4108 | 1195 | 50.0% | 10.0% | ok_low_relevance |
| 11 | Anthropic | Anthropic Claude AI IPO Nvidia | 19/40 | 47.5% | 6 | 6 | 5.3% | 100.0% | ok |
| 12 | OpenAI | OpenAI ChatGPT AI | 41/50 | 82.0% | 4972 | 1640 | 68.2% | 10.0% | ok |
| 13 | Meta Muse AI | Meta META Muse AI | 41/50 | 82.0% | 371 | 54 | 14.3% | 10.0% | ok |
| 14 | Semiconductor supply chain | semiconductor supply chain AI chips | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | Taiwan PCB / AI hardware supply chain | Taiwan PCB AI server supply chain | 0/6 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 16 | Gigabyte Technology | Gigabyte 2376 AI server stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 17 | onsemi | onsemi ON semiconductor stock | 3/3 | 100.0% | 31 | 31 | 0.0% | 100.0% | ok |
| 18 | Navitas Semiconductor | Navitas Semiconductor NVTS GaN stock | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 19 | Magnachip Semiconductor | Magnachip Semiconductor MX stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 20 | Uranium / nuclear energy stocks | uranium nuclear energy stocks AI data centers | 1/26 | 3.8% | 298 | 298 | 0.0% | 100.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Micron — ok_low_relevance
Relevance groups: `[["Micron", "MU", "美光"], ["earnings", "HBM", "memory", "DRAM", "财报", "財報"]]`
- Rejected: Micron Stock Is Going to a New All-Time High
- Rejected: MU - 09 - Upcoming Catalysts Like HBM4 and Nvidia's Blackwell Could Skyrocket Micron's Growth #MU
- Rejected: Memory Stocks Fell, But The Fundamentals Just Got More Interesting!
- Rejected: MU - 08 - The Risks Micron Faces Consumer Cycles, Capex, Geopolitics, and Fierce Competition #micron
- Rejected: The Only Level That Matters for Micron Right Now

### Marvell Technology — ok_low_relevance
Relevance groups: `[["Marvell", "MRVL"], ["earnings", "AI", "networking", "custom silicon"]]`
- Rejected: Marvell Technology looks very attractive #Marvell #MRVL #Semiconductors #AIInfrastructure #Investing
- Rejected: Broadcom Stock (AVGO) EXPLODES! $230B AI Revenue Roadmap & Custom Chips — BUY NOW?
- Rejected: Top Stocks- AMD, Tesla, Marvell Technology #stocks #AMD #Tesla #MRVL
- Rejected: I’m buying these 5 AI stocks for the next 20 days

### Apple Siri AI — ok_low_relevance
Relevance groups: `[["Apple", "AAPL", "Siri"], ["AI", "Apple Intelligence", "Siri"]]`
- Rejected: Introducing the new iPhone Duo
- Rejected: Apple unveils new foldable iPhone Duo priced at $1,999
- Rejected: iPhone Duo: Everything announced about the first foldable iPhone
- Rejected: The TRUTH About Apple's HUGE iPhone Event... Good & BAD!
- Rejected: Introducing the new iPhone 18 Pro

### Semiconductor supply chain — ok_no_relevant_videos
Relevance groups: `[["semiconductor supply chain", "semiconductor manufacturing", "半導體製程", "半导体制造"]]`
- Rejected: Why Can’t Nvidia Get Enough AI Chips?
- Rejected: HBM Memory Will Eat 30% of DRAM Wafers — Your DDR5 Pays for It
- Rejected: Wolfspeed Cut SiC On-Resistance 27% — But There's a Catch
- Rejected: OpenAI Deepens Samsung Partnership on Next-Generation AI Chips
- Rejected: The Rock Behind the World’s Most Advanced Chips

### Taiwan PCB / AI hardware supply chain — ok_no_relevant_videos
Relevance groups: `[["PCB", "printed circuit board", "印刷電路板", "電路板"], ["AI", "server", "伺服器", "服务器"]]`
- Rejected: 你的持股在裸泳嗎?白宮《大轉運詐騙》台灣列洗產地Tier1！剖析台廠跨國分工產地純度認定轉運風險 ft.台經中心執行長 吳大任【#市場觀測站Podcast EP190】CC字幕 @cteevideo​
- Rejected: 【精選】蘋果折疊機 iPhone 18 Duo 規格大洗牌！台積電2奈米降維打擊！「左手吃AI右手吃蘋果」秒殺空頭？《寶傑點兵》 劉寶傑
- Rejected: 台灣PCB鏈產值1.3兆估年增25%"明年更看好"！ 載板4雄拚追上供需 找第二供應商衝刺營運動能｜非凡財經新聞｜20260911
- Rejected: 【全集】「蘋果新機、台積電8月營收、美CPI」引爆台股觀望潮？ - 黃世聰 蘇威元 林友銘 王榮旭 劉寶傑《寶傑點兵》2026.09.09
- Rejected: 大立光變第一大持股！00410A如何布局光通訊、散熱與AI伺服器？｜家裡隨便聊

### Navitas Semiconductor — ok_no_relevant_videos
Relevance groups: `[["Navitas Semiconductor", "Navitas", "NVTS"], ["GaN", "power semiconductor", "power chip"]]`
- Rejected: NVTS Stock Before 2027: BUY, HOLD or AVOID? | Navitas Semiconductor Stock Prediction
- Rejected: 别只盯着GPU！这只被严重低估的AI芯片股，正迎来十倍重构点？｜深度拆解第三代半导体黑马 Navitas 的千亿算力逻辑

### Uranium / nuclear energy stocks — ok_low_relevance
Relevance groups: `[["uranium stocks", "uranium miners", "nuclear energy stocks", "铀矿股", "鈾礦股"]]`
- Rejected: Big uranium supply deficit incoming (Live from #WorldNuclearSymposium)
- Rejected: Uranium prices to beat all-time highs? (Live from #WorldNuclearSymposium)
- Rejected: Uranium supply deficit is structural (Live from #WorldNuclearSymposium)
- Rejected: #Uranium prices at turning point (Live from #WorldNuclearSymposium)
- Rejected: Uranium in Namibia (Live from #WorldNuclearSymposium)

