# YouTube Entity Enrichment

Generated: **2026-09-19T11:29:47.126239+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Jev AI | Jev AI | 49/50 | 98.0% | 13657 | 2915 | 73.9% | 0.0% | ok |
| 2 | Philadelphia Semiconductor / Cathay 00830 | 00830 Philadelphia Semiconductor ETF | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 3 | India semiconductor buildout | India semiconductor | 29/50 | 58.0% | 3816 | 5519 | 50.0% | 10.0% | ok |
| 4 | M31 Technology | M31 6643 stock semiconductor | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 5 | Take-Two Interactive | Take Two TTWO earnings | 3/8 | 37.5% | 369 | 369 | 33.3% | 100.0% | ok |
| 6 | ON Semiconductor | ON Semiconductor ON stock | 5/50 | 10.0% | 715 | 69 | 0.0% | 40.0% | ok_low_relevance |
| 7 | Robinhood | Robinhood HOOD earnings | 18/47 | 38.3% | 65 | 36 | 0.0% | 80.0% | ok |
| 8 | Foxconn / Hon Hai | Foxconn Hon Hai stock AI servers | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | Amazon | Amazon AMZN earnings | 17/50 | 34.0% | 24 | 13 | 7.7% | 60.0% | ok |
| 10 | Photonics stocks | photonics stocks AI data center | 3/22 | 13.6% | 24 | 14 | 0.0% | 66.7% | ok_low_relevance |
| 11 | TypeSafe AI | TypeSafe AI | 18/50 | 36.0% | 2361 | 1490 | 61.5% | 60.0% | ok |
| 12 | Lennar | Lennar LEN earnings | 26/40 | 65.0% | 23 | 19 | 0.0% | 80.0% | ok |
| 13 | Marvell Technology | Marvell MRVL earnings AI chips | 11/19 | 57.9% | 41 | 33 | 0.0% | 80.0% | ok |
| 14 | AMD | AMD earnings AI chips | 11/50 | 22.0% | 39 | 24 | 30.0% | 90.0% | ok_low_relevance |
| 15 | Yageo | Yageo 2327 stock electronics | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 16 | Uber | Uber UBER earnings | 45/50 | 90.0% | 2597 | 761 | 44.0% | 0.0% | ok |
| 17 | Grab | Grab GRAB stock | 35/50 | 70.0% | 810 | 303 | 26.9% | 30.0% | ok |
| 18 | NVIDIA | NVIDIA NVDA earnings AI chips | 29/50 | 58.0% | 34 | 23 | 26.1% | 40.0% | ok |
| 19 | Navitas Semiconductor | Navitas Semiconductor NVTS stock | 5/7 | 71.4% | 44 | 44 | 0.0% | 100.0% | ok |
| 20 | Tesla | Tesla TSLA earnings | 31/50 | 62.0% | 229 | 12 | 11.1% | 20.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON stock"]]`
- Rejected: I just bought THIS Semiconductor Stock
- Rejected: Veteran Strategist: AI stocks to buy as semiconductors MAKE HISTORY
- Rejected: The REAL REASON AI Stocks Are Falling (and 2 to BUY NOW)
- Rejected: Trump's HUGE Intel Bet: 3 Chip Stocks With Bigger Upside
- Rejected: NVTS Stock 2027: Can Navitas Semiconductor Become a Massive AI Power Stock?

### Photonics stocks — ok_low_relevance
Relevance groups: `[["photonics", "optical interconnect", "silicon photonics"]]`
- Rejected: Applied Optoelectronics (AAOI): High Speed Optical Connections for AI  | #Optoelectronics
- Rejected: CRDO Stock: Credo Just Unveiled Its Next AI Connectivity Weapon
- Rejected: CRDO Stock Just Changed the AI Connectivity Game — Here’s Why
- Rejected: Tower Semiconductor Stock: Is the 200% Rally Just the Beginning?
- Rejected: Credo Down 45% — Is It Reasonably Valued After the Crash?

### AMD — ok_low_relevance
Relevance groups: `[["AMD", "Advanced Micro Devices"]]`
- Rejected: BofA Leaks $3.2 Trillion Semiconductor Secret - 5 Stocks Leading The Next Supercycle
- Rejected: The AI Stocks Quietly Beating Nvidia
- Rejected: Nasdaq Keeps Gain After Fed Quarter-Point Hike: AI/Semiconductor Complex Dominates, Intel-SK Hynix …
- Rejected: TeraWulf and Cipher Lead as Chip Shares Rally
- Rejected: TA Masterclass: AI Don’t Care: Q4 Setup Looks Explosive

