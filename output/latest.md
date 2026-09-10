# YouTube Entity Enrichment

Generated: **2026-09-10T11:32:40.097226+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Oracle | Oracle ORCL earnings AI cloud | 16/34 | 47.1% | 41 | 27 | 0.0% | 80.0% | ok |
| 2 | GameStop | GameStop GME earnings | 21/50 | 42.0% | 435 | 339 | 22.2% | 70.0% | ok |
| 3 | AeroVironment | AeroVironment AVAV earnings defense drones | 7/11 | 63.6% | 178 | 118 | 16.7% | 85.7% | ok |
| 4 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 5 | Pinterest | Pinterest PINS earnings | 1/50 | 2.0% | 24 | 24 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Apple Siri AI | Apple AAPL Siri AI | 7/50 | 14.0% | 1550 | 93 | 25.0% | 57.1% | ok_low_relevance |
| 7 | Meta Muse AI | Meta META Muse AI agent | 43/50 | 86.0% | 869 | 245 | 37.0% | 50.0% | ok |
| 8 | Anthropic | Anthropic Claude AI | 46/50 | 92.0% | 1093 | 341 | 15.4% | 0.0% | ok |
| 9 | Apple AI | Apple AAPL AI | 13/50 | 26.0% | 5800 | 3722 | 75.0% | 20.0% | ok_low_relevance |
| 10 | TSMC | TSMC TSM revenue AI chips | 2/7 | 28.6% | 4 | 4 | 0.0% | 100.0% | ok_low_relevance |
| 11 | Tower Semiconductor | Tower Semiconductor TSEM stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 12 | Navitas Semiconductor | Navitas Semiconductor NVTS stock GaN | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 13 | Magnachip Semiconductor | Magnachip MX semiconductor stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 14 | onsemi | onsemi ON semiconductor stock | 1/2 | 50.0% | 2804 | 2804 | 100.0% | 100.0% | ok |
| 15 | Semiconductor stocks | semiconductor stocks AI chips | 4/50 | 8.0% | 50 | 19 | 0.0% | 75.0% | ok_low_relevance |
| 16 | Power semiconductors | power semiconductor stocks GaN SiC | 0/12 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 17 | Nuclear stocks | nuclear stocks uranium power AI data centers | 0/13 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 18 | Silver mining stocks | silver mining stocks | 4/50 | 8.0% | 5015 | 1243 | 66.7% | 75.0% | ok_low_relevance |
| 19 | Uranium stocks | uranium stocks nuclear fuel | 1/48 | 2.1% | 1095 | 1095 | 100.0% | 100.0% | ok_low_relevance |
| 20 | Astra AI | Astra AI model agent | 49/50 | 98.0% | 12002 | 5790 | 75.0% | 10.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Pinterest — ok_low_relevance
Relevance groups: `[["Pinterest", "PINS"], ["earnings", "results", "guidance"]]`
- Rejected: 🚨 Pinterest LOVES This Content (But It Pays Less)
- Rejected: This 2026 Pinterest Strategy Is Working For Me ($400+/Day)
- Rejected: How I Automate Pinterest Pins for Daily Free Organic Traffic & Passive Income
- Rejected: Pinterest + ChatGPT:  Online Earning ఎలా! | affiliate marketing 2026 | online earning Telugu
- Rejected: You Should Sell $27 Products On Pinterest

### Apple Siri AI — ok_low_relevance
Relevance groups: `[["Apple", "AAPL", "Siri"], ["AI", "Apple Intelligence", "Siri"]]`
- Rejected: Apple's First Foldable iPhone
- Rejected: AAPL Shows Off iPhone Duo, iPhone 18 & AirPods 5 at "Surprise and Shine" Event
- Rejected: Apple announces new foldable phone, the iPhone Duo
- Rejected: Apple Unveils New Products Under Ternus | Bloomberg Businessweek Daily 9/9/2026
- Rejected: Are you ready for Apple's new Foldable IPHONE?? 😳

### Apple AI — ok_low_relevance
Relevance groups: `[["Apple", "AAPL"], ["AI", "Apple Intelligence"]]`
- Rejected: The iPhone Duo is Here! Everything Announced at Apple's Event in 14 Minutes
- Rejected: Apple Event in 14 Minutes: Everything You Need to Know!
- Rejected: Apple Event September ’26: Recapping announcements of iPhone Duo, iPhone 18 Pro, and more
- Rejected: I Tested Apple's New FOLDABLE iPhone
- Rejected: This is the 'MOST IMPRESSIVE' Apple product introduction in YEARS, expert says

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "TSM", "台積電", "台积电"]]`
- Rejected: The AI Dividend Stock Behind Nvidia, Micron & AMD
- Rejected: Tom Lee: Do NOT Sell in September - Wall Street is WRONG About NVIDIA(Buy These 3 AI Stocks Now)
- Rejected: Look for Semis to Continue
- Rejected: SPCX变盘在即！#spcx #SpaceX股票 #spcx股票#美股#
- Rejected: 黄仁勋疯了？40万张GPU杀向AI！真正的“炸弹”才刚刚点燃？下一场暴涨，还是AI泡沫顶点？

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor stocks", "chip stocks", "半导体股", "半導體股"]]`
- Rejected: PRICING GAINS: Chip shortages benefiting major semiconductor companies
- Rejected: AI Stocks Lead, Blue Chips Lag In Down Session: AMD, Magnite, TVTX In Focus | Stock Market Today
- Rejected: Cathie Wood Just Bought $17 Million of This AI Chip Stock!🚨 #stockmarket #trading #ai #stocks
- Rejected: Nvidia is funding an AI boom. Will it trigger a financial crash? | The Economist
- Rejected: Micron SanDisk Just Won Apple's Biggest Event of the Year ($MU $SNDK $AAPL Stocks)

### Power semiconductors — ok_no_relevant_videos
Relevance groups: `[["power semiconductor", "power semiconductors", "功率 半導體", "GaN", "SiC"]]`
- Rejected: 【全集】丈夫葬禮當晚，所有人逼她交出百億家產，卻沒人知道這個看似柔弱的豪門遺孀，竟是隱藏多年的黑道女王！#aidrama #熱血 #逆襲 #Drama #AI真人#drama
- Rejected: All Ignored The Poor Girl's Cries For Help—Only A Waiter Saved Her,Who Was Secretly Billionaire CEO!
- Rejected: 🔴【FULL】开朗少女为父报仇嫁进豪门，冷酷少爷竟是她苦寻多年的旧爱！两人开启隐婚生活，一边斗嘴撒糖，一边偷偷调查，没想到真凶竟是身边人！
- Rejected: 【短劇全集】覺醒異能綁定消費系統後我越花錢越暴富，狂賺千億逆襲成女總裁，窮親戚上門搶家產被我直接甩黑卡轟出門，捐掉財產我狠狠打惡人臉【財富逆襲女王】
- Rejected: 賭場都以為他只是8歲小孩，誰知他竟是讓四大賭王臣服的賭神！天門十二絕技重現江湖，一路連贏到賭場破產！#短劇 #逆襲 #反轉 #爽劇 #重生 #奇幻

### Nuclear stocks — ok_no_relevant_videos
Relevance groups: `[["nuclear stocks", "nuclear power stocks", "核电股", "核能股"]]`
- Rejected: Uranium prices to beat all-time highs? (Live from #WorldNuclearSymposium)
- Rejected: The AI ETF Strategy: How to Invest Beyond NVIDIA
- Rejected: Coinbase CEO Predicts Bitcoin's Downturn Is Over
- Rejected: Apple's $2000+ iPhone, Oil Gain Stokes Inflation Fear | Bloomberg Businessweek Daily 9/8/2026
- Rejected: EP098 Oklo Stock: $3.6B From Shareholders, $25M From Customers

### Silver mining stocks — ok_low_relevance
Relevance groups: `[["silver mining stocks", "silver miners", "白银矿业股", "白銀礦業股"]]`
- Rejected: David Morgan: Gold to $5,000 by Year-End? Silver, Mining Stocks & Financial Reset
- Rejected: AYA.TO: 81.7% Silver Margin — The Moroccan Mine Nobody Is Talking About | MineStock Pro Deep Dive
- Rejected: Week in Review: China Buys Record Gold as Mining Stocks Surge | Gold, Silver & Mining Stocks
- Rejected: Stanley Druckenmiller: The Hidden Reason Gold & Silver Prices Are Surging Right Now
- Rejected: HUGE SILVER NEWS FROM TRUMP! IF YOU OWN SILVER, WATCH THIS NOW | SCOTT BESSENT

### Uranium stocks — ok_low_relevance
Relevance groups: `[["uranium stocks", "uranium miners", "铀矿股", "鈾礦股"]]`
- Rejected: Uranium prices to beat all-time highs? (Live from #WorldNuclearSymposium)
- Rejected: The Nuclear Renaissance: Why Uranium Is Becoming a Major Investment Theme Again
- Rejected: Top Nuclear Energy Stocks & Best Approach To Photonics Rich Off Gains Ep.44📈
- Rejected: Apple's $2000+ iPhone, Oil Gain Stokes Inflation Fear | Bloomberg Businessweek Daily 9/8/2026
- Rejected: 3 Stocks Under $20 To Buy Now

