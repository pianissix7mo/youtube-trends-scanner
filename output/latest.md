# YouTube Entity Enrichment

Generated: **2026-09-06T11:35:02.746974+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Lululemon | Lululemon LULU earnings guidance | 19/50 | 38.0% | 136 | 63 | 6.7% | 60.0% | ok |
| 2 | Navitas Semiconductor | Navitas NVTS semiconductor stock | 11/14 | 78.6% | 31 | 31 | 0.0% | 100.0% | ok |
| 3 | OpenAI Astra | OpenAI Astra AI model | 49/50 | 98.0% | 31833 | 21600 | 83.3% | 0.0% | ok |
| 4 | UiPath | UiPath PATH earnings AI automation | 11/25 | 44.0% | 197 | 156 | 10.0% | 90.0% | ok |
| 5 | Zscaler | Zscaler ZS earnings cybersecurity | 13/28 | 46.4% | 122 | 45 | 12.5% | 50.0% | ok |
| 6 | Foxconn / Hon Hai | Foxconn Hon Hai 2317 AI server | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 7 | U.S. semiconductor tariffs | US semiconductor tariffs chip tariffs | 10/50 | 20.0% | 321 | 5 | 20.0% | 50.0% | ok_low_relevance |
| 8 | Broadcom | Broadcom AVGO earnings AI chips | 16/50 | 32.0% | 42 | 36 | 15.4% | 70.0% | ok |
| 9 | Planet Labs | Planet Labs PL earnings defense guidance | 5/50 | 10.0% | 223 | 47 | 0.0% | 60.0% | ok_low_relevance |
| 10 | Samsara | Samsara IOT earnings call | 5/31 | 16.1% | 19 | 19 | 0.0% | 100.0% | ok_low_relevance |
| 11 | Tesla | Tesla TSLA earnings | 4/50 | 8.0% | 2305 | 11 | 0.0% | 25.0% | ok_low_relevance |
| 12 | Memory stocks | memory stocks HBM DRAM Micron | 16/50 | 32.0% | 211 | 155 | 33.3% | 90.0% | ok |
| 13 | SEMICON Taiwan 2026 | SEMICON Taiwan 2026 semiconductor | 18/50 | 36.0% | 627 | 167 | 27.3% | 50.0% | ok |
| 14 | TSMC | TSMC Taiwan Semiconductor TSM stock | 10/15 | 66.7% | 17 | 17 | 10.0% | 100.0% | ok |
| 15 | Semiconductor ETFs | semiconductor ETF SMH SOXX | 2/5 | 40.0% | 15 | 15 | 0.0% | 100.0% | ok |
| 16 | ON Semiconductor | ON Semiconductor ON stock | 6/50 | 12.0% | 6492 | 736 | 33.3% | 50.0% | ok_low_relevance |
| 17 | indie Semiconductor | indie Semiconductor INDI stock | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 18 | Magnachip Semiconductor | Magnachip MX semiconductor stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 19 | Robinhood | Robinhood HOOD stock | 39/50 | 78.0% | 241 | 64 | 22.2% | 20.0% | ok |
| 20 | iPhone 18 / Apple | Apple AAPL iPhone 18 launch | 40/50 | 80.0% | 6066 | 1732 | 61.9% | 20.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### U.S. semiconductor tariffs — ok_low_relevance
Relevance groups: `[["semiconductor", "chip", "半導體"], ["tariff", "tariffs", "關稅", "关税"]]`
- Rejected: US Tariffs: The Secret Chipmaking Loophole Revealed!
- Rejected: US Tariffs Force Samsung & SK hynix: Build or Pay Big?
- Rejected: How the US-China Tech Split Is Reshaping Taiwan’s Chip Supply Chain | feat. Rocky Wu & Adam Ma
- Rejected: #LIVE【關我什麼事】川普再揮"晶片關稅"大刀! 不在美國設廠...直接砍向你?恐怖晶片關稅海嘯來襲! 台積電憑"免死金牌"全身而退?!｜陳斐娟 主持｜20260903
- Rejected: Lutnick: Taiwan To Bring 40% of Semiconductor Production to US｜TaiwanPlus News

### Planet Labs — ok_low_relevance
Relevance groups: `[["Planet Labs", "PL"], ["earnings", "guidance", "defense", "defence"]]`
- Rejected: $PL: Posts Record Q2 FY27 Revenue Building on Previously Disclosed Record Quarterly Performance
- Rejected: 【決算速報】PLプラネット・ラボ2027年Q2は売上高58%増も、防衛特需と粗利益率低下の持続性をどう見るか？
- Rejected: The largest enhanced-geothermal PPA announced to date will feed AI - TCR 09/03/26
- Rejected: Field Hearing – Industrial Base and Workforce Development for Skilled Trades
- Rejected: Blowout Jobs Report Jolts Markets | Open Interest 9/4/2026

### Samsara — ok_low_relevance
Relevance groups: `[["Samsara", "IOT"], ["earnings", "guidance", "财报", "財報"]]`
- Rejected: Samsara (IOT) Q2 FY2027: Massive Growth & GAAP Profitability
- Rejected: I Ran Samsara’s Numbers Through My Model — Here’s What It Spit Out for IOT
- Rejected: Samsara Hits $2.1B ARR: Growth vs Cash Flow Reality
- Rejected: Lulu Dives; Adobe New CEO; Samsara Higher | Stock Movers
- Rejected: 【決算速報】サムサラ（IOT）2027年度第2四半期は30％増収で予想超過も株価は小幅高にとどまる理由とは？

### Tesla — ok_low_relevance
Relevance groups: `[["Tesla", "TSLA"], ["earnings", "guidance", "财报", "財報"]]`
- Rejected: Why Traders Are Buying TSLA Calls Before the Cybercab Event
- Rejected: Tesla Incentive Update
- Rejected: Tesla Transformative CyberCab Launch (TSLA Stock)
- Rejected: TSLA After the Quiet Launch | When Does Cybercab Actually Print Profit?
- Rejected: Is Tesla Stock A Buy After The BIG NEWS?

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: 3 AI Semiconductor Stocks To Love After Their Post-Earnings Sell-Off!!
- Rejected: Best Semiconductor Stock to Buy: Marvell Stock or Qualcomm Stock? | MRVL Stock vs. QCOM Stock
- Rejected: NVIDIA Stuns Wall Street | Buy 3 AI Semiconductor Stocks Now | WFE DRAM NAND
- Rejected: NVTS Stock CRASH 🚨 Is Navitas Semiconductor the Next AI Power Winner?
- Rejected: IA13: Which Memory Stock To Buy? 🧠 SK Hynix vs Samsung vs Micron

### indie Semiconductor — ok_no_relevant_videos
Relevance groups: `[["indie Semiconductor", "INDI"]]`
- Rejected: अंटार्कटिका में माइनस 50 डिग्री पर विदेशी साजिश-भारत के आवारा लड़के ने ऐसे किया बेनकाब! | Story

