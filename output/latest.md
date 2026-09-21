# YouTube Entity Enrichment

Generated: **2026-09-21T11:33:32.216857+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Memory stocks | memory stocks Micron SanDisk | 18/39 | 46.2% | 459 | 434 | 41.2% | 90.0% | ok |
| 2 | Power semiconductors | power semiconductor stocks | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 3 | Alphabet / Google | Google GOOGL stock | 38/50 | 76.0% | 203 | 160 | 26.9% | 60.0% | ok |
| 4 | Circle Internet Group | Circle CRCL stock | 8/11 | 72.7% | 25 | 25 | 12.5% | 100.0% | ok |
| 5 | iShares Semiconductor ETF / SOXX | iShares Semiconductor SOXX | 1/4 | 25.0% | 12 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 6 | India semiconductor buildout | India semiconductor investment | 2/50 | 4.0% | 871 | 871 | 50.0% | 100.0% | ok_low_relevance |
| 7 | UMC | UMC UMC stock semiconductor | 2/8 | 25.0% | 90 | 90 | 0.0% | 100.0% | ok_low_relevance |
| 8 | Marvell Technology | Marvell MRVL earnings | 10/17 | 58.8% | 13 | 13 | 0.0% | 100.0% | ok |
| 9 | TSMC | TSMC TSM earnings | 6/13 | 46.2% | 3 | 3 | 0.0% | 100.0% | ok |
| 10 | Micron Technology | Micron MU earnings memory | 28/47 | 59.6% | 127 | 127 | 18.5% | 100.0% | ok |
| 11 | Intel | Intel INTC earnings | 18/32 | 56.2% | 19 | 19 | 6.2% | 90.0% | ok |
| 12 | Qualcomm | Qualcomm QCOM earnings | 14/18 | 77.8% | 19 | 19 | 14.3% | 100.0% | ok |
| 13 | Alphabet earnings | Google GOOGL earnings | 27/50 | 54.0% | 48 | 25 | 8.3% | 70.0% | ok |
| 14 | Mining stocks | mining stocks gold copper | 1/50 | 2.0% | 5391 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 15 | Bitcoin | Bitcoin BTC ETF | 47/50 | 94.0% | 180 | 28 | 14.8% | 20.0% | ok |
| 16 | Siri AI / Apple | Apple Siri AI | 37/50 | 74.0% | 2147 | 1701 | 56.5% | 50.0% | ok |
| 17 | Claude / Anthropic | Anthropic Claude AI | 49/50 | 98.0% | 886 | 72 | 31.0% | 30.0% | ok |
| 18 | Navitas Semiconductor | Navitas NVTS semiconductor | 4/7 | 57.1% | 20 | 20 | 0.0% | 100.0% | ok |
| 19 | Broadcom | Broadcom AVGO earnings AI | 10/19 | 52.6% | 30 | 30 | 0.0% | 100.0% | ok |
| 20 | Oil stocks | oil stocks crude oil | 31/50 | 62.0% | 4560 | 700 | 46.2% | 20.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Power semiconductors — ok_no_relevant_videos
Relevance groups: `[["power semiconductor", "功率半導體", "SiC", "GaN"]]`
- Rejected: 2 Semiconductor Stocks- Which one is winning?!
- Rejected: The AI Memory Boom Is About to Get Much Bigger!!
- Rejected: Navitas Stock Just Entered a New AI Phase — What Comes Next?
- Rejected: 2 Semiconductor Stocks Building India’s Chip Future
- Rejected: Tower Semiconductor Stock: Is the 200% Rally Just the Beginning?

### iShares Semiconductor ETF / SOXX — ok_low_relevance
Relevance groups: `[["SOXX", "iShares Semiconductor"]]`
- Rejected: QCOM Crash 5.8%! Semiconductor Rotation Explained
- Rejected: ITA: How Creation and Redemption Keeps Price Near NAV
- Rejected: 巴倫周刊2026.9.21：Anthropic估值2兆上市風險；日本金援美國天然氣電廠；巴菲特退休後波克夏權力轉移；蘋果晶片護城河，與美聯儲升息下法國債市及商業地產REITs投資機會。

### India semiconductor buildout — ok_low_relevance
Relevance groups: `[["India semiconductor", "India chip"]]`
- Rejected: 2 Semiconductor Stocks Building India’s Chip Future
- Rejected: India's Semiconductor Talent Is Finally Working for India
- Rejected: US, Japan Announce Huge $12 Billion Semiconductors Investment in India! Semicon 2.0 India
- Rejected: 2 Semiconductor Stocks- Which one is winning?!
- Rejected: Semicon India 2026 Ends With $7 Billion Investment Commitments

### UMC — ok_low_relevance
Relevance groups: `[["UMC", "聯電"]]`
- Rejected: 台股「黃」袍加身 晶片銷量翻倍 CPO軍備戰決戰磷化銦？ - 周佳和 陳唯泰 謝宗霖 蔡侑達《股動錢潮》全集 2026.09.18
- Rejected: 鴻海靠光通訊噴飛卡位1.6T交換機！「美CPO大廠助攻」成熟製程低基期大爆發 四大受惠股一次看！ - 林友銘 王榮旭 劉寶傑《寶傑點兵》20260918-2
- Rejected: 00981A配息0.63元！主動ETF領息很香，但總報酬真的比較高？｜家裡隨便聊
- Rejected: [26.09.19 주간 리포트 메타분석] "전기가 없으면 AI도 없다" : Time-to-Power 병목이 만든 8인치 슈퍼사이클과 LFP 수혜주 Top 10 #전력인프라
- Rejected: 台股「黃」袍加身 晶片銷量翻倍 CPO軍備戰決戰磷化銦？ - 周佳和 陳唯泰 謝宗霖 蔡侑達《股動錢潮》全集 2026.09.18

### Mining stocks — ok_low_relevance
Relevance groups: `[["mining stocks", "gold stocks", "copper stocks"]]`
- Rejected: MIKE MCGLONE: COPPER COULD CRASH 30%
- Rejected: Silver Jumps 3% While Copper Surges 2.2% And Gold Breaks Higher ~ Monday Market Moves
- Rejected: BREAKING! 🦍🦍 Metals Are Doing THIS! (Silver, Copper + Gold Price UPDATE)
- Rejected: +730% and the CEO Says It Hasn’t Even Started — Copper Giant’s 1.1 Billion-Tonne Bet
- Rejected: Commodities Update: Technical Analysis: GOLD, SILVER, COPPER LOOKING STRONG

