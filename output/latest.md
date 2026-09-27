# YouTube Entity Enrichment

Generated: **2026-09-27T12:14:37.985663+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Costco | Costco COST earnings | 17/50 | 34.0% | 48 | 26 | 0.0% | 60.0% | ok |
| 2 | Semiconductor shortage | semiconductor chip shortage | 4/50 | 8.0% | 81 | 81 | 0.0% | 100.0% | ok_low_relevance |
| 3 | Semiconductor stocks | semiconductor stocks | 27/50 | 54.0% | 100 | 98 | 14.3% | 70.0% | ok |
| 4 | Meta AI glasses | Meta AI glasses | 19/50 | 38.0% | 179 | 36 | 8.3% | 30.0% | ok |
| 5 | Amazon | Amazon AMZN earnings | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 6 | Meta Muse AI | Meta Muse AI | 40/50 | 80.0% | 4908 | 571 | 35.7% | 20.0% | ok |
| 7 | NVIDIA | NVIDIA NVDA earnings | 8/50 | 16.0% | 350 | 340 | 28.6% | 87.5% | ok_low_relevance |
| 8 | Semiconductor ETFs | semiconductor ETF SOXX SMH | 1/7 | 14.3% | 187 | 187 | 0.0% | 100.0% | ok_low_relevance |
| 9 | Memory stocks | memory stocks Micron SanDisk SK Hynix | 12/17 | 70.6% | 1740 | 1740 | 60.0% | 80.0% | ok |
| 10 | Tesla | Tesla TSLA earnings | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Biotech stocks | biotech stocks | 14/50 | 28.0% | 10 | 10 | 7.1% | 100.0% | ok_low_relevance |
| 12 | Micron Technology | Micron MU earnings | 19/50 | 38.0% | 4 | 4 | 12.5% | 80.0% | ok |
| 13 | BlackBerry | BlackBerry BB stock | 24/34 | 70.6% | 43 | 43 | 0.0% | 90.0% | ok |
| 14 | indie Semiconductor | indie Semiconductor INDI | 0/21 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | TSMC | TSMC Taiwan Semiconductor | 28/50 | 56.0% | 68 | 21 | 5.0% | 40.0% | ok |
| 16 | ON Semiconductor | ON Semiconductor onsemi | 1/6 | 16.7% | 3 | 3 | 0.0% | 100.0% | ok_low_relevance |
| 17 | Anthropic / Claude | Anthropic Claude AI | 50/50 | 100.0% | 1006 | 839 | 38.9% | 20.0% | ok |
| 18 | Navitas Semiconductor | Navitas Semiconductor NVTS | 3/3 | 100.0% | 4 | 4 | 0.0% | 100.0% | ok |
| 19 | Magnachip Semiconductor | Magnachip Semiconductor MX | 2/3 | 66.7% | 255 | 255 | 0.0% | 100.0% | ok |
| 20 | Robotics stocks | robotics stocks | 17/50 | 34.0% | 58 | 35 | 12.5% | 90.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor shortage — ok_low_relevance
Relevance groups: `[["semiconductor shortage", "chip shortage", "半导体短缺", "半導體短缺"]]`
- Rejected: DEBATE: The Great Indian Chip Buildout: What Comes Next?
- Rejected: The Chips That Secretly Run the World!!
- Rejected: Is the AI Bull Market Moving Past Semiconductors?
- Rejected: ⚠️ America’s Chip Factory Problem Started BEFORE It Even Opened 😳🇺🇸  #ChipFactory #TechNews
- Rejected: Why Are Electronics Getting SO EXPENSIVE in 2026? | The Real Reason

### Amazon — ok_no_relevant_videos
Relevance groups: `[["Amazon", "AMZN"], ["earnings", "results", "财报", "財報"]]`
- Rejected: What Gives AMZN "Most Interesting" Stock Set Up of Mag 7 Since All-Time High Plunge
- Rejected: Amazon topped $200B. Which business drives it?
- Rejected: A $7 Million Amazon Trade Just Showed Up, Here Is The Structure
- Rejected: AMZN (Amazon): Monday Predicted Opening Price + 3 Scenarios - Is $2000 Broken? 🚨
- Rejected: AMZN Amazon: 5 Stock Signals After Sept 24 News - Friday Predicted Opening Price? 📈

### NVIDIA — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA", "英伟达", "輝達"], ["earnings", "results", "财报", "財報"]]`
- Rejected: AI Bubble?  Nvidia Stock is Cheap!
- Rejected: NVIDIA's Stock is "Incredibly Misunderstood" — The 2026 Deep Dive
- Rejected: NVDA Stock News: What Beginners Should Check First
- Rejected: Micron Nvidia AMD SanDisk Broadcom STOCKS The Warning Nobody Sees ($MU $NVDA $AMD $SNDK $AVGO)
- Rejected: This Could Be the End Of Nvidia

### Semiconductor ETFs — ok_low_relevance
Relevance groups: `[["semiconductor ETF", "SOXX", "SMH", "半导体 ETF", "半導體 ETF"]]`
- Rejected: CLOU: How the Weighting Rule Decides What You Own
- Rejected: GRID: What the Expense Ratio Costs Over a Full Cycle
- Rejected: ETF DE INFRAESTRUTURA DE IA
- Rejected: 2028~2029년, 미국이 전쟁을 준비하고 있다는 이 이론, 우연일까요? #나스닥100 #qqq
- Rejected: ETF QUE INVESTE NA INFRAESTRUTURA DE IA

### Tesla — ok_no_relevant_videos
Relevance groups: `[["Tesla", "TSLA"], ["earnings", "results", "财报", "財報"]]`
- Rejected: TSLA This Week: SOMETHING BIG IS DEVELOPING
- Rejected: Tesla Semi Wins the Biggest Electric Truck Order in History - DISRUPTION COMING!
- Rejected: We NEED to Discuss Tesla Optimus Robots NOW.
- Rejected: SpaceX vs Tesla Growth Expectations
- Rejected: Tesla Cybercab Gets a Flat Tire, and Grok Builds FSD!

### Biotech stocks — ok_low_relevance
Relevance groups: `[["biotech", "biotechnology", "biopharma", "生物科技", "生技"]]`
- Rejected: Saudi Pipeline Attacked 🚨, Bank Stocks Have Peaked 📉 & 3 Healthcare Stocks to Own 💊
- Rejected: Erasca Stock Analysis: The $400M Bet on RAS Cancer Drugs (ERAS-0015 & ERAS-4001)
- Rejected: LES BIOTECHS S'EFFONDRENT JUSQU'À 25% EN UN JOUR
- Rejected: Twist Bioscience Stock Analysis: Is the AI Hype Worth the Premium Price?
- Rejected: Pharma stock soars 150% on injectables deal with Wegovy maker Novo

### indie Semiconductor — ok_no_relevant_videos
Relevance groups: `[["indie Semiconductor", "INDI"]]`
- Rejected: 🇮🇳 India's Semiconductor Dream: What is Missing? #Semiconductors #UPSC
- Rejected: Why India Needs “Safety of Business,” Not Just Ease of Business | Jahangir Aziz | The Core
- Rejected: Taiwan Semiconductor Manufacturing
- Rejected: From Limits to Scale: How Make in India Transformed Domestic Manufacturing
- Rejected: Trump-Xi Summit: Here’s What’s on the Agenda, and Why It Matters for India

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON Semi"]]`
- Rejected: Why so much talk about GaN?
- Rejected: Synaptics (SYNA) Stock Analysis: Deep Dive Into the $7B Physical AI Takeover
- Rejected: Meta Muse: The AI Agent Era Has Arrived!
- Rejected: 美股下周怎么走？周五非农会送利好？QQQ再冲历史新高｜AI半导体、特斯拉、美光全解析【华尔街圆桌第15期】
- Rejected: ETF QUE INVESTE NA INFRAESTRUTURA DE IA

