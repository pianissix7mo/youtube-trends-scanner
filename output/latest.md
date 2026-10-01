# YouTube Entity Enrichment

Generated: **2026-10-01T11:33:10.637334+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Google Gemini 4 Argon | Google Gemini 4 Argon GOOGL | 31/50 | 62.0% | 126 | 87 | 21.4% | 80.0% | ok |
| 2 | McDonald's GLP-1 menu investment | McDonald's MCD GLP-1 menu $8.5 billion | 1/2 | 50.0% | 37 | 37 | 0.0% | 100.0% | ok |
| 3 | U.S.-Canada trade tensions | Trump Canada trade Navarro tariffs | 8/50 | 16.0% | 18 | 18 | 0.0% | 75.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### U.S.-Canada trade tensions — ok_low_relevance
Relevance groups: `[["Trump", "Navarro"], ["Canada", "Canadian"], ["trade", "tariff", "tariffs"]]`
- Rejected: ‘No response’: PM Carney says he’ll ’take note’ of Trump, Navarro’s jabs on trade
- Rejected: JUST IN: Canada REJECTS Trump's Apology Demand As His Import Ban Takes Effect
- Rejected: ‘No response’: PM Carney says he’ll ’take note’ of Trump, Navarro’s jabs on trade
- Rejected: 'You will pay': Trump adviser warns Canada not to 'interfere' with U.S. midterms
- Rejected: ‘GET THE HELL OUT!’: Peter Navarro Threatens Canadians With ‘OUSTER’ From U.S. Amid Trump Tariff War

