# YouTube Entity Enrichment

Generated: **2026-10-05T12:19:39.644212+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Quantum computing stocks | quantum computing stocks RGTI IONQ QBTS QUBT | 8/9 | 88.9% | 30 | 30 | 0.0% | 100.0% | ok |
| 2 | Alphabet / Google | Alphabet Google GOOGL stock AI | 25/46 | 54.3% | 11 | 11 | 0.0% | 90.0% | ok |
| 3 | AMD | AMD earnings AI chips | 9/50 | 18.0% | 15 | 15 | 0.0% | 100.0% | ok_low_relevance |
| 4 | Micron Technology | Micron MU earnings memory HBM | 12/50 | 24.0% | 8 | 8 | 0.0% | 90.0% | ok_low_relevance |
| 5 | ON Semiconductor | ON Semiconductor ON stock | 5/50 | 10.0% | 5 | 5 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Nike | Nike NKE earnings call | 10/50 | 20.0% | 253 | 60 | 0.0% | 70.0% | ok_low_relevance |
| 7 | TSMC | TSMC TSM Taiwan Semiconductor stock | 26/31 | 83.9% | 15 | 12 | 0.0% | 90.0% | ok |
| 8 | Navitas Semiconductor | Navitas Semiconductor NVTS stock GaN SiC | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Figure AI | Figure AI humanoid robots | 17/50 | 34.0% | 431 | 247 | 25.0% | 60.0% | ok |
| 10 | U.S. AI policy / AI czar | Trump AI czar Jay Clayton AI policy | 30/50 | 60.0% | 21 | 8 | 10.0% | 30.0% | ok |
| 11 | Delta Electronics | Delta Electronics 2308 AI power data center | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 12 | Semiconductor manufacturing capacity | semiconductor plant manufacturing capacity US chips | 1/50 | 2.0% | 7 | 7 | 0.0% | 100.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### AMD — ok_low_relevance
Relevance groups: `[["AMD", "Advanced Micro Devices"], ["earnings", "results", "AI", "chips"]]`
- Rejected: AMD Stock: What Makes Server CPU Design Irreplaceable
- Rejected: Synopsys, OpenAI develop NEW AI model for chip design work
- Rejected: MICRON, AMD & NVIDIA INVESTORS… THE MADNESS IS ABOUT TO BEGIN!
- Rejected: NVIDIA Made Me Rich. I'm Buying This Stock Next.
- Rejected: AMD Aktie 2026: Überbewertet trotz KI-Boom? | AMD Aktienanalyse, Fair Value & Kursziel

### Micron Technology — ok_low_relevance
Relevance groups: `[["Micron", "MU"], ["earnings", "memory", "HBM", "DRAM", "記憶體"]]`
- Rejected: Micron Stock Will Hit $2,000 Sooner Than You Think
- Rejected: Fear Is Creating The Opportunity In Micron Stock ($MU)
- Rejected: MICRON STOCK: CHEAP OR PEAK?
- Rejected: Micron's Revenue Went Up 379% in One Year. Here's Why.
- Rejected: Micron's Record Year, Explained: $85B Profit, But Is MU Overpriced?

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: Stock Daily - October 05, 2026
- Rejected: Semiconductor growth is exploding 🚀
- Rejected: Stock Market Update 10/4 3Ts and Semiconductor Stocks to Watch
- Rejected: Micron Stock This Week Could Change Everything ($MU)
- Rejected: The Money’s Moving: Semiconductor Suppliers Next After HBM? Are Power Stocks Back? | Lee Chang-dae

### Nike — ok_low_relevance
Relevance groups: `[["Nike", "NKE"], ["earnings", "earnings call", "results"]]`
- Rejected: NIKE (NKE Stock): KEEPS GETTING WORSE!
- Rejected: NKE: Why Nike's Inventory Turns Carry More Weight Than the Multiple
- Rejected: Nike pays $1.64 but guides to $1.15–1.35 EPS | NKE
- Rejected: Nike Just Hit a 1-Year Low. I Own It. #shorts #stocks #nike
- Rejected: Nike (NKE) Q1 2027: A Forensic Financial Audit

### Navitas Semiconductor — ok_no_relevant_videos
Relevance groups: `[["Navitas Semiconductor", "Navitas", "NVTS"], ["GaN", "SiC", "semiconductor", "stock"]]`
- Rejected: NVTS再迎催化：美军10kV项目、英伟达800V与Claros，何时兑现收入？

### Semiconductor manufacturing capacity — ok_low_relevance
Relevance groups: `[["semiconductor plant", "semiconductor manufacturing", "chip fab", "fab", "foundry"]]`
- Rejected: Chip Shortage: 20 Years of US Chip Factories, Measured
- Rejected: Why a Chip Factory Can Spend Billions Chasing a Market That Changes First
- Rejected: Inside America's $66 Billion Bet To Beat China's Shipbuilding Empire
- Rejected: Intel Made the Chips Everyone Needed — Then Lost the Future
- Rejected: Tata Semiconductor Dholera 2026 | ₹91,000 Crore Mega Project | India’s Chip Hub?

