# YouTube Entity Enrichment

Generated: **2026-10-09T12:54:29.426873+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 先进封装 / CoWoS | 先进封装 台积电 CoWoS AI芯片 | 4/14 | 28.6% | 487 | 487 | 25.0% | 100.0% | ok_low_relevance |
| 2 | 人工智能代理 / Gemini Agent | Google Gemini AI agent 人工智能代理 | 5/15 | 33.3% | 88 | 88 | 0.0% | 100.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### 先进封装 / CoWoS — ok_low_relevance
Relevance groups: `[["先进封装", "先進封裝", "CoWoS", "advanced packaging", "interposer"]]`
- Rejected: 台积电Q3营收高于指引上沿，AI收入能确认吗？｜2026-10-08
- Rejected: 2026/10/6 SpaceX暴涨，台积电新高，AI格局突变！【老雷财经直播】全球资产配置|全球投资地图|中美贸易战美日、美澳稀土协议|美股财报季|美联储降息欧股财报季|日经半导体IA股港股|黄金
- Rejected: 两个月狂砸1400亿！英伟达80倍溢价疯抢小公司？黄仁勋不是横扫天下而是拼命逃命？
- Rejected: 台积电突然找上8年前放弃7nm的GFS！20亿美元协议背后，英伟达为何也给AMKR预付款？
- Rejected: 台積電為何找上美國廠商？背後訊號不簡單！ #台股分析 #台股投資 #科技股 #ai供應鏈 #半導體 #台積電

