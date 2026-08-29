# YouTube Entity Enrichment

Generated: **2026-08-29T12:19:23.338424+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NVIDIA earnings | NVIDIA NVDA earnings 财报 輝達 | 13/24 | 54.2% | 82 | 41 | 10.0% | 70.0% | ok |
| 2 | IREN earnings | IREN stock earnings | 17/50 | 34.0% | 3196 | 657 | 44.4% | 30.0% | ok |
| 3 | Salesforce earnings | Salesforce CRM earnings | 18/50 | 36.0% | 598 | 146 | 12.5% | 10.0% | ok |
| 4 | Marvell earnings | Marvell MRVL earnings 財報 | 2/10 | 20.0% | 619 | 135 | 0.0% | 50.0% | ok_low_relevance |
| 5 | Workday earnings | Workday WDAY earnings | 9/26 | 34.6% | 26 | 8 | 0.0% | 66.7% | ok |
| 6 | Okta earnings | Okta OKTA earnings | 15/50 | 30.0% | 312 | 31 | 8.3% | 70.0% | ok |
| 7 | CrowdStrike earnings | CrowdStrike CRWD earnings | 21/50 | 42.0% | 122 | 63 | 6.7% | 40.0% | ok |
| 8 | Royal Bank earnings | RBC RY earnings Canadian banks | 2/4 | 50.0% | 19 | 19 | 0.0% | 100.0% | ok |
| 9 | Sunrise / Sino-American Silicon semiconductor | 昇陽半導體 8028 stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 10 | Memory stocks | memory stocks DRAM HBM 記憶體 股票 | 7/14 | 50.0% | 2211 | 886 | 50.0% | 57.1% | ok |
| 11 | Gold & silver miners | gold silver mining stocks miners | 7/50 | 14.0% | 1159 | 1159 | 60.0% | 71.4% | ok_low_relevance |
| 12 | iShares Semiconductor ETF | iShares Semiconductor ETF SOXX | 1/5 | 20.0% | 1011 | 1011 | 100.0% | 100.0% | ok_low_relevance |
| 13 | Utility stocks | utility stocks power AI data centers | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 14 | Semiconductor tariffs | semiconductor tariffs Trump chip tariffs 半導體 關稅 | 2/17 | 11.8% | 33 | 33 | 0.0% | 100.0% | ok_low_relevance |
| 15 | Rocket Lab | Rocket Lab RKLB stock | 24/40 | 60.0% | 68 | 57 | 9.1% | 80.0% | ok |
| 16 | MSI | MSI 微星 stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 17 | Nanya Technology | Nanya Technology 南亞科技 stock memory | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 18 | TSMC | TSMC TSM Taiwan Semiconductor 台積電 | 3/4 | 75.0% | 433 | 433 | 0.0% | 100.0% | ok |
| 19 | Uranium stocks | uranium stocks Cameco CCJ UUUU | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 20 | PharmaEssentia | PharmaEssentia 藥華藥 stock FDA | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Marvell earnings — ok_low_relevance
Relevance groups: `[["Marvell", "MRVL"], ["earnings", "earnings call", "財報", "财报"]]`
- Rejected: 2026/08/28(五) 輝達能撐住AI股嗎？軟體股大反彈 #CRM #CRWD #MRVL
- Rejected: Marvell FY2027 Q2：AI 互联开始兑现，定制 ASIC 仍待收入验证
- Rejected: Marvell營收暴增46%，定制芯片開始搶走哪塊市場？
- Rejected: NVDA, MRVL, CRWD — Conversion before exposure | Morning Market Brief 2026-08-28
- Rejected: 秃瓢盘前 | #gap 盘前大涨15% | #pypl 盘前重挫14% | #mrvl 绩后大跌 | Kevin Warsh 美东十点讲话

### Gold & silver miners — ok_low_relevance
Relevance groups: `[["gold", "silver"], ["mining stocks", "miners", "mining"]]`
- Rejected: SILVER Stocks Set to Go Berserk - 'These Companies Are Printing Cash': John Feneck
- Rejected: SILVER Price ALERT!🚨 3 Big Names Said THIS! 🦍🦍 You Best Hear It - (Gold too)
- Rejected: METALS INVESTOR! 📈 Market Reality: 5 Reasons Not to Worry About Friday's Price Slam - Gold & Silver
- Rejected: Gold Just Broke the 200-Day — Don't Panic Yet
- Rejected: FLORIAN GRUMMES | the miners are now in a period where every pullback is a buying opportunity!

### iShares Semiconductor ETF — ok_low_relevance
Relevance groups: `[["iShares Semiconductor", "SOXX", "semiconductor ETF", "chip ETF"]]`
- Rejected: 🚨 Trade Alert: Direxion Daily Semiconductor Bull 3X Shares (SOXL)
- Rejected: The AI Bubble Is Cracking – While "Boring" Businesses Are Quietly Printing Cash
- Rejected: กองทุนหุ้นชิปเอไอ กองนี้ KKP SEMICON-H เกียรตินาคิน เป็นไง?
- Rejected: SOXL 원금 되찾으려면 171%가 올라야 합니다 #SOXL #서학개미 #레버리지ETF #3배레버리지 #반도체ETF #디렉시온 #미국주식 #ETF투자 #변동성손실

### Utility stocks — ok_no_relevant_videos
Relevance groups: `[["utility stocks", "utilities", "power stocks"], ["AI", "data center", "rates"]]`
- Rejected: AI Factory Ep.2.3: $1.4 Trillion Power Grid Boom - Which AI Stock Wins?
- Rejected: AI Singularity Is Here: AI Infra, $100K Bets, & The 10-Year Supercycle 🚀
- Rejected: The Bridge Ep. 19: The Boring Way to Invest in AI
- Rejected: Tech Stocks Gain on AI Optimism as Nvidia Jumps | The Pulse 8/27/2026
- Rejected: Nvidia’s AI Boom, Salesforce’s Anthropic Bet | Bloomberg Tech 8/27/2026

### Semiconductor tariffs — ok_low_relevance
Relevance groups: `[["semiconductor", "chip", "半導體", "半导体"], ["tariff", "tariffs", "關稅", "关税"]]`
- Rejected: 台灣當心! 川普關稅不只揮晶片 筆電.伺服器恐遭殃美加貿易戰升溫 川普再出招! 安大略湖變"美國湖"｜三立財經iNEWS
- Rejected: 【美洲速報】川普政府擬徵新晶片關稅　筆電、遊戲機恐中招｜#鏡新聞
- Rejected: 台灣靠AI.半導體「首度超越中國」躍居新加坡最大貿易夥伴！？欣興電子涉洗產地「中國製變MIT」觸怒老美雷區？！【關鍵時刻】每日懶人包 20260828
- Rejected: 美農民40年來最慘危機！630億美元蒸發、中國抽走大豆、加拿大卡住化肥！中印俄抱團反擊！川普打中、制印、封俄 反逼三國聯手【#環球大戰線】20260826-完整版 葉思敏 侯漢廷 苑舉正 彭華幹
- Rejected: 트럼프 반도체 관세 폭탄, 한국에 직격탄일까? #반도체 #관세 #트럼프

### Nanya Technology — ok_no_relevant_videos
Relevance groups: `[["Nanya Technology", "南亞", "南亞科", "南亞科技"], ["memory", "DRAM"]]`
- Rejected: 南亞科被動買盤來了！但真正的考驗不是 MSCI
- Rejected: 巨無霸咖哩飯台灣最速完食紀錄🔥來評評理!咖哩要拌還是不要拌?｜【小慧就愛吃  シャオホイ】大食い｜food challenge｜mukbang｜먹방｜eating show

