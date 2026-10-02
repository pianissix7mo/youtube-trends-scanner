# YouTube Entity Enrichment

Generated: **2026-10-02T12:08:27.834977+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Micron Technology | Micron MU earnings AI memory | 39/50 | 78.0% | 4296 | 408 | 45.8% | 40.0% | ok |
| 2 | OpenAI DevDay / Dots | OpenAI DevDay Dots AI | 48/50 | 96.0% | 3262 | 709 | 34.6% | 10.0% | ok |
| 3 | Nike | Nike NKE earnings outlook | 20/50 | 40.0% | 614 | 178 | 15.4% | 40.0% | ok |
| 4 | Marvell Technology | Marvell MRVL stock AI chips | 4/29 | 13.8% | 24 | 24 | 0.0% | 100.0% | ok_low_relevance |
| 5 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 9/20 | 45.0% | 36 | 35 | 0.0% | 88.9% | ok |
| 6 | ON Semiconductor | ON Semiconductor ON stock Synaptics | 6/14 | 42.9% | 6 | 6 | 0.0% | 100.0% | ok |
| 7 | TSMC | TSMC TSM Taiwan Semiconductor | 24/31 | 77.4% | 14 | 11 | 0.0% | 90.0% | ok |
| 8 | NIO | NIO earnings stock | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Foxconn / Hon Hai | Foxconn Hon Hai 鴻海 AI servers stock | 1/1 | 100.0% | 912 | 0 | 0.0% | 0.0% | ok |
| 10 | Robinhood | Robinhood HOOD stock | 43/50 | 86.0% | 207 | 66 | 10.7% | 20.0% | ok |
| 11 | Uranium stocks | uranium stocks CCJ UEC nuclear | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 12 | Gold and silver mining stocks | gold silver mining stocks GDX SIL | 1/3 | 33.3% | 1 | 1 | 0.0% | 100.0% | ok |
| 13 | Space stocks | space stocks RKLB ASTS LUNR | 1/2 | 50.0% | 3464 | 0 | 0.0% | 0.0% | ok |
| 14 | Chinese stocks | Chinese stocks BABA JD PDD NIO | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 15 | Optical communications / CPO | optical communications CPO AI data center stocks | 2/12 | 16.7% | 113 | 43 | 0.0% | 50.0% | ok_low_relevance |
| 16 | Power semiconductors | power semiconductor SiC GaN stocks | 2/10 | 20.0% | 253 | 51 | 0.0% | 50.0% | ok_low_relevance |
| 17 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 18 | Apple Siri AI | Apple Siri AI AAPL | 24/50 | 48.0% | 282 | 100 | 27.8% | 50.0% | ok |
| 19 | Tokenized stocks | tokenized stocks Robinhood crypto equities | 4/50 | 8.0% | 185 | 185 | 25.0% | 100.0% | ok_low_relevance |
| 20 | Semiconductor market / foundry manufacturing | semiconductor market foundry manufacturing TSMC Intel | 2/27 | 7.4% | 17 | 17 | 0.0% | 100.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Marvell Technology — ok_low_relevance
Relevance groups: `[["Marvell", "MRVL"], ["AI", "chip", "semiconductor", "data center", "custom silicon"]]`
- Rejected: NVIDIA has put billions behind these companies, all positioned in the same AI supply chain: 1
- Rejected: "Worse Than Anything We've Ever Seen" - The Boomer Sell-Off Is Coming | Dave Collum
- Rejected: AI Buildout Powers On Despite Safety Concerns
- Rejected: NVIDIA Is Fighting a 5.26% 10-Year—Who Wins? | Daily Read #32
- Rejected: China's Mortgage Subsidy Plan Fails to Impress

### NIO — ok_no_relevant_videos
Relevance groups: `[["NIO", "蔚來", "蔚来"], ["earnings", "results", "guidance"]]`
- Rejected: NIO's Biggest Opportunity! NIO STOCK ANALYSIS TODAY BUY OR SELL PRICE PREDICTION KEY LEVELS TO WATCH
- Rejected: NIO Stock Crashes on Geely News - Is $3.38 the Bottom?🔋
- Rejected: NIO Stock: Is the Geely Deal a Win for Shareholders?
- Rejected: The PULLBACK!!! Fractal Tracking: AMC / BB / MRNA / NIO / RIOT
- Rejected: NIO Weekly Recap Sep 27, 2026 — Stock Drops -1.1% This Week

### Uranium stocks — ok_no_relevant_videos
Relevance groups: `[["uranium", "nuclear"], ["stock", "stocks", "CCJ", "UEC", "URA"]]`
- Rejected: AI & Market News: Amazon-Synopsys $1B Deal, NVIDIA, Palantir, Nuclear, Google & More

### Optical communications / CPO — ok_low_relevance
Relevance groups: `[["optical", "光通訊", "CPO", "silicon photonics", "矽光子"]]`
- Rejected: [광통신섹터 주가전망] 반도체 슈퍼사이클, 여러번 말씀 드렸습니다. 마지막 피날레! 결국 올 수 밖에 없다. 오늘부터 다시 움직이기 시작한 '이유' 를 알자.
- Rejected: [성호전자 주가전망] 광통신주 11% 급등, AI 데이터센터 수혜 더 이어질까?
- Rejected: [주식추천] 엔비디아가 광통신 10조 투자하고 미친듯이 사모으는 MLCC '이 기업' MLCC로 광통신 병목 해결한다! #광통신 #광통신관련주 #mlcc관련주 #주식추천
- Rejected: “마이크론이 또 돈을 풉니다” 반도체 장비주, 더 갈 이유 l 김지운 l 정경민 l 박진희
- Rejected: [딥담화] 삼성전자·SK하이닉스 자사주 매입 막바지..롤러코스피 나올까?｜이권희｜이화진｜이진우

### Power semiconductors — ok_low_relevance
Relevance groups: `[["power semiconductor", "功率 半導體", "SiC", "GaN"]]`
- Rejected: NVTS Stock: Can Navitas Semiconductor Turn the AI Power Boom Into Profits?
- Rejected: Navitas Semiconductor: The Next AI Power Giant? (NVTS Stock Deep Dive)
- Rejected: 第763集｜4Q九成機率上漲? 資金會往哪走? 高壓時代來了 第三代半導體掌握省電關鍵《凱基股股漲》2026/10/02
- Rejected: 【全集】外資大賣322億有人接盤！台.日.韓.德技術合作2028年玻璃基板...輝達聯手台積電台灣供應鏈繼續飆！？ - 黃世聰  封開平 吳岳展 劉彥良 張禹宣 劉寶傑《寶傑點兵》2026.09.29
- Rejected: Navitas Semiconductor: The AI Power Play or a Value Trap? (NVTS Stock Analysis)

### Tokenized stocks — ok_low_relevance
Relevance groups: `[["tokenized stock", "tokenized stocks", "tokenized equities"]]`
- Rejected: Top Agentic Projects On Robinhood Chain!
- Rejected: Why Robinhood Built Its Own Chain ($1.6B TVL in 3 Months)
- Rejected: The Memecoin War: Can Robinhood Challenge Solana?
- Rejected: ROBINHOOD CHAIN EVENT + TAO Event! The Future of Tokenization, AI,  and Meme Coins?!
- Rejected: Bitcoin's Institutional Era Has Arrived | Robinhood VP of Crypto Institutions Nicola White

### Semiconductor market / foundry manufacturing — ok_low_relevance
Relevance groups: `[["semiconductor", "foundry", "chip manufacturing"]]`
- Rejected: TSMC, Samsung and Intel Agreed to Double the Photomask
- Rejected: Marvell Alphabet custom silicon deal includes warrants
- Rejected: Japan's New Chip Factory Is Racing TSMC — And Nobody Saw It Coming
- Rejected: TSMC plans second Texas campus with potential $265 billion investment
- Rejected: The One Company Two Superpowers Can't Replace??

