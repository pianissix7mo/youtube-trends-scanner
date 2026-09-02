# YouTube Entity Enrichment

Generated: **2026-09-02T11:33:28.134515+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Dell earnings | Dell DELL 财报 AI服务器 | 7/30 | 23.3% | 27 | 27 | 14.3% | 100.0% | ok_low_relevance |
| 2 | Robinhood | Robinhood HOOD 美股 | 2/7 | 28.6% | 32 | 32 | 0.0% | 100.0% | ok_low_relevance |
| 3 | NIO earnings | NIO 蔚来 财报 | 2/5 | 40.0% | 40 | 40 | 0.0% | 100.0% | ok |
| 4 | Gold & silver miners | 黄金 白银 矿业股 gold silver miners | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 5 | Palo Alto Networks earnings | Palo Alto PANW 财报 | 1/7 | 14.3% | 6 | 6 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Semiconductor ETFs | 半导体 ETF SMH SOXX | 4/10 | 40.0% | 41 | 41 | 0.0% | 100.0% | ok |
| 7 | SEMICON Taiwan 2026 | SEMICON Taiwan 2026 半导体展 | 29/50 | 58.0% | 3136 | 293 | 25.0% | 10.0% | ok |
| 8 | Broadcom earnings | Broadcom AVGO 博通 财报 | 9/23 | 39.1% | 56 | 27 | 0.0% | 66.7% | ok |
| 9 | Snowflake earnings | Snowflake SNOW 财报 | 3/6 | 50.0% | 4 | 4 | 0.0% | 100.0% | ok |
| 10 | MediaTek | 联发科 MediaTek AI 芯片 | 18/32 | 56.2% | 23 | 12 | 0.0% | 90.0% | ok |
| 11 | Rezolve AI earnings | Rezolve AI RZLV 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 12 | MongoDB earnings | MongoDB MDB 财报 | 1/3 | 33.3% | 4 | 4 | 0.0% | 100.0% | ok |
| 13 | Credo Technology earnings | Credo CRDO 财报 AI互连 | 1/2 | 50.0% | 44 | 44 | 0.0% | 100.0% | ok |
| 14 | Medtronic earnings | Medtronic MDT 财报 | 1/2 | 50.0% | 1 | 1 | 0.0% | 100.0% | ok |
| 15 | Samsung Austin Semiconductor | Samsung Austin Semiconductor 美国晶圆厂 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 16 | Lattice Semiconductor | Lattice Semiconductor LSCC | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 17 | NVIDIA earnings | NVIDIA NVDA 财报 | 11/50 | 22.0% | 115 | 87 | 20.0% | 90.0% | ok_low_relevance |
| 18 | TSMC | TSMC TSM 台积电 | 5/9 | 55.6% | 20 | 20 | 0.0% | 100.0% | ok |
| 19 | ASE Technology | 日月光 ASE Technology 封装 | 1/4 | 25.0% | 18526 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 20 | Uranium | 铀 uranium stocks 核电 | 6/10 | 60.0% | 116 | 74 | 20.0% | 83.3% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Dell earnings — ok_low_relevance
Relevance groups: `[["Dell", "戴尔", "戴爾"], ["earnings", "earnings call", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: Dell：950亿美元AI服务器积压，自由现金流为什么只有9.86亿美元？
- Rejected: 戴尔拿下609亿美元AI服务器订单，问题不在需求 | 9月1日
- Rejected: 戴尔AI业务进入“利润释放”阶段！净利润暴增255%，股价还能涨到600美元？
- Rejected: 戴尔订单彻底爆发了，AI根本没有见顶｜609亿美元订单爆发
- Rejected: 戴尔AI服务器订单609亿美元：利润真变厚了吗？

### Robinhood — ok_low_relevance
Relevance groups: `[["Robinhood", "HOOD"]]`
- Rejected: 最近美股怎么了？不涨不跌，感觉越来越不对劲！
- Rejected: Ondas遭遇全面负面评级！详解全面差评报告！#ondas #美股 #股票 #财经 #投资 #财报 #无人机 #onds #纳斯达克 #标普500指数 #贝莱德 #etf
- Rejected: Crypto第二波？3大主流幣＋4大概念股技術分析｜BTC、ETH、SOL、COIN 邊隻上望100%-200%？【短炒啟航｜第14堂】 #MSTR #加密貨幣 #技術分析 #PriceAction
- Rejected: 秃瓢盘前 | 债券危机 | 油价继续上涨 | 股市承压
- Rejected: 悟空解资讯第167期 ：比特币期权押注10万美元，Solana交易费创新高，Strategy再买4603枚BTC，以太坊连续65周增持，赵长鹏“四不”理财原则曝光！|9月1日币圈新闻#加密货币新闻

### Palo Alto Networks earnings — ok_low_relevance
Relevance groups: `[["Palo Alto Networks", "Palo Alto", "PANW"], ["earnings", "earnings call", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: Palo+Alto买的是成长还是报表？#ai #shorts  #自由現金流 #股權稀釋 #身份安全 #盤後財報
- Rejected: 加權指數急跌 784 點收 46,164 點！三大法人賣超 1,150 億元，主本比 鎖碼#雙鴻#穩懋#合晶｜ 2026/09/03 #台股 盤前解析｜今天 Shot 這盤｜豐雲學堂直播
- Rejected: 秃瓢盘前 | 就业数据周 | #aapl 换帅 | #snow #dell #hpe 业绩发布 | 加息预期再起 | 油价暴涨
- Rejected: 戴尔拿下609亿美元AI服务器订单，问题不在需求 | 9月1日
- Rejected: 【8/31美股周报②】SpaceX观点最热闹的一集｜Sven Carlin说是「马斯克服用太空类固醇」，美投侃新闻却曝出千亿美元星舰发射基地协议

### NVIDIA earnings — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA", "英伟达", "英偉達", "辉达", "輝達"], ["earnings", "results", "财报", "財報"]]`
- Rejected: 2026/09/01(二) 輝達(NVDA)砸35億美元投資聯發科，買什麼？
- Rejected: [NVDA & SOXX] 半導體大超級週期來襲！英偉達淨利率 66% 恐怖真相：AI 產業鏈爆發性機會全解析
- Rejected: 輝達單季營收破960億！毛利率要掉到71%，但管理層親口說明年還要暴增70%？市場完全聽錯重點了?
- Rejected: 你以為錯過英偉達上漲8%很痛？！更痛的是你追進去後，才發現自己買的是後悔！
- Rejected: 油價飆升+美債暴漲壓制美股！NVDA 止跌低吸、特斯拉回踩是買點？蘋果逆勢暴漲還能加倉嗎？

### ASE Technology — ok_low_relevance
Relevance groups: `[["ASE Technology", "日月光", "日月光投控"]]`
- Rejected: 破壞性革命！輝達推高頻記憶體「NVHBM」 並排改堆疊「先進封裝」族群利多！？ - 黃世聰 吳岳展 王榮旭 劉寶傑《寶傑點兵》20260831-3
- Rejected: 原本以為 PC 市場死氣沉沉... 為何輝達與聯發科聯手的「11 萬 AI 筆電」才剛開賣就被秒殺？｜2026/08/31 (一)
- Rejected: 破壞性革命！輝達推高頻記憶體「NVHBM」 並排改堆疊「先進封裝」族群利多！？ - 黃世聰 吳岳展 王榮旭 劉寶傑《寶傑點兵》20260831-3

