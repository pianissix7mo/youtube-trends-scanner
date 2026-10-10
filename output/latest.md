# YouTube Entity Enrichment

Generated: **2026-10-10T12:19:20.501521+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Applied Digital（APLD）财报 | Applied Digital APLD earnings October 2026 | 43/50 | 86.0% | 89 | 78 | 7.9% | 50.0% | ok |
| 2 | Delta Air Lines（DAL）财报 | Delta Air Lines DAL Q3 earnings 2026 | 8/33 | 24.2% | 14 | 14 | 0.0% | 100.0% | ok_low_relevance |
| 3 | PepsiCo（PEP）财报 | PepsiCo PEP earnings 2026 | 40/50 | 80.0% | 33 | 23 | 0.0% | 10.0% | ok |
| 4 | NVIDIA（NVDA） | NVIDIA NVDA AI chips stock October 2026 | 28/50 | 56.0% | 49 | 18 | 20.0% | 40.0% | ok |
| 5 | Samsung Electronics 存储财报 | Samsung Electronics earnings HBM memory 2026 | 23/50 | 46.0% | 61 | 26 | 5.9% | 40.0% | ok |
| 6 | Valens Semiconductor（VLN） | Valens Semiconductor VLN stock chips 2026 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 7 | Intel（INTC）财报关注 | Intel INTC earnings semiconductor 2026 | 21/42 | 50.0% | 59 | 45 | 0.0% | 50.0% | ok |
| 8 | 台积电（TSM）财报 | TSMC TSM quarterly revenue earnings 2026 | 12/21 | 57.1% | 44 | 38 | 0.0% | 90.0% | ok |
| 9 | 氮化镓功率半导体 | gallium nitride GaN power semiconductors NVTS | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 10 | 费城半导体指数（SOX） | Philadelphia Semiconductor Index SOX chip stocks | 0/5 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | OpenAI 数学研究 | OpenAI mathematics research October 2026 | 47/50 | 94.0% | 396 | 173 | 21.1% | 50.0% | ok |
| 12 | 量子计算美股 | quantum computing stocks IONQ RGTI QBTS | 14/17 | 82.4% | 15 | 15 | 0.0% | 100.0% | ok |
| 13 | 安森美（ON） | ON Semiconductor ON stock power chips | 1/50 | 2.0% | 3591 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 14 | Aritzia（ATZ）财报 | Aritzia ATZ earnings 2026 | 5/5 | 100.0% | 26 | 26 | 0.0% | 100.0% | ok |
| 15 | VanEck Semiconductor ETF（SMH） | VanEck Semiconductor ETF SMH semiconductor | 2/11 | 18.2% | 23 | 23 | 0.0% | 100.0% | ok_low_relevance |
| 16 | Zoom（ZM）财报关注 | Zoom Communications ZM earnings 2026 | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Delta Air Lines（DAL）财报 — ok_low_relevance
Relevance groups: `[["Delta Air Lines", "Delta Airlines", "DAL"]]`
- Rejected: How Much of Delta's Profit Outlook Cut Is Fuel?｜Record Q3 2026 Revenue
- Rejected: Delta Kicks Off Q3 Earnings Season
- Rejected: 📊 Delta Q3 2026 | La Verdad del Balance: Absorbió $500M en Combustible, Descontó Deuda y Guia Fuerte
- Rejected: The Week Wall Street Almost Cracked | 7 Stories That Mattered
- Rejected: [델타 항공] 10월 9일 실적 발표! 낮아진 눈높이가 부를 어닝 서프라이즈? 목표주가 $100 도달 시나리오 총정리

### 氮化镓功率半导体 — ok_no_relevant_videos
Relevance groups: `[["gallium nitride", "GaN", "氮化镓"]]`
- Rejected: Can NVTS Reach $20 in November

### 费城半导体指数（SOX） — ok_no_relevant_videos
Relevance groups: `[["费城半导体", "費城半導體", "SOX", "Philadelphia Semiconductor"]]`
- Rejected: Semiconductor Stocks 2026: The $1.6T AI Supercycle Peak or Trap? (SOXX Outlook)
- Rejected: Nvidia: The $6 Trillion Chip King. #stockmarket #soxx #semiconductors #nvidia #smh
- Rejected: OpenAI's Revenue Just Came In $20B Light
- Rejected: 나스닥 오를 때 반도체만 -4.3%… 이번 주 반도체 무슨 일?
- Rejected: สรุปจบทันโลกหุ้น pro : Nasdaq ร่วงดิ่งเหว เทคฯ โดนเทขายหนัก หลังข่าว OpenAI ต่ำคาด 9oct2026

### 安森美（ON） — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "安森美"]]`
- Rejected: Nvidia Just Hit a Record High... But It's Still Losing to Its Own Sector
- Rejected: Teradyne Titan HP Isn’t the Answer—It Expands the Options
- Rejected: TSM Taiwan Semiconductor After 3% Drop - 3 Price Targets + Friday Predicted Opening Price? 📉
- Rejected: TSMC Just Built What Everyone Said Was Impossible
- Rejected: Trump Says Putin to Supply US With Diesel

### VanEck Semiconductor ETF（SMH） — ok_low_relevance
Relevance groups: `[["VanEck", "SMH", "Semiconductor ETF"]]`
- Rejected: I Backtested SCHD Against 24 ETFs — The Results Will Make You Rethink Everything
- Rejected: Chip stocks fell 2.8% today. 25 days this year were worse.
- Rejected: Navigating Uncertainty: Insights from Future Proof
- Rejected: Finally Some Red In The Market
- Rejected: Chip ETF or Just Buy NVIDIA? Kitchen vs Chef #Shorts

### Zoom（ZM）财报关注 — ok_no_relevant_videos
Relevance groups: `[["Zoom Communications", "Zoom Video", "ZM"]]`
- Rejected: SEC Insider Update: 33 Companies Filed New Liquidation Plans (2026-10-08)

