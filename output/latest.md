# YouTube Entity Enrichment

Generated: **2026-09-11T11:32:03.562306+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Oracle | Oracle ORCL earnings AI cloud | 35/50 | 70.0% | 181 | 84 | 11.5% | 30.0% | ok |
| 2 | Adobe | Adobe ADBE earnings AI | 23/50 | 46.0% | 93 | 87 | 20.0% | 70.0% | ok |
| 3 | Alif Semiconductor / Analog Devices | Analog Devices ADI Alif Semiconductor acquisition | 1/3 | 33.3% | 0 | 0 | 0.0% | 100.0% | ok |
| 4 | GameStop | GameStop GME earnings | 20/50 | 40.0% | 254 | 207 | 11.1% | 80.0% | ok |
| 5 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 6 | TSMC | TSMC TSM revenue AI chips | 9/10 | 90.0% | 8 | 7 | 12.5% | 88.9% | ok |
| 7 | AeroVironment | AeroVironment AVAV earnings defense drones | 6/16 | 37.5% | 272 | 37 | 0.0% | 83.3% | ok |
| 8 | Apple Siri AI | Apple AAPL Siri AI | 11/50 | 22.0% | 6664 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 9 | Meta Muse AI | Meta META Muse AI | 46/50 | 92.0% | 1010 | 193 | 33.3% | 50.0% | ok |
| 10 | Anthropic | Anthropic Claude AI | 47/50 | 94.0% | 1671 | 190 | 30.8% | 10.0% | ok |
| 11 | OpenAI | OpenAI AI model research | 36/50 | 72.0% | 1393 | 200 | 42.9% | 40.0% | ok |
| 12 | U.S. CPI / inflation | US CPI inflation Fed rates | 17/50 | 34.0% | 2134 | 632 | 50.0% | 30.0% | ok |
| 13 | Oil prices / Iran war | oil prices Iran war stocks inflation | 28/50 | 56.0% | 3578 | 100 | 11.1% | 0.0% | ok |
| 14 | Semiconductor stocks | semiconductor stocks AI chips | 4/50 | 8.0% | 37 | 15 | 0.0% | 75.0% | ok_low_relevance |
| 15 | Energy stocks | energy stocks oil prices | 1/50 | 2.0% | 1 | 1 | 0.0% | 100.0% | ok_low_relevance |
| 16 | Silver stocks | silver stocks silver miners | 3/50 | 6.0% | 338 | 338 | 33.3% | 100.0% | ok_low_relevance |
| 17 | Meta earnings | Meta META earnings | 3/50 | 6.0% | 2612 | 2612 | 100.0% | 33.3% | ok_low_relevance |
| 18 | NVIDIA | NVIDIA NVDA earnings AI chips | 29/50 | 58.0% | 28 | 26 | 11.5% | 70.0% | ok |
| 19 | onsemi | onsemi ON semiconductor stock | 1/2 | 50.0% | 781 | 781 | 0.0% | 100.0% | ok |
| 20 | Navitas Semiconductor | Navitas Semiconductor NVTS stock GaN | 2/2 | 100.0% | 52 | 52 | 0.0% | 100.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Apple Siri AI — ok_low_relevance
Relevance groups: `[["Apple", "AAPL", "Siri"], ["AI", "Apple Intelligence", "Siri"]]`
- Rejected: iPhone Duo: Everything announced about the first foldable iPhone
- Rejected: The TRUTH About Apple's HUGE iPhone Event... Good & BAD!
- Rejected: Apple unveils new foldable iPhone Duo priced at $1,999
- Rejected: Introducing the new iPhone Duo
- Rejected: Apple Event September ’26: Recapping announcements of iPhone Duo, iPhone 18 Pro, and more

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor stocks", "chip stocks", "半导体股", "半導體股"]]`
- Rejected: Memory Stocks Fell, But The Fundamentals Just Got More Interesting!
- Rejected: PRICING GAINS: Chip shortages benefiting major semiconductor companies
- Rejected: Cathie Wood Just Bought $17 Million of This AI Chip Stock!🚨 #stockmarket #trading #ai #stocks
- Rejected: AI Stocks Lead, Blue Chips Lag In Down Session: AMD, Magnite, TVTX In Focus | Stock Market Today
- Rejected: Dan Ives’ $1 Trillion AI Prediction - 3 AI Stocks Wall Street Is Accidentally Pricing Wrong

### Energy stocks — ok_low_relevance
Relevance groups: `[["energy stocks", "oil stocks", "能源股", "石油股"]]`
- Rejected: Are We Staring At An Oil Crisis? Or Renaissance? | Doomberg
- Rejected: Oil Near $100 Tanks the Dow—But AI Stocks Split
- Rejected: Oil Breaks $100—What It Means for Your Wallet
- Rejected: You Can’t Make This Up: Markets Face a Yield & Oil Spiral
- Rejected: The Oil Paradox: $30 Oil May Be Just As Likely As $150 Oil

### Silver stocks — ok_low_relevance
Relevance groups: `[["silver stocks", "silver miners", "白银股", "白銀股"]]`
- Rejected: SILVER and GOLD 🚨 ALERT! 🚨 - This Is Happening NOW - (You BEST NOT Be Fooled)
- Rejected: 5 Producing Mines… Why Is This Silver Stock Still So Cheap? Guanajuato Silver (GSVR.V / GSVRF)
- Rejected: Copper Just Flashed a Massive Buy Signal — Gold Investors Are Looking the Wrong Way
- Rejected: Willem Middelkoop: Gold Is Poised To Hit $10,000 and Silver to $200
- Rejected: **Silver Investors!** THIS Is Finally Happening 🦍🦍 - (Major Gold Price News too)

### Meta earnings — ok_low_relevance
Relevance groups: `[["Meta"], ["earnings", "results", "guidance"]]`
- Rejected: Meta's Muse Rally and the 10 Million in Puts Betting It Fades
- Rejected: MICROSOFT & META SHARES SLIDE: Josh Brown Explains What Investors Should Watch
- Rejected: Meta's $18B Settlement Just Made Your Ads More Expensive
- Rejected: Meta Stock SHOCK — Zuckerberg Is Betting BIG on AI
- Rejected: Meta Just Launched Muse. Here's Why It's the Best AI Stock to Buy

