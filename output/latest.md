# YouTube Entity Enrichment

Generated: **2026-09-14T12:31:49.506689+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | AI slowdown / AI capex caution | AI slowdown AI capex Nvidia semiconductors | 1/5 | 20.0% | 4 | 4 | 0.0% | 100.0% | ok_low_relevance |
| 2 | iShares Semiconductor ETF / SOXX | SOXX iShares Semiconductor ETF | 1/3 | 33.3% | 1 | 1 | 0.0% | 100.0% | ok |
| 3 | Quantum computing stocks | quantum computing stocks IONQ RGTI QBTS QUBT | 9/10 | 90.0% | 6 | 6 | 0.0% | 100.0% | ok |
| 4 | Robinhood Markets | Robinhood HOOD stock | 22/50 | 44.0% | 119 | 82 | 22.2% | 70.0% | ok |
| 5 | Navitas Semiconductor | Navitas Semiconductor NVTS stock GaN power | 3/3 | 100.0% | 37 | 37 | 0.0% | 100.0% | ok |
| 6 | Uranium stocks | uranium stocks nuclear energy CCJ UEC | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 7 | OpenAI / Hugging Face incident | OpenAI Hugging Face incident AI agents hack | 8/50 | 16.0% | 9 | 9 | 12.5% | 100.0% | ok_low_relevance |
| 8 | Ukraine attacks on Russian energy / oil | Ukraine Russian oil refineries diesel Trump markets | 18/50 | 36.0% | 1759 | 1322 | 57.1% | 30.0% | ok |
| 9 | Gold stocks / gold | gold stocks gold price Fed rates | 47/50 | 94.0% | 2004 | 1039 | 50.0% | 20.0% | ok |
| 10 | Semiconductor supply chain | semiconductor supply chain AI chips manufacturing | 1/50 | 2.0% | 112 | 112 | 0.0% | 100.0% | ok_low_relevance |
| 11 | Yageo | Yageo 國巨 AI server components | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 12 | IREN | IREN stock AI cloud neocloud | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 13 | Oracle layoffs / AI transformation | Oracle ORCL layoffs AI cloud | 2/5 | 40.0% | 88 | 88 | 0.0% | 100.0% | ok |
| 14 | Alphabet / Google | Google Alphabet GOOG GOOGL stock cloud AI | 4/7 | 57.1% | 26 | 26 | 0.0% | 100.0% | ok |
| 15 | Oil prices / energy inflation | oil prices Saudi pipeline Iran diesel inflation | 13/50 | 26.0% | 1836 | 9 | 14.3% | 40.0% | ok_low_relevance |
| 16 | TSMC | TSMC TSM Taiwan Semiconductor AI chips | 10/11 | 90.9% | 50 | 37 | 0.0% | 90.0% | ok |
| 17 | onsemi | onsemi ON Semiconductor stock | 2/6 | 33.3% | 23 | 23 | 0.0% | 100.0% | ok |
| 18 | indie Semiconductor | indie Semiconductor INDI stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### AI slowdown / AI capex caution — ok_low_relevance
Relevance groups: `[["AI slowdown", "AI spending slowdown", "AI capex", "AI development slowdown"]]`
- Rejected: Xi Pitches AI Vision as Silicon Valley Leaders Tap Brakes
- Rejected: AI Chiefs Call for Slower Model Development
- Rejected: Схлопнется ли пузырь? Что покупать в сентябре? – главные инсайты сезона отчетности и разбор бигтехов
- Rejected: SOXL 하이닉스 급락한 이유, AI 개발 멈추자는 CEO들, 반도체에 무슨 일이? 금값 뜻밖의 호재 터졌다 곧 상상도 못할 일 TQQQ QLD 월가 미국주식｜존버나드 지식자랑

### OpenAI / Hugging Face incident — ok_low_relevance
Relevance groups: `[["OpenAI", "Hugging Face"], ["incident", "hack", "breach", "cyberattack", "agent"]]`
- Rejected: 700 AI Agents Hacked A Real Company — Here's The Bill
- Rejected: How OpenAI Agents Broke Into Hugging Face
- Rejected: 700 OpenAI agents hacked Hugging Face to cheat on a test
- Rejected: I Read OpenAI’s Hacking Report. The Implications Are Alarming | Threat Wire
- Rejected: OpenAI President Greg Brockman on Doing Business in the Wake of Hugging Face

### Semiconductor supply chain — ok_low_relevance
Relevance groups: `[["semiconductor supply chain", "chip supply chain", "semiconductor manufacturing", "半導體製程"]]`
- Rejected: How China Closed a 30-Point AI Gap in 3 Years (Nobody Saw This Coming)
- Rejected: Why The U.S. AI Chip Ban on China Just Backfired
- Rejected: The Chip War: Why The World’s Most Advanced Tech Is A Threat
- Rejected: The 100-Mile Strait Protecting the Global Tech Supply Chain
- Rejected: The Silicon Bottleneck: The Physics and Economics of Global Chip Dependence

### IREN — ok_no_relevant_videos
Relevance groups: `[["IREN", "IREN Ltd"]]`
- Rejected: The AI boom needs infrastructure. ⚡🤖
- Rejected: The AI doom post passed 100M views. Power and rates are the real risk. | Ep. 56
- Rejected: Dot-Com Autopsy: Using the 2000 Stock Market Crash To Predict AI Bubble Winners and Losers

### Oil prices / energy inflation — ok_low_relevance
Relevance groups: `[["oil", "Brent", "WTI", "diesel"], ["Saudi", "Iran", "pipeline", "inflation", "energy"]]`
- Rejected: U.S. fuel prices climb as Middle East fighting escalates
- Rejected: Bloomberg This Weekend | Pacing The AI Frontier, Oil & Gas Prices Rising
- Rejected: European Tech Stocks Hit by AI Boss Risk Warnings
- Rejected: AI Chiefs Call for Slower Model Development
- Rejected: AI Leaders Call For Development Slowdown as Safety Fears Mount

