# YouTube Entity Enrichment

Generated: **2026-09-16T11:44:37.135451+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Apple Siri AI | Apple AAPL Siri AI iOS 27 | 49/50 | 98.0% | 20183 | 11494 | 87.5% | 0.0% | ok |
| 2 | Micron Technology | Micron MU earnings memory HBM | 9/25 | 36.0% | 55 | 55 | 0.0% | 100.0% | ok |
| 3 | Semiconductor industry | semiconductor news chip stocks AI | 7/50 | 14.0% | 103 | 17 | 0.0% | 57.1% | ok_low_relevance |
| 4 | Power semiconductors | power semiconductor GaN SiC stocks | 1/3 | 33.3% | 371 | 371 | 0.0% | 100.0% | ok |
| 5 | AI slowdown | AI slowdown AI capex chips stocks | 9/50 | 18.0% | 1216 | 11 | 0.0% | 44.4% | ok_low_relevance |
| 6 | Alphabet / Google | Google GOOGL earnings AI cloud | 7/40 | 17.5% | 570 | 114 | 0.0% | 57.1% | ok_low_relevance |
| 7 | ASML | ASML earnings EUV High NA | 3/10 | 30.0% | 2327 | 1198 | 50.0% | 66.7% | ok |
| 8 | Arm Holdings | Arm ARM earnings AI chips | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Robinhood | Robinhood HOOD stock | 22/50 | 44.0% | 70 | 50 | 10.5% | 70.0% | ok |
| 10 | OpenAI / Hugging Face | OpenAI ChatGPT Hugging Face incident | 15/50 | 30.0% | 416 | 19 | 10.0% | 50.0% | ok |
| 11 | Microsoft | Microsoft MSFT earnings AI Azure | 1/9 | 11.1% | 3091 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 12 | NVIDIA | NVIDIA NVDA earnings AI GPU | 5/39 | 12.8% | 41 | 41 | 0.0% | 100.0% | ok_low_relevance |
| 13 | TSMC | TSMC TSM 台積電 AI chips | 1/3 | 33.3% | 3 | 3 | 0.0% | 100.0% | ok |
| 14 | Tesla Roadster | Tesla TSLA Roadster Oct 1 | 38/50 | 76.0% | 738 | 582 | 32.3% | 60.0% | ok |
| 15 | Oil and gasoline prices | oil gas prices Iran inflation markets | 9/50 | 18.0% | 10166 | 23052 | 100.0% | 11.1% | ok_low_relevance |
| 16 | Salesforce | Salesforce CRM Koa AI outage Dreamforce | 1/5 | 20.0% | 255 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 17 | Winbond Electronics | Winbond 華邦電 memory semiconductor | 1/3 | 33.3% | 0 | 0 | 0.0% | 0.0% | ok |
| 18 | onsemi | onsemi ON Semiconductor stock power chips | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 19 | Navitas Semiconductor | Navitas Semiconductor NVTS GaN stock | 3/3 | 100.0% | 29 | 29 | 0.0% | 100.0% | ok |
| 20 | Uber | Uber UBER Uber Eats earnings | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor industry — ok_low_relevance
Relevance groups: `[["semiconductor", "semiconductors", "chip stocks", "半導體", "半导体"]]`
- Rejected: The Stock Market Nervousness, Fed, Elon, AI Chips
- Rejected: AI Safety Risks Spark Chip Selloff & Crude Oil Rises Back Above $100
- Rejected: 3 AI Stocks to Buy Regardless of What the Fed Does!
- Rejected: Stocks Fall on AI Fears as 10-Year Yield Hits 5%
- Rejected: Matthew Caruso on AI Safety Selloff "Overreaction," Picks AMD, DELL & HPE

### AI slowdown — ok_low_relevance
Relevance groups: `[["AI slowdown", "AI spending slowdown", "AI capex slowdown", "AI development pace", "AI bubble"]]`
- Rejected: 3 AI Stocks to Buy Regardless of What the Fed Does!
- Rejected: Stocks Fall on AI Fears as 10-Year Yield Hits 5%
- Rejected: Ca$htag$: GOOGL Vast CapEx Justifies $500B Backlog in AI Acceleration
- Rejected: European Tech Stocks Hit by AI Boss Risk Warnings
- Rejected: Who Wins and Loses From AI Safety Cyber Rotation

### Alphabet / Google — ok_low_relevance
Relevance groups: `[["Google", "Alphabet", "GOOGL", "GOOG"], ["earnings", "results", "guidance", "AI", "cloud"]]`
- Rejected: **Alphabet Spent $91 Billion in One Year — Here's What the 10-Ks Say**
- Rejected: Google Looks Cheap. The P/E Is Lying (GOOGL Stock Analysis)
- Rejected: Alphabet (GOOGL) Long Term Outlook
- Rejected: 3 AI Stocks to Watch Now in 2026 🤖📈 #shorts
- Rejected: Ca$htag$: AMZN Cloud Growth Lags Behind MSFT, "Their Game to Lose"

### Arm Holdings — ok_no_relevant_videos
Relevance groups: `[["Arm"], ["earnings", "results", "chip", "AI"]]`
- Rejected: Nvidia Stock Fell 3% on AI Fears. CrowdStrike Jumped 14%.
- Rejected: The $30 Billion AI Bottleneck Nobody Talks About
- Rejected: Google Just Won The AI Race
- Rejected: 【精選回顧】任正非「出逃」傳聞破了！華為要全面出海！從AI晶片到整座資料中心全包 輝達真對手殺來了！｜獨家觀點 #環球大戰線 #寰宇新聞 @globalnewstw
- Rejected: Xi Pitches AI Vision as Silicon Valley Leaders Tap Brakes

### Microsoft — ok_low_relevance
Relevance groups: `[["Microsoft", "MSFT"], ["earnings", "results", "AI", "Azure", "cloud"]]`
- Rejected: Microsoft (MSFT): My #1 Mega Cap | Series 1 of 6
- Rejected: 3 AI Stocks to Watch Now in 2026 🤖📈 #shorts
- Rejected: マイクロソフトは何で稼ぐ？売上18%増を支える「Windows以外」の事業 | $MSFT
- Rejected: 微软靠什么赚钱？从 Office、Azure 到 Copilot，看懂它的商业模式
- Rejected: 王逸研：港股進入調正時期 關注黃金、石油類資源！AI模型暗湧不斷 OPENAI繼續指引模型發展 #AI #科技股 #投資

### NVIDIA — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA"], ["earnings", "results", "AI", "GPU"]]`
- Rejected: Nvidia CEO Says "AGI Is HERE". Demand For Compute Explodes
- Rejected: The Economics Behind NVIDIA’s $5 Trillion Empire
- Rejected: 【米国株】エヌビディア「我々を信じなさい」→株価上昇
- Rejected: Jensen and Elon speak at the All-In Summit and the market is red
- Rejected: Who Should Regulate AI? America's Fight Over the Rules

### Oil and gasoline prices — ok_low_relevance
Relevance groups: `[["gas prices", "oil prices", "Brent", "WTI", "汽油價格", "油價"]]`
- Rejected: Eurasia Group’s Greg Brew: The conflict in Iran is being fought in the oil market
- Rejected: Rep. Waters Presses Bessent on Inflation, Iran and Tariffs
- Rejected: Big Oil Shock To Impact The Markets? Red Sea Crisis, Iran-US Tensions Spark Fresh Alarm
- Rejected: Crude & Yields' Greater Stock Market Impacts, Global Economies Eye Rate Hikes
- Rejected: Oil Price Jumps Again | Iran War Updates and News Analysis

### Salesforce — ok_low_relevance
Relevance groups: `[["Salesforce", "CRM"], ["Koa", "AI", "outage", "Dreamforce", "NVIDIA"]]`
- Rejected: Claudeforce: Salesforce Hands Its UI to Claude | The 96% Brief SPECIAL
- Rejected: Anthropic's CEO Asked the Industry to Slow Down | The 96% Brief W38
- Rejected: AI’s Reality Check, OpenAI’s Trillion-Dollar Report, and Smarter AI Factories | UpNext AI – Septe...
- Rejected: Today's Top 4 in Artificial Intelligence — Darwinbox Gets Follow-On Investment, Launches Cortex

### Uber — ok_no_relevant_videos
Relevance groups: `[["Uber", "Uber Eats"], ["earnings", "results", "guidance"]]`
- Rejected: Uber Eats vs DoorDash 2026: The Higher-Paying App Loses After Taxes
- Rejected: I Make Over $1,400 EVERY WEEK Driving Uber - Here's How I Do It!!
- Rejected: I Worked Only Uber Eats for a Full Day — Here’s What I Made
- Rejected: I Worked All Week… Then Made $49/HR on Uber Eats Friday Night! 😱
- Rejected: How Much Does a Food Delivery Driver Earn In 1Hour? Fights, Cancelled Orders & Long Distances!

