# YouTube Entity Enrichment

Generated: **2026-10-03T11:38:09.622199+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Micron Technology | Micron MU earnings memory HBM | 36/50 | 72.0% | 66 | 33 | 19.4% | 60.0% | ok |
| 2 | Nike | Nike NKE earnings outlook | 19/50 | 38.0% | 1070 | 64 | 30.0% | 30.0% | ok |
| 3 | Robinhood | Robinhood HOOD stock | 37/50 | 74.0% | 71 | 31 | 8.0% | 20.0% | ok |
| 4 | AMD | AMD earnings AI chips | 14/50 | 28.0% | 39 | 25 | 0.0% | 80.0% | ok_low_relevance |
| 5 | NIO | NIO earnings stock | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 6 | Accenture | Accenture ACN earnings AI | 22/50 | 44.0% | 22 | 22 | 0.0% | 90.0% | ok |
| 7 | Quantum computing stocks | quantum computing stocks IONQ RGTI QBTS | 8/9 | 88.9% | 26 | 26 | 0.0% | 100.0% | ok |
| 8 | Chinese stocks | Chinese stocks BABA JD PDD NIO | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | Gold and silver mining stocks | gold silver mining stocks GDX SIL | 1/5 | 20.0% | 0 | 0 | 0.0% | 100.0% | ok_low_relevance |
| 10 | Taiwan semiconductor / TSMC | TSMC TSM Taiwan Semiconductor | 28/37 | 75.7% | 7 | 6 | 0.0% | 70.0% | ok |
| 11 | Memory stocks | memory stocks Micron MU HBM DRAM NAND | 14/50 | 28.0% | 765 | 194 | 18.2% | 70.0% | ok_low_relevance |
| 12 | Semiconductor ETF / Philadelphia Semiconductor Index | Philadelphia Semiconductor Index SOX semiconductor ETF | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### AMD — ok_low_relevance
Relevance groups: `[["AMD", "Advanced Micro Devices"], ["earnings", "AI", "chip", "GPU"]]`
- Rejected: Humans Baked AI Into a Chip. What Could Go Wrong?
- Rejected: AMD Hits New Highs: Is It Too Late to Buy?
- Rejected: Semiconductor growth is exploding 🚀
- Rejected: Micron guided $61.5B. OpenAI shipped agents. AMD bought World Labs.
- Rejected: AMD Pays $8.2B in Stock for World Labs. Its Last Lab Cost $665M Cash

### NIO — ok_no_relevant_videos
Relevance groups: `[["NIO", "蔚來", "蔚来"], ["earnings", "results", "guidance"]]`
- Rejected: NIO's Biggest Opportunity! NIO STOCK ANALYSIS TODAY BUY OR SELL PRICE PREDICTION KEY LEVELS TO WATCH
- Rejected: NIO Weekly Recap Sep 27, 2026 — Stock Drops -1.1% This Week
- Rejected: The PULLBACK!!! Fractal Tracking: AMC / BB / MRNA / NIO / RIOT
- Rejected: SELL This Bitcoin Short Squeeze [WARNING]
- Rejected: Everything in Markets Is Now Moving Incredibly Fast | Odd Lots

### Gold and silver mining stocks — ok_low_relevance
Relevance groups: `[["gold", "silver"], ["mining", "miners", "stocks", "GDX", "SIL"]]`
- Rejected: Gold & Silver Storm Setup Is Ready! 🚨 The BIG Move May Be Closer Than You Think
- Rejected: KER QuickTake - Beaver Creek Takeaways, Technical Breakdown Across Gold, Silver, Copper & Energy
- Rejected: Gold & Silver Are Preparing for a Move Nobody Expected! 🚨 The Hidden Setup Is Here
- Rejected: SAMSTAGS-UPDATE: 60 $ entscheiden jetzt – Silber vor Stärke oder massivem Rücksetzer?

### Memory stocks — ok_low_relevance
Relevance groups: `[["memory", "DRAM", "NAND", "HBM"], ["stock", "stocks", "Micron", "MU"]]`
- Rejected: Micron Earnings Just FORCED Wall Street to Recalculate!
- Rejected: Micron’s Earnings Were INSANE - So Why Isn’t the Stock Exploding?
- Rejected: MICRON STOCK: CHEAP OR PEAK?
- Rejected: Micron Just CRUSHED Earnings , So Why Isn’t MU Moving?
- Rejected: Micron (MU) Q4 Earnings: $54B Record Quarter vs. CapEx Fears

### Semiconductor ETF / Philadelphia Semiconductor Index — ok_no_relevant_videos
Relevance groups: `[["Philadelphia Semiconductor", "SOX", "費城半導體", "00830"]]`
- Rejected: 주가 흔들렸던 삼성전자·하이닉스 "공급이 부족하다" (체슬리 최일호 부사장, 소현철 박사, 박세환 박사) 1부
- Rejected: 반도체가 오른 한 달, 서학개미는 거꾸로 3배를 샀어 #미국주식 #서학개미 #SOXS #shorts
- Rejected: SOXX가 SMH를 이긴 진짜 이유,엔비디아 9%인데 1년에 두 배? #SOXX #미국주식 #ETF 그리고 자신에게 맞는 저렴한 배당수익률의 ETF를 찾는 눈을 키우세요.

