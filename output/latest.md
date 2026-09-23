# YouTube Entity Enrichment

Generated: **2026-09-23T11:29:04.739583+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Meta Muse AI | Meta Muse AI | 28/50 | 56.0% | 834 | 47 | 12.5% | 10.0% | ok |
| 2 | NVIDIA | NVDA earnings | 43/50 | 86.0% | 59 | 36 | 24.3% | 60.0% | ok |
| 3 | Micron Technology | MU Micron earnings | 33/50 | 66.0% | 751 | 751 | 48.3% | 90.0% | ok |
| 4 | Memory stocks / HBM | memory stocks HBM | 25/50 | 50.0% | 175 | 175 | 23.8% | 80.0% | ok |
| 5 | Philadelphia Semiconductor Index | Philadelphia Semiconductor SOX | 7/33 | 21.2% | 362 | 362 | 14.3% | 100.0% | ok_low_relevance |
| 6 | Semiconductor stocks | semiconductor stocks | 20/50 | 40.0% | 97 | 74 | 20.0% | 60.0% | ok |
| 7 | Foxconn / Hon Hai | Foxconn Hon Hai stock | 6/7 | 85.7% | 2472 | 965 | 0.0% | 16.7% | ok |
| 8 | Yageo | Yageo stock | 8/10 | 80.0% | 819 | 620 | 0.0% | 75.0% | ok |
| 9 | AUO | AUO stock | 27/50 | 54.0% | 2908 | 183 | 0.0% | 0.0% | ok |
| 10 | Alphabet / Google | GOOGL earnings call | 14/50 | 28.0% | 12 | 10 | 9.1% | 70.0% | ok_low_relevance |
| 11 | Royal Caribbean | RCL stock | 20/50 | 40.0% | 39 | 20 | 7.1% | 50.0% | ok |
| 12 | General Mills | GIS earnings | 3/50 | 6.0% | 93 | 49 | 0.0% | 66.7% | ok_low_relevance |
| 13 | Tungsten stocks | tungsten stocks | 12/50 | 24.0% | 14 | 6 | 11.1% | 70.0% | ok_low_relevance |
| 14 | Oil stocks | oil stocks | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | US diesel policy | US diesel export ban Trump | 24/50 | 48.0% | 1684 | 80 | 46.2% | 50.0% | ok |
| 16 | US mortgage rates | US mortgage rates | 23/50 | 46.0% | 94 | 18 | 10.0% | 70.0% | ok |
| 17 | Mining stocks | mining stocks | 8/50 | 16.0% | 597 | 597 | 37.5% | 100.0% | ok_low_relevance |
| 18 | Silver stocks | silver stocks | 2/50 | 4.0% | 16 | 16 | 0.0% | 100.0% | ok_low_relevance |
| 19 | TSMC | TSM Taiwan Semiconductor | 14/36 | 38.9% | 52 | 52 | 8.3% | 90.0% | ok |
| 20 | Apple Siri AI | Apple Siri AI | 41/50 | 82.0% | 927 | 756 | 38.9% | 30.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Philadelphia Semiconductor Index — ok_low_relevance
Relevance groups: `[["Philadelphia Semiconductor", "SOX", "費城半導體"]]`
- Rejected: 害怕買在高點？統計曝「等崩盤」賺最少！破解0050配美股半導體的假性分散陷阱
- Rejected: Is AI Cooling Down & A Big Shift of Capital Rotation into Crypto Occurring?
- Rejected: 美股纳指巨头们都回来了！Meta 狂飙 11% 市值增近两千亿，AMD冲破万亿！个人agent软件带动AI硬件半导体？#meta #aiagents #cpu  #semiconductor
- Rejected: 2026-09-21 財經早報｜費半領漲
台股高檔戰
- Rejected: 미국증시 혼조 속 반도체 강세, 메모리·장비주까지 상승 확산

### Alphabet / Google — ok_low_relevance
Relevance groups: `[["Alphabet", "Google", "GOOG", "GOOGL"]]`
- Rejected: SPX Nears All-Time High, Diesel Sees Key Support as UN General Assembly Begins
- Rejected: Symbiotec Pharmalab Earnings Call for Q1FY27
- Rejected: Every AI CEO Agreed on “Safety” in Six Days—Now Look at Their Burn Rates!🚨 #ai #stockmarket
- Rejected: They Priced It Wrong
- Rejected: The Nasdaq surge: The Investment Committee's strategy

### General Mills — ok_low_relevance
Relevance groups: `[["General Mills", "GIS"]]`
- Rejected: The Highest Marginal Tax Rate in Canada Is Paid by Retirees on Modest Incomes
- Rejected: 📌 You're Probably Wrong About Your Tax Rate in Retirement (Canadian Seniors 65+)
- Rejected: How Canadian Seniors Get $19,956 a Year in 9 MINUTES (Widowed and Under 65)
- Rejected: 🎉Canadian Seniors: 5 Bills You Don't Have to Pay After 65 (Most People Don't Know)
- Rejected: Should You Delay OAS to 70? The Real Math

### Tungsten stocks — ok_low_relevance
Relevance groups: `[["tungsten", "钨", "鎢"]]`
- Rejected: Why $ELMT Just Received a Massive Defense Bailout
- Rejected: Gold and Antinmony, Full Production by 2027 | Chris Gerteisen on Nova Minerals (NYSE-A: NVA)
- Rejected: A Glimpse of What Happens When Oil Sells Off: Tech Stocks Rip
- Rejected: Resolution Minerals Ltd Advances Two FAST-41 Projects at Horse Heaven
- Rejected: Eps 27 - The Fed just raised rates. The question isn't what they did...

### Oil stocks — ok_no_relevant_videos
Relevance groups: `[["oil stocks", "energy stocks", "石油股"]]`
- Rejected: Slide in Crude Oil, Yields "Extremely Attractive" for Stocks, Mag 7 Lead Momentum
- Rejected: Oil Prices Are Plunging : Here's What Just Happened | Media Stocks Rally | Alok Jain
- Rejected: Market Open: Stocks Rise, Oil and Yields Lower, Amazon’s Next Sale Nears • 9/21/26
- Rejected: Tech Stocks and Crypto Huge Rally 🚨 Oil Prices Fall | Live Trading Stock Market Today $MU $SNDK $QQQ
- Rejected: Oil & Diesel export ban will TRIGGER A REAL INFLATION SHOCK #oil #wti #brent #stocks #marketcrash

### Mining stocks — ok_low_relevance
Relevance groups: `[["mining stocks", "miners"]]`
- Rejected: Eric Sprott Just Bought This Gold Stock! 2 Assets are Basically FREE — Cerrado Gold (CERT.V / CRDOF)
- Rejected: Greenland Mines Stock: The TRUTH About The Rare Earth Pivot & Financial Risk!
- Rejected: Peter Krauth: Silver Mania Still Ahead, Don't Get Caught in Bear Trap
- Rejected: Top 5 Gold Stocks To Watch - Takeover Targets For 2026
- Rejected: This Gold Discovery Was Already Huge. Now It’s Becoming a Monster. | Goliath Resources

### Silver stocks — ok_low_relevance
Relevance groups: `[["silver stocks", "silver miners"]]`
- Rejected: 🚨🚨...BUT It Gets Even BETTER! 🦍🦍 You BEST Hear This SILVER Price and Gold NEWS
- Rejected: Peter Krauth: Silver Mania Still Ahead, Don't Get Caught in Bear Trap
- Rejected: Don Durrett’s Masterclass on Investing in Gold & Silver Mining Stocks | Part 3
- Rejected: BREAKING! 🦍🦍 Metals Are Doing THIS! (Silver, Copper + Gold Price UPDATE)
- Rejected: The Global Monetary Reset Has Begun (Why Gold & Silver are Next)

