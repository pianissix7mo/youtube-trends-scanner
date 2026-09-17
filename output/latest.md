# YouTube Entity Enrichment

Generated: **2026-09-17T11:50:59.535296+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Apple / Siri AI | Apple Siri AI iOS 27 waitlist | 50/50 | 100.0% | 16777 | 5112 | 73.3% | 0.0% | ok |
| 2 | Cannabis stocks | cannabis stocks US | 1/50 | 2.0% | 7090 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 3 | Grab Holdings | Grab GRAB stock | 30/50 | 60.0% | 767 | 309 | 37.5% | 60.0% | ok |
| 4 | Uber | Uber UBER earnings Uber Eats | 29/50 | 58.0% | 240 | 221 | 26.9% | 90.0% | ok |
| 5 | Samsung Semiconductor Austin | Samsung semiconductor Austin fab | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 6 | VanEck Semiconductor ETF / SMH | SMH VanEck Semiconductor ETF | 2/6 | 33.3% | 6 | 6 | 0.0% | 100.0% | ok |
| 7 | TSMC | TSM TSMC earnings call | 21/50 | 42.0% | 15 | 15 | 15.8% | 90.0% | ok |
| 8 | AI slowdown | AI slowdown AI stocks semiconductors | 14/50 | 28.0% | 410 | 13 | 11.1% | 50.0% | ok_low_relevance |
| 9 | Robinhood Markets | HOOD Robinhood stock | 41/50 | 82.0% | 170 | 124 | 8.8% | 40.0% | ok |
| 10 | OpenAI / Hugging Face incident | OpenAI Hugging Face incident | 6/50 | 12.0% | 162 | 162 | 16.7% | 100.0% | ok_low_relevance |
| 11 | AI regulation | AI regulation stocks policy | 3/50 | 6.0% | 48 | 24 | 0.0% | 66.7% | ok_low_relevance |
| 12 | Tesla | TSLA Tesla earnings call | 47/50 | 94.0% | 14220 | 11377 | 100.0% | 20.0% | ok |
| 13 | Silver | silver stocks silver miners | 5/50 | 10.0% | 236 | 236 | 40.0% | 100.0% | ok_low_relevance |
| 14 | AMD | AMD earnings stock | 27/50 | 54.0% | 66 | 39 | 9.1% | 60.0% | ok |
| 15 | NVIDIA | NVDA Nvidia earnings call | 34/50 | 68.0% | 1663 | 1027 | 50.0% | 60.0% | ok |
| 16 | Semiconductor chip shortage | semiconductor chip shortage supply chain | 2/50 | 4.0% | 40 | 40 | 0.0% | 100.0% | ok_low_relevance |
| 17 | DoorDash | DASH DoorDash earnings | 24/49 | 49.0% | 756 | 120 | 33.3% | 50.0% | ok |
| 18 | Arm Holdings | ARM Arm earnings call | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 19 | Bank of Canada rates | Bank of Canada interest rate fuel inflation | 1/50 | 2.0% | 0 | 0 | 0.0% | 100.0% | ok_low_relevance |
| 20 | Ardentec / 欣銓 (3264) | 欣銓 3264 AI ASIC testing | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Cannabis stocks — ok_low_relevance
Relevance groups: `[["cannabis stocks", "marijuana stocks", "weed stocks"]]`
- Rejected: US Cannabis: Much Ado About Deflation?
- Rejected: Tilray Stock Is Getting Interesting — What Comes Next?
- Rejected: TLRY STOCK: Something BIG Is Brewing Behind the Scenes
- Rejected: The rescheduling of medical marijuana
- Rejected: Cannabis Investing Guide Individual Stocks

### Samsung Semiconductor Austin — ok_no_relevant_videos
Relevance groups: `[["Samsung Semiconductor", "Samsung Austin", "Samsung fab Austin"]]`
- Rejected: 삼성 텍사스 반도체 공장, 상상 이상의 건설 현장 공개, 삼성물산이 짓는 텍사스 반도체 공장, 비싼 장비를 놓기 전에 해야 할 일
- Rejected: 10 Texas Megaprojects That Will Change America Forever
- Rejected: 삼성이 텍사스 시골 마을에 17조를 묻은 진짜 이유

### AI slowdown — ok_low_relevance
Relevance groups: `[["AI slowdown", "AI spending slowdown", "AI capex slowdown", "AI demand slowdown"]]`
- Rejected: The AI Dip Is a Gift (2 Stocks I'm Buying)
- Rejected: AI Stocks are CRASHING: Here's What I'm Buying
- Rejected: 3 AI Stocks to Buy Regardless of What the Fed Does!
- Rejected: AI and Chip Stocks Slide as CEOs Call to Slow Down AI
- Rejected: AI Stocks Just Got HIT — NVIDIA, AMD & Intel Are Falling 🤯

### OpenAI / Hugging Face incident — ok_low_relevance
Relevance groups: `[["OpenAI Hugging Face incident", "Hugging Face incident", "OpenAI Hugging Face"]]`
- Rejected: As a Microsoft Engineer, This Is the AI Agent Story That Scared Me
- Rejected: How OpenAI agents went rogue and hacked Hugging Face
- Rejected: OpenAI Agents Probed Hugging Face In Security Investigation  |WION
- Rejected: OpenAI’s AI Agents Built a Secret Network, Then Hacked Hugging Face
- Rejected: How 700 OpenAI Agents hacked Huggingface (Architect Post-Mortem)

### AI regulation — ok_low_relevance
Relevance groups: `[["AI regulation", "AI policy", "AI regulator", "AI rules"]]`
- Rejected: AI's regulatory divide grows
- Rejected: Meta’s Zuckerberg, Nvidia’s Huang Push Alternatives to AI Slowdown
- Rejected: Small group of AI companies should not set the policy on AI, says Cohere CEO Aidan Gomez
- Rejected: Bond Yields Surge Ahead of the Fed Rate Decision
- Rejected: 'Big Short' investor Steve Eisman on AI: The companies are trying to manufacture a crisis

### Silver — ok_low_relevance
Relevance groups: `[["silver stocks", "silver miners", "silver mining stocks"]]`
- Rejected: SILVER and GOLD 🚨 ALERT! 🚨 - Smart Investors Buying THIS News!
- Rejected: This Undervalued Silver Mining Stock is Already Producing: GoGold Resources (GGD.TO / GLGDF)
- Rejected: I Sold My Entire Position In This Popular Silver Mining Stock : Avino Gold & Silver (ASM / ASM.TO)
- Rejected: Michael Oliver: Why $500 Silver May Be Just the Beginning
- Rejected: Episode #81: Why Silver Could Outperform Gold | Kuya Silver CEO David Stein

### Semiconductor chip shortage — ok_low_relevance
Relevance groups: `[["semiconductor chip shortage", "chip shortage", "semiconductor shortage"]]`
- Rejected: More ‘BAD S**T WILL HAPPEN’ if we don’t act: Naomi Klein & Astra Taylor EXPOSE ‘End Times Fascism’
- Rejected: TSMC CoWoS: Nvidia Takes 595,000 Wafers — You Get What's Left
- Rejected: Why HBM Shortages Bottleneck AI Training Clusters
- Rejected: Bond Yields Surge Ahead of the Fed Rate Decision
- Rejected: AI模型黑化? 放進虛擬試管竟無師自通"暗號" 美債殖利率又衝 美股3大指數翻黑.費半撐盤｜主播貝庭｜【非凡Morning Call】20260917｜非凡財經新聞

### Arm Holdings — ok_no_relevant_videos
Relevance groups: `[["Arm", "Arm Holdings", "Arm earnings"]]`
- Rejected: 102 MPH Without Extension | Justin Martinez (See Description)
- Rejected: How to Add Another $1M/Year to Your Wholesale Business
- Rejected: Behind Enemy Lines, Vol. 12
- Rejected: Andrew Yang on AI safety issues: The fear is real, the concern is real
- Rejected: Despite big win last weekend, Deion Sanders still not satisfied with his Colorado Buffaloes

### Bank of Canada rates — ok_low_relevance
Relevance groups: `[["Bank of Canada", "BoC", "Canada interest rates"]]`
- Rejected: Canada inflation holds at 3% as fuel prices rise
- Rejected: Canada's inflation rate steady at 3% in August as travel, rent costs soar
- Rejected: EU Proposes Canada to Become First ‘Associate Member’; Fed Decision on Deck
- Rejected: Trump Floats EU Tariffs on Canada Invite, Warsh’s Inflation Fight Calms Market
- Rejected: Stocks, Bonds Find Relief Ahead of Fed, EU Floats Canada Becoming 'Associate Member'

