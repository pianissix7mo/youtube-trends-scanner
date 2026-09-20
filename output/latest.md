# YouTube Entity Enrichment

Generated: **2026-09-20T11:34:18.536274+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Jev AI | Jev AI decision model | 50/50 | 100.0% | 4500 | 493 | 43.8% | 10.0% | ok |
| 2 | Lennar | Lennar LEN earnings | 13/23 | 56.5% | 19 | 18 | 0.0% | 90.0% | ok |
| 3 | UMC | UMC UMC stock 聯電 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 4 | Circle Internet Group | Circle CRCL stock | 10/18 | 55.6% | 24 | 24 | 20.0% | 100.0% | ok |
| 5 | Tower Semiconductor | Tower Semiconductor TSEM | 2/5 | 40.0% | 3 | 3 | 0.0% | 100.0% | ok |
| 6 | Nike | Nike NKE earnings | 31/50 | 62.0% | 188 | 88 | 13.0% | 40.0% | ok |
| 7 | Amazon | Amazon AMZN earnings | 23/50 | 46.0% | 22 | 23 | 10.0% | 90.0% | ok |
| 8 | Micron Technology | Micron MU earnings | 26/50 | 52.0% | 102 | 87 | 30.4% | 90.0% | ok |
| 9 | TSMC | TSMC TSM semiconductor | 8/50 | 16.0% | 9 | 5 | 0.0% | 87.5% | ok_low_relevance |
| 10 | Semiconductor supply chain | semiconductor supply chain AI chips | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Marvell Technology | Marvell MRVL earnings | 13/22 | 59.1% | 27 | 22 | 0.0% | 80.0% | ok |
| 12 | AMD | AMD earnings AI chips | 15/50 | 30.0% | 20 | 20 | 33.3% | 100.0% | ok |
| 13 | CoreWeave | CoreWeave CRWV earnings | 23/37 | 62.2% | 41 | 35 | 5.0% | 70.0% | ok |
| 14 | Alphabet | Google GOOGL stock | 41/50 | 82.0% | 315 | 258 | 30.4% | 60.0% | ok |
| 15 | NVIDIA | NVIDIA NVDA earnings | 37/50 | 74.0% | 40 | 22 | 11.1% | 30.0% | ok |
| 16 | Uber | Uber UBER earnings | 26/50 | 52.0% | 6023 | 1038 | 55.6% | 10.0% | ok |
| 17 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 5/6 | 83.3% | 26 | 26 | 0.0% | 100.0% | ok |
| 18 | Tesla | Tesla TSLA earnings | 32/50 | 64.0% | 1093 | 17 | 18.8% | 0.0% | ok |
| 19 | Oil prices | oil price crude oil stocks | 32/50 | 64.0% | 1348 | 23 | 12.5% | 10.0% | ok |
| 20 | Crypto regulation / CLARITY Act | CLARITY Act crypto regulation Senate | 36/50 | 72.0% | 1730 | 38 | 22.2% | 20.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "Taiwan Semiconductor", "TSM"]]`
- Rejected: 台積電"埃米級晶片"拚2030年量產 搶先英特爾！台股量能破兆站回4萬7 外資買超869億第5大｜非凡財經新聞｜20260919 #shorts
- Rejected: AI退燒了?下一波資金竟轉進這族群!!【小宇宙大爆發 】#shorts #理財
- Rejected: 魏哲家喊話「股價趕快趕上聯發科」還有2000上漲空間！台積電2奈米擴產狂衝「輾壓中國」華為苦缺產量！【關鍵時刻】張炤和
- Rejected: AI會不會退燒?潘健成揭邏輯vs信仰成關鍵..記憶體紅利看40年!#AI #股市 #台股 #半導體 #記憶體 #台積電​
- Rejected: 營收財測衝新高卻不漲？專家揭台積電這大包袱

### Semiconductor supply chain — ok_no_relevant_videos
Relevance groups: `[["semiconductor supply chain", "chip supply chain"]]`
- Rejected: ASML Just Told You the AI Chip Boom Is Not Over
- Rejected: Veteran Strategist: AI stocks to buy as semiconductors MAKE HISTORY
- Rejected: The AI Boom Has a Water Problem
- Rejected: The Hidden Bottleneck Behind Nvidia's New AI Chips
- Rejected: Who Actually Makes NVIDIA's AI Chips? #ai #aiinvesting #investing

