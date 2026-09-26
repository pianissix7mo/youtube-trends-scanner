# YouTube Entity Enrichment

Generated: **2026-09-26T12:44:42.425582+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Costco | Costco COST earnings | 15/50 | 30.0% | 54 | 50 | 0.0% | 60.0% | ok |
| 2 | Semiconductor shortage | semiconductor chip shortage | 3/50 | 6.0% | 129 | 129 | 0.0% | 100.0% | ok_low_relevance |
| 3 | Semiconductor stocks | semiconductor stocks | 28/50 | 56.0% | 76 | 49 | 10.0% | 50.0% | ok |
| 4 | Meta AI glasses | Meta AI glasses | 11/50 | 22.0% | 1334 | 87 | 0.0% | 20.0% | ok_low_relevance |
| 5 | Amazon | Amazon AMZN earnings | 1/50 | 2.0% | 79 | 79 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Meta Muse AI | Meta Muse AI | 41/50 | 82.0% | 8060 | 1908 | 57.1% | 20.0% | ok |
| 7 | NVIDIA | NVIDIA NVDA earnings | 4/50 | 8.0% | 244 | 244 | 25.0% | 100.0% | ok_low_relevance |
| 8 | Semiconductor ETFs | semiconductor ETF SOXX SMH | 0/10 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Memory stocks | memory stocks Micron SanDisk SK Hynix | 11/15 | 73.3% | 2386 | 2386 | 55.6% | 80.0% | ok |
| 10 | Tesla | Tesla TSLA earnings | 1/50 | 2.0% | 82 | 82 | 0.0% | 100.0% | ok_low_relevance |
| 11 | Biotech stocks | biotech stocks | 17/50 | 34.0% | 19 | 18 | 6.2% | 90.0% | ok |
| 12 | Micron Technology | Micron MU earnings | 17/50 | 34.0% | 36 | 28 | 14.3% | 80.0% | ok |
| 13 | BlackBerry | BlackBerry BB stock | 22/32 | 68.8% | 40 | 36 | 0.0% | 90.0% | ok |
| 14 | indie Semiconductor | indie Semiconductor INDI | 0/21 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | TSMC | TSMC Taiwan Semiconductor | 31/50 | 62.0% | 92 | 25 | 5.6% | 40.0% | ok |
| 16 | ON Semiconductor | ON Semiconductor onsemi | 1/10 | 10.0% | 0 | 0 | 0.0% | 100.0% | ok_low_relevance |
| 17 | Anthropic / Claude | Anthropic Claude AI | 49/50 | 98.0% | 2342 | 1305 | 71.0% | 20.0% | ok |
| 18 | Navitas Semiconductor | Navitas Semiconductor NVTS | 4/5 | 80.0% | 41 | 41 | 0.0% | 100.0% | ok |
| 19 | Magnachip Semiconductor | Magnachip Semiconductor MX | 1/3 | 33.3% | 224 | 224 | 0.0% | 100.0% | ok |
| 20 | Robotics stocks | robotics stocks | 18/50 | 36.0% | 44 | 28 | 0.0% | 60.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor shortage — ok_low_relevance
Relevance groups: `[["semiconductor shortage", "chip shortage", "半导体短缺", "半導體短缺"]]`
- Rejected: The AI Memory Boom | Why DRAM Prices Are Surging
- Rejected: 亞洲稱霸多年 美推動半導體自主卻遇"缺工"  半導體蓬勃撐起經濟! 南韓初階職缺暴增50%｜非凡財經新聞｜20260925
- Rejected: "지금 반도체 대란? 솔직히 까놓고 말해 전부 애플 탓입니다" l 곽상준 대표 팩폭 #곽상준 #반도체 #애플 #마이크론
- Rejected: DEBATE: India Is Building Chip Fabs Worth Billions - But Who Is Actually Going to Buy the Chips?
- Rejected: Why Are Smartphones Getting So Expensive? 😳 AI Is Making Phones Costlier! #facts #smartphone

### Meta AI glasses — ok_low_relevance
Relevance groups: `[["Meta"], ["AI glasses", "smart glasses", "眼镜", "眼鏡"]]`
- Rejected: Hands-On With Meta VR Glasses and All of Meta's Other Glasses and AI
- Rejected: First impressions of Meta's new camera-free Ray-Ban Audio glasses
- Rejected: Meta's New VR Glasses Are Not What You Think
- Rejected: Meta Quest 4 Is Finally Here! - Meta VR Glasses Hands-On
- Rejected: EVERYTHING You Missed at Meta Connect 2026

### Amazon — ok_low_relevance
Relevance groups: `[["Amazon", "AMZN"], ["earnings", "results", "财报", "財報"]]`
- Rejected: What Gives AMZN "Most Interesting" Stock Set Up of Mag 7 Since All-Time High Plunge
- Rejected: A $7 Million Amazon Trade Just Showed Up, Here Is The Structure
- Rejected: AMZN (Amazon): Monday Predicted Opening Price + 3 Scenarios - Is $2000 Broken? 🚨
- Rejected: AMZN Amazon: 5 Stock Signals After Sept 24 News - Friday Predicted Opening Price? 📈
- Rejected: Stock Market Warnings to Watch - Is Amazon Stock an Opportunity?

### NVIDIA — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA", "英伟达", "輝達"], ["earnings", "results", "财报", "財報"]]`
- Rejected: NVIDIA $1072: Jim Cramer Breaks Down the Big Question
- Rejected: 🤖📈 Nvidia to be the First Company with a $10 Trillion Dollar Market Cap? | $NVDA Stock #shorts
- Rejected: Is Nvidia Overvalued in 2026?
- Rejected: The Market May Be Wrong About These 2 AI Stocks
- Rejected: Nvidia Is Repeating Cisco's Fatal Mistake

### Semiconductor ETFs — ok_no_relevant_videos
Relevance groups: `[["semiconductor ETF", "SOXX", "SMH", "半导体 ETF", "半導體 ETF"]]`
- Rejected: Wall Street Money Is Rotating Into Tech—Don’t Get Left Behind
- Rejected: SK하이닉스, 美 반도체 ETF 줄편입…글로벌 자금 몰린다
- Rejected: CLOU: How the Weighting Rule Decides What You Own
- Rejected: GRID: What the Expense Ratio Costs Over a Full Cycle
- Rejected: IGV: Why the Index and the Fund Do Not Match

### Tesla — ok_low_relevance
Relevance groups: `[["Tesla", "TSLA"], ["earnings", "results", "财报", "財報"]]`
- Rejected: Tesla Stock Price Analysis | Top $TSLA Levels To Watch for September 24th, 2026
- Rejected: A Tesla Engineer Just Revealed Grok’s Role in FSD
- Rejected: We NEED to Discuss Tesla Optimus Robots NOW.
- Rejected: The REAL Cost of Your Next Tesla (Don't Get Scammed)
- Rejected: SpaceX vs Tesla Growth Expectations

### indie Semiconductor — ok_no_relevant_videos
Relevance groups: `[["indie Semiconductor", "INDI"]]`
- Rejected: Macro, Relative Strength, Breadth, Trends & Risk - Weekly Review
- Rejected: ASML Says It's Selling Zero Chip Machines In Europe | Here's Why That's A Warning Sign
- Rejected: ALERT: India and EU Are Building a Joint AI Chip and 6G Alliance While the UN Calls AI Existential
- Rejected: ‘India has enough capacity for mobile screen protectors…’: says MeitY Secy S Krishnan
- Rejected: Why India Needs “Safety of Business,” Not Just Ease of Business | Govindraj Ethiraj | The Core

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON Semi"]]`
- Rejected: Why so much talk about GaN?
- Rejected: Scaling Software-Defined Vehicles with 10BASE-T1S
- Rejected: Options Corner: ON Making Bullish Crossover as SMH Outperforms
- Rejected: AI has a power problem. These 5 stocks are built to solve it.
- Rejected: Meta Muse: The AI Agent Era Has Arrived!

