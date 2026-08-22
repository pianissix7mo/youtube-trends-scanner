# YouTube Entity Enrichment

Generated: **2026-08-22T22:50:29.546184+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Semiconductor stocks | semiconductor stocks AI chips | 5/50 | 10.0% | 9 | 9 | 0.0% | 100.0% | ok_low_relevance |
| 2 | Apple earnings | Apple earnings AAPL | 0/48 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 3 | Canadian bank stocks | Canadian bank stocks earnings | 1/50 | 2.0% | 4 | 4 | 0.0% | 100.0% | ok_low_relevance |
| 4 | Tower Semiconductor | Tower Semiconductor stock TSEM | 0/20 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 5 | Robotics stocks | 機器人 股票 robotics stocks | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 6 | Webull | Webull earnings BULL stock | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 7 | Silver mining stocks | silver mining stocks | 4/50 | 8.0% | 1349 | 1164 | 66.7% | 75.0% | ok_low_relevance |
| 8 | Alibaba earnings | Alibaba earnings BABA | 16/50 | 32.0% | 160 | 41 | 8.3% | 60.0% | ok |
| 9 | Strategy / MSTR | MSTR 股票 Strategy Bitcoin | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 10 | Walmart earnings | Walmart earnings WMT | 19/50 | 38.0% | 129 | 17 | 0.0% | 30.0% | ok |
| 11 | NVIDIA earnings | NVIDIA earnings NVDA | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 12 | Yageo | 國巨 Yageo 股票 | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 13 | Ross Stores earnings | Ross Stores earnings ROST | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 14 | Evergreen Marine | 長榮 海運 股票 Evergreen Marine | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | SpaceX | SpaceX 股票 投資 | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 16 | ON Semiconductor | onsemi ON Semiconductor stock | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 17 | Moderna | Moderna MRNA stock | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 18 | TSMC | TSMC 台積電 stock semiconductor | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 19 | AI data centers | AI data center stocks NVIDIA power | —/0 | —% | — | — | —% | —% | api_failed_no_cache |
| 20 | Target earnings | Target earnings TGT | —/0 | —% | — | — | —% | —% | api_failed_no_cache |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor", "semiconductors", "chip stocks", "semiconductor stocks", "半導體股票", "半导体股票"]]`
- Rejected: This AI Stock Selloff Could Be Your Last Chance (Micron Sandisk AMD Nvidia SK Hynix Meta)
- Rejected: How Much Would an AI Crash Destroy?
- Rejected: If You Own Credo Technology Stock...You Need to Hear This!!
- Rejected: How 3 Harvard dropouts built a $21 billion AI chip startup that is taking on Nvidia
- Rejected: Nvidia's $30B Intel Bet: Should You Buy INTC Too?

### Canadian bank stocks — ok_low_relevance
Relevance groups: `[["Canadian bank", "Canadian banks", "RBC", "Royal Bank", "TD Bank", "BMO", "Bank of Montreal", "Scotiabank", "CIBC", "National Bank of Canada"], ["stock", "stocks", "earnings", "shares", "equity", "銀行股", "银行股", "財報", "财报"]]`
- Rejected: Bessent's Treasury Market Intervention, Samsung, SK Hynix Buybacks | The Opening Trade 8/20/2026
- Rejected: Walmart FY2027 Q2 Earnings Release
- Rejected: Bond Market Tests Limits of Treasury Intervention
- Rejected: Can You Deduct Interest When Your ETF Pays Return of Capital?
- Rejected: If You Have Under $500,000 - DON'T Convert Your RRSP.  Do THIS Instead!

### Silver mining stocks — ok_low_relevance
Relevance groups: `[["silver"], ["miner", "miners", "mining"], ["stock", "stocks", "shares", "equity", "investment", "investing"]]`
- Rejected: Rick Rule Evaluates 8 Mining Stocks: What He Likes, What He Doesn't
- Rejected: THIS is BIG! 💥💥 COMMODITY BULL MARKET "Get Long & Buckle Up!" (Billionaire Shift) - Silver & Gold
- Rejected: Gold and Silver Miners: Are They Ready to Break Out?
- Rejected: ERIC YEUNG | Why the miners will become the new MAG-7!
- Rejected: Everything You Need to Know About This Silver & Gold Rally

### Evergreen Marine — ok_no_relevant_videos
Relevance groups: `[["Evergreen Marine", "長榮海運", "长荣海运", "長榮航運", "长荣航运"]]`
- Rejected: 運價高檔、地緣政治干擾不斷！別只看貨櫃三雄，拆解航運冷鏈與關鍵零組件的真正贏家！#台股 #航運股 #陽明 #萬海 #長榮 #散裝航運 #冷鏈物流 #小資理財
- Rejected: 貨櫃三雄飆漲後怎麼選？避開航運景氣循環波動，鎖定越運越賺的船用設備贏家！#台股 #航運股 #陽明 #萬海 #長榮 #船用設備 #低基期飆股 #小資理財
- Rejected: 運價飆高、萬海半年報淨利狂增 96%！別只看貨櫃三雄，拆解 40 元以下設備零組件贏家！#台股 #航運股 #萬海 #陽明 #長榮 #運價飆漲 #旺季效應 #小資理財

