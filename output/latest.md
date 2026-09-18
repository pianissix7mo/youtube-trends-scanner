# YouTube Entity Enrichment

Generated: **2026-09-18T11:40:00.751446+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | TypeSafe AI | typesafe ai | 10/50 | 20.0% | 3867 | 4374 | 77.8% | 90.0% | ok_low_relevance |
| 2 | Philadelphia Semiconductor / Cathay 00830 | 00830 國泰 費城 半導體 | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 3 | Dollarama | dollarama earnings | 6/16 | 37.5% | 53 | 53 | 16.7% | 100.0% | ok |
| 4 | India semiconductor buildout | india semiconductor | 3/50 | 6.0% | 18870 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 5 | Lennar | lennar earnings call | 19/39 | 48.7% | 23 | 22 | 0.0% | 90.0% | ok |
| 6 | Foxconn / Hon Hai | 鴻海 股票 | 12/50 | 24.0% | 940 | 86 | 0.0% | 20.0% | ok_low_relevance |
| 7 | Grab | grab 股票 | 6/50 | 12.0% | 1053 | 293 | 25.0% | 66.7% | ok_low_relevance |
| 8 | Oil / energy stocks | oil stocks today | 17/50 | 34.0% | 15843 | 1084 | 60.0% | 0.0% | ok |
| 9 | Apple / Siri AI | ios 27 siri ai | 50/50 | 100.0% | 14378 | 8004 | 92.9% | 10.0% | ok |
| 10 | Marvell Technology | mrvl earnings call | 7/12 | 58.3% | 6 | 6 | 0.0% | 100.0% | ok |
| 11 | Tesla | tsla earnings call | 35/50 | 70.0% | 427 | 9 | 16.7% | 30.0% | ok |
| 12 | Semiconductor stocks | semiconductor stocks | 12/50 | 24.0% | 341 | 73 | 25.0% | 60.0% | ok_low_relevance |
| 13 | Uber | uber eats earnings | 29/50 | 58.0% | 502 | 399 | 32.0% | 70.0% | ok |
| 14 | NVIDIA | nvda earnings call | 17/38 | 44.7% | 2 | 2 | 11.8% | 100.0% | ok |
| 15 | Amazon | amzn earnings call | 7/50 | 14.0% | 87 | 24 | 0.0% | 57.1% | ok_low_relevance |
| 16 | Hugging Face / AI incident | ai hugging face incident | 28/50 | 56.0% | 100 | 76 | 4.0% | 70.0% | ok |
| 17 | Alphabet / Google | googl earnings call | 12/50 | 24.0% | 96 | 33 | 10.0% | 80.0% | ok_low_relevance |
| 18 | Berkshire Hathaway / Warren Buffett | warren buffett | 37/50 | 74.0% | 116 | 70 | 17.9% | 50.0% | ok |
| 19 | Navitas Semiconductor | navitas semiconductor stock | 4/6 | 66.7% | 35 | 35 | 0.0% | 100.0% | ok |
| 20 | Strait of Hormuz / oil | strait of hormuz news | 39/50 | 78.0% | 7249 | 179 | 33.3% | 0.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### TypeSafe AI — ok_low_relevance
Relevance groups: `[["TypeSafe AI"]]`
- Rejected: Jev From TypeSafe is a New Class of AI Model that is FAST and CHEAP - But There is a Caveat!
- Rejected: wtf is jev?
- Rejected: Is Jev What AI Has Been Missing? I Tested It.
- Rejected: Jev: The New AI Model That's Breaking The Internet (Full Tutorial)
- Rejected: JEV Breakdown: The First AI Model Built For Code

### Philadelphia Semiconductor / Cathay 00830 — ok_no_relevant_videos
Relevance groups: `[["00830", "費城半導體", "Philadelphia Semiconductor"]]`
- Rejected: 【錢線百分百】20260916完整版(下集)《全球資金偷偷換車 海外ETF"4大新寵"竄出! 法案卡關Coinbase重挫 資金瘋逃黃金.原油?》│非凡財經新聞│
- Rejected: 《全球資金偷偷換車 海外ETF"4大新寵"竄出!》【錢線百分百】20260916-9│非凡財經新聞│

### India semiconductor buildout — ok_low_relevance
Relevance groups: `[["India semiconductor", "India chip"]]`
- Rejected: SEMICON India 2026 | Day 1 | Silicon to Systems: Building the Ecosystem
- Rejected: SEMICON India 2026 begins: India’s semiconductor ambitions on global stage
- Rejected: India's Semiconductor Push Enters a New Phase | Ashwini Vaishnaw at SEMICON India 2026
- Rejected: PM Modi Inaugurates SEMICON India’ 26, Showcasing India’s Semiconductor Ambitions
- Rejected: SEMICON India 2026 | How India Is Building A Global Chip Hub | India’s Semiconductor Rise | Modi |4K

### Foxconn / Hon Hai — ok_low_relevance
Relevance groups: `[["鴻海", "Foxconn", "Hon Hai"]]`
- Rejected: 配息破紀錄，是陷阱? 0050、00878、0056、00919 台股反彈逼近套牢區！巨無霸ETF配息創高，盲點不可不知，美股、台積電、輝達、聯電、友達、中石化、財經趨勢 09/18/26【宏爺講股
- Rejected: AI三巨頭喊剎車？散戶該賣股嗎？ 台積電攜手ASML升級EUV 家登、帆宣、辛耘吃香 機器人股首選它《鈔錢部署》盧燕俐 ft.蔡明翰 20260915
- Rejected: 【⚠️注意】華邦電.力積電.國巨.禾伸堂.南亞.欣興.緯創.聯發科  2026.09.18(有CC字幕)
- Rejected: 【又四萬七 這次狼來了?】2026/9/18 哲哲只有60秒 #shorts
- Rejected: 【❌NO】Fed升息後大漲不是你想的那樣明天絕對不要…… 2026.09.17(有CC字幕)

### Grab — ok_low_relevance
Relevance groups: `[["Grab"]]`
- Rejected: 現在的「它」像極了當時的AMD：人人喊打但我先加碼！我發瘋了嗎...？
- Rejected: Interesting News for Uber Stock Investors!
- Rejected: 【Rwei直播】費半站不回去？台股站上月線卻開高走低！不是升息嗎？怎麼風平浪靜！🧐｜2026/09/17
- Rejected: THIS MAKES INVESTING EASY TO UNDERSTAND
- Rejected: 高利貸搶窮小子老婆孩子還要砍他手！他一通電話讓對方跪地喊爺——轉頭股市對賭贏走仇人一條胳膊！第2集 YT #熱播短劇 #重生 #爽劇 BG

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor stocks", "chip stocks", "SOXX", "SMH"]]`
- Rejected: I just bought THIS Semiconductor Stock
- Rejected: The AI Dip Is a Gift (2 Stocks I'm Buying)
- Rejected: ON Semiconductor CEO Hassane El-Khoury: Compute will be at the center of everything we do
- Rejected: NVTS Stock 2027: Can Navitas Semiconductor Become a Massive AI Power Stock?
- Rejected: AMD Micron SanDisk Stocks! The Copper Crisis That Could Hit Them ($AMD $MU $SNDK)

### Amazon — ok_low_relevance
Relevance groups: `[["Amazon", "AMZN"]]`
- Rejected: The AI Correction Is Here: These Stocks Are On My Buy List
- Rejected: The Call That Doomed Hewlett-Packard
- Rejected: 3 Stocks We're Buying If They Dip Again Before Year End!
- Rejected: Stocks Rally as Yields Fall After the Fed Rate Hike
- Rejected: Rate HIKE Cycle Started.. What It Means for Your STOCKS

### Alphabet / Google — ok_low_relevance
Relevance groups: `[["Alphabet", "Google", "GOOGL"]]`
- Rejected: The AI Correction Is Here: These Stocks Are On My Buy List
- Rejected: The K-Shaped Economy Is About to Get More Real
- Rejected: Tempsens Instruments (India) Earnings Call for Q1FY27
- Rejected: Capture holiday peak demand | Rethink Retail 2026 (full keynote)
- Rejected: One Day Before the Fed: Financials Rolling Over, Energy Won't Quit

