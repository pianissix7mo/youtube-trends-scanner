# YouTube Entity Enrichment

Generated: **2026-10-04T11:41:31.731894+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Nike | Nike NKE earnings 2027 outlook | 9/22 | 40.9% | 143 | 94 | 25.0% | 88.9% | ok |
| 2 | Alphabet / Google | Alphabet GOOGL Google stock AI | 23/50 | 46.0% | 19 | 15 | 6.2% | 50.0% | ok |
| 3 | Semiconductor ETF / Philadelphia Semiconductor Index | semiconductor ETF SOX Philadelphia Semiconductor Index | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 4 | Circle Internet Group | Circle CRCL stock stablecoin USDC | 2/3 | 66.7% | 23 | 23 | 0.0% | 100.0% | ok |
| 5 | ON Semiconductor | ON Semiconductor ON stock Synaptics | 8/50 | 16.0% | 4 | 4 | 0.0% | 100.0% | ok_low_relevance |
| 6 | NIO | NIO earnings stock | 12/50 | 24.0% | 368 | 368 | 33.3% | 100.0% | ok_low_relevance |
| 7 | Accenture | Accenture ACN earnings AI | 21/50 | 42.0% | 14 | 14 | 0.0% | 90.0% | ok |
| 8 | Oracle | Oracle ORCL stock AI cloud | 12/26 | 46.2% | 24 | 17 | 9.1% | 90.0% | ok |
| 9 | Quantum computing stocks | quantum computing stocks IONQ RGTI QBTS | 8/10 | 80.0% | 29 | 29 | 0.0% | 100.0% | ok |
| 10 | TSMC / Taiwan Semiconductor | TSMC TSM Taiwan Semiconductor AI chips | 11/16 | 68.8% | 3 | 2 | 0.0% | 90.0% | ok |
| 11 | Micron Technology | Micron MU earnings HBM memory | 25/50 | 50.0% | 13 | 8 | 9.5% | 60.0% | ok |
| 12 | Memory stocks | memory stocks Micron HBM DRAM NAND | 7/39 | 17.9% | 63 | 35 | 0.0% | 85.7% | ok_low_relevance |
| 13 | Gold and silver mining stocks | gold silver mining stocks GDX SIL | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 14 | Chinese stocks / U.S.-listed China ADRs | Chinese stocks BABA JD PDD NIO ADR | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 15 | Iran currency / oil pressure | Iran rial currency oil exports markets | 5/50 | 10.0% | 31 | 8 | 0.0% | 60.0% | ok_low_relevance |
| 16 | Uranium stocks | uranium stocks CCJ UEC nuclear energy | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor ETF / Philadelphia Semiconductor Index — ok_no_relevant_videos
Relevance groups: `[["semiconductor ETF", "半導體 ETF", "SOX", "Philadelphia Semiconductor", "費城半導體", "00830"]]`
- Rejected: Semiconductor Index  What $10,000 Became After 10 Years #finance #investing #compoundinterest #etf
- Rejected: 미국 반도체 주가 전망 | 1년 두 배, 사상최고까지 10% | 종목분석 #반도체 #반도체ETF #마이크론
- Rejected: 주가 흔들렸던 삼성전자·하이닉스 "공급이 부족하다" (체슬리 최일호 부사장, 소현철 박사, 박세환 박사) 1부

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"], ["stock", "Synaptics", "semiconductor"]]`
- Rejected: Nike Worsening Sales; Broadcom-Anthropic Chips; Twilio to Join S&P | Stock Movers
- Rejected: Synaptics Is Being Sold for $123 Cash. What Filings Show
- Rejected: Friday's First Moves: NVDA Top Pick, HPE Upgrade, ON/SYNA Merger Update
- Rejected: Morgan Stanley Backs NVDA as Top Pick, Crude Oil & Yields Cool
- Rejected: Only 29,000 Jobs. Yields Rose Anyway. | October 2

### NIO — ok_low_relevance
Relevance groups: `[["NIO", "蔚來", "蔚来"], ["earnings", "stock", "results"]]`
- Rejected: The PULLBACK!!! Fractal Tracking: AMC / BB / MRNA / NIO / RIOT
- Rejected: SELL This Bitcoin Short Squeeze [WARNING]
- Rejected: TEN 601 | Fathom Delay Fears, Bolt Cut Back, Top Gear Caravan Smash!
- Rejected: China Confirms Nio's First Ever in Hefei 🔥 🤯
- Rejected: Robert Kiyosaki: The Truth About Money Most People Never Learn

### Memory stocks — ok_low_relevance
Relevance groups: `[["memory", "DRAM", "NAND", "HBM"], ["stocks", "Micron", "MU"]]`
- Rejected: MICRON STOCK: CHEAP OR PEAK?
- Rejected: Micron Earnings Just FORCED Wall Street to Recalculate!
- Rejected: Micron’s Earnings Were INSANE - So Why Isn’t the Stock Exploding?
- Rejected: The $1 Chip That Now Costs $3.50
- Rejected: Micron made $133B in sales. Why is it priced at 6.6x earnings? $MU deep dive

### Gold and silver mining stocks — ok_no_relevant_videos
Relevance groups: `[["gold", "silver", "mining", "miners"], ["GDX", "SIL", "stocks"]]`
- Rejected: Gold & Silver Storm Setup Is Ready! 🚨 The BIG Move May Be Closer Than You Think
- Rejected: SAMSTAGS-UPDATE: 60 $ entscheiden jetzt – Silber vor Stärke oder massivem Rücksetzer?

### Iran currency / oil pressure — ok_low_relevance
Relevance groups: `[["Iran", "Iranian rial", "rial"], ["oil", "sanctions", "currency"]]`
- Rejected: Stock Market News Today - Oct. 1, 2026
- Rejected: The Diesel Ban Is Dead. So Why Are Bond Yields Still Rising? | Week Ahead
- Rejected: US Sends Aircraft Carrier, 10,000 Troops as Iran Tensions Escalate
- Rejected: 2.5 Million Rials to $1: Inside the Economic Warfare Crushing Iran
- Rejected: 川普又要加碼打伊朗？近萬美軍增援難逼退讓 長期部署越打越疲！AI恐成紅藍鬥爭武器！川普改名SI、巨頭自管 民主黨不買單！【#寰宇全視界】20261003-完整版 謝忠岳 介文汲 介文汲 林穎佑 戴志言

