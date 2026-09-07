# YouTube Entity Enrichment

Generated: **2026-09-07T11:39:38.820685+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Tower Semiconductor | Tower Semiconductor TSEM stock | 1/1 | 100.0% | 11 | 11 | 0.0% | 100.0% | ok |
| 2 | Pinterest | Pinterest PINS earnings | 1/50 | 2.0% | 5 | 5 | 0.0% | 100.0% | ok_low_relevance |
| 3 | OpenAI Astra | OpenAI Astra AI model | 49/50 | 98.0% | 12836 | 10411 | 80.0% | 0.0% | ok |
| 4 | China financial-sector recapitalization | China $54 billion banks insurers recapitalization stocks | 0/4 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 5 | Tesla | Tesla TSLA stock Cybercab | 44/50 | 88.0% | 2193 | 69 | 22.2% | 0.0% | ok |
| 6 | Amazon | Amazon AMZN earnings | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 7 | DoorDash | DoorDash DASH earnings | 2/21 | 9.5% | 43 | 43 | 0.0% | 100.0% | ok_low_relevance |
| 8 | Lululemon | Lululemon LULU earnings guidance | 11/44 | 25.0% | 11 | 7 | 0.0% | 80.0% | ok_low_relevance |
| 9 | Canada-U.S. trade war / retaliatory tariffs | Canada US retaliatory tariffs trade war | 12/50 | 24.0% | 1237 | 192 | 20.0% | 30.0% | ok_low_relevance |
| 10 | SEMICON Taiwan 2026 | SEMICON Taiwan 2026 semiconductor | 7/50 | 14.0% | 680 | 74 | 25.0% | 57.1% | ok_low_relevance |
| 11 | Semiconductor ETFs | SMH SOXX semiconductor ETF | 1/6 | 16.7% | 32 | 32 | 0.0% | 100.0% | ok_low_relevance |
| 12 | TSMC | TSMC TSM Taiwan Semiconductor | 8/11 | 72.7% | 16 | 16 | 0.0% | 100.0% | ok |
| 13 | ON Semiconductor | ON Semiconductor onsemi ON stock | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 14 | Navitas Semiconductor | Navitas NVTS semiconductor stock | 8/9 | 88.9% | 35 | 35 | 0.0% | 100.0% | ok |
| 15 | Magnachip Semiconductor | Magnachip MX semiconductor stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 16 | Valens Semiconductor | Valens Semiconductor VLN stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 17 | Robinhood | Robinhood HOOD stock | 35/50 | 70.0% | 184 | 54 | 29.2% | 40.0% | ok |
| 18 | NVIDIA | NVIDIA NVDA earnings AI chips | 7/50 | 14.0% | 92 | 63 | 0.0% | 85.7% | ok_low_relevance |
| 19 | Power semiconductors | power semiconductor stocks GaN SiC | 0/8 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 20 | Anthropic / Claude | Anthropic Claude AI | 45/50 | 90.0% | 110 | 99 | 15.0% | 70.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Pinterest — ok_low_relevance
Relevance groups: `[["Pinterest", "PINS"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: Walmart Affiliate Program: How to Join & Create Pinterest Pins That Sell with AI
- Rejected: How I Earn Selling Digital Products On Pinterest in 2026 (HOW TO START NOW)
- Rejected: How I Built My Pinterest Digital Product Funnel in 2 Hours (No Website, No Followers)
- Rejected: The Pinterest Affiliate Marketing Strategy That Actually Works in 2026
- Rejected: Get Paid to Manage Pinterest 💰 | Earn $500–$3,000 Per Client | Day 74 of 100

### China financial-sector recapitalization — ok_no_relevant_videos
Relevance groups: `[["China", "中国", "中國"], ["bank", "banks", "insurer", "insurance", "recapitalization", "capital injection", "银行", "銀行", "保险", "保險"]]`
- Rejected: Investors Turn to Emerging Market Debt Amid Yield Volatility | Insight with Haslinda Amin 9/7/2026
- Rejected: Iran, US Trade Tanker Attacks, Strong US Payrolls Fuel Fed Hike Bets | The Asia Trade 9/7/2026
- Rejected: China का SMART कदम⚠️$54 Billion बचाएगा अपने डूबते बैंक और इंश्योरेंस कंपनियां | Global Shock #stock
- Rejected: German Far Right Surges in Vote, Iran & US Trade Tanker Attacks | The Opening Trade 9/7/2026

### Amazon — ok_no_relevant_videos
Relevance groups: `[["Amazon", "AMZN"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: Amazon Stock Technical Analysis: Breakout or Rejection? | AMZN 📈 #trading
- Rejected: There Is NO Reason You Shouldnt Be Making Money On Amazon In 2026 Selling Books/CDs/DVDs! #go2lister
- Rejected: Understanding Amazon Com’s Balance Sheet #AMZN (period: 2026-06-30)
- Rejected: AMZN Stock Analysis: 30 Red Flags
- Rejected: How Much Income Can You Make w a Cybercab

### DoorDash — ok_low_relevance
Relevance groups: `[["DoorDash", "DASH"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: How Much I Made Doing DoorDash #doordash #sidehustle #makemoneyonline
- Rejected: Shmoney Talk✨ Want to Make Shmoney With DoorDash? 💵 Here’s How to Start!🦋
- Rejected: DoorDash Just Invited Customers to Become Your Competition
- Rejected: 16 | Dashing My Way To Retirement
- Rejected: Would You Take It?

### Lululemon — ok_low_relevance
Relevance groups: `[["Lululemon", "LULU"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: Lululemon Stock Just Collapsed—Is It Finally Cheap Enough?
- Rejected: Lululemon Athletica (LULU): 🍋 The Fallen Athleisure Titan & Michael Burry's Sub-100-Dollar Dip Buy
- Rejected: DISASTER FOR LULULEMON! Or Buying Opportunity?🚨
- Rejected: Lululemon Stock: Buy the Dip or Catch a Falling Knife?
- Rejected: Semis Break Out, NVIDIA Eyes New Highs, Lululemon Craters

### Canada-U.S. trade war / retaliatory tariffs — ok_low_relevance
Relevance groups: `[["Canada", "Canadian", "加拿大"], ["US", "U.S.", "United States", "美国", "美國"], ["tariff", "tariffs", "trade war", "关税", "關稅"]]`
- Rejected: Canada readies $28B in tariffs | CTV News Ottawa at Six for September 6, 2026
- Rejected: U.S Might Not be Ready for Canada's Retaliatory Tariffs Strategy | U.S-Canada Trade War | N18G | 4K
- Rejected: The $459 Billion Secret: Canada’s Hidden Weapon in the Trade War
- Rejected: Majority of Canadians Back Retaliatory Tariffs Against U.S. Trade War Poll | DWS News | AF14
- Rejected: Canada To Lose 90,000 Jobs From Trade War: Brace For 'Economic Pain' | Trevor Tombe

### SEMICON Taiwan 2026 — ok_low_relevance
Relevance groups: `[["SEMICON Taiwan", "2026 半導體 展", "台灣 半導體 展", "國際 半導體 展", "台湾半导体展", "国际半导体展"]]`
- Rejected: 直擊2026國際半導體展，揭密AI真正贏家，CPO、先進封裝爆發，拆解AI浪潮關鍵產業升級趨勢！鎖定投資最錢線。
- Rejected: Arizona courts Taiwan tech firms beyond semiconductors #晶片 #半導合作
- Rejected: Memory on Top of the GPU: Samsung’s zHBM Vision
- Rejected: How Taiwan built a chip city  #business
- Rejected: 那些年的噩夢都瞬間回來了，沉浸式的Dream Fab無塵室體驗【2026國際半導體展系列專題#1】 #國際半導體展 #Semicontaiwan #semiconductor

### Semiconductor ETFs — ok_low_relevance
Relevance groups: `[["SMH", "SOXX", "semiconductor ETF", "半导体 ETF", "半導體 ETF"]]`
- Rejected: SEME ETF: The Global Semiconductor Fund Most American Investors Have Never Heard Of
- Rejected: Korea’s Market Is Being Held Up by Buybacks !?!
- Rejected: Holanda saca su oro de EE.UU., Dell explota con servidores de IA y Uber apuesta a robotaxis
- Rejected: DRAM: O PRIMEIRO ETF DE MEMÓRIA CRIADO PARA A ERA DA IA
- Rejected: 162,000 Jobs. The Long Bond Didn't Buy the Boom. | September 4

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: China Pours Billions Into Mega Banks and Insurers | The China Show | 9/7/2026

### NVIDIA — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: Nvidia's $30 Billion AI Bet: 3 Stocks to Buy Before Wall Street Catches On
- Rejected: NVIDIA DEMAND: Buyers are SNAPPING UP its chips, market expert says
- Rejected: NVIDIA Just Made a MASSIVE AI Bet — NVDA Investors Need to See This
- Rejected: The Big 3: AAPL, NVDA, CVX
- Rejected: NVDA Stock: $13B Hugging Face Deal — What Happens Next?

### Power semiconductors — ok_no_relevant_videos
Relevance groups: `[["power semiconductor", "power semiconductors", "功率 半導體", "功率半导体", "GaN", "SiC"]]`
- Rejected: NVTS Stock: The AI Power Revolution Is Just Beginning
- Rejected: [주식추천] 실리콘 시대 끝납니다ㅣ차세대 전력반도체 대장주 3선
- Rejected: 【短劇全集】說好只做兩年隱婚夫妻，她卻被便宜老公越寵越心動，全然不知他竟是隱藏總裁！消失五年她帶娃歸來，男人紅著眼求婚：老婆孩子，這次都別走！【今我來思】
- Rejected: 美女總裁車內舊疾突發，混混圍車砸窗，窮小子路過一針救命，再反手將數十混混全放倒，女主醒後倒貼求嫁！
- Rejected: 【FULL】I Hid My Billionaire Identity as a Blacksmith… Until My Wife Chose Money Over Me😈

