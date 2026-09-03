# YouTube Entity Enrichment

Generated: **2026-09-03T11:31:44.988556+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Broadcom earnings | Broadcom AVGO 财报 | 30/50 | 60.0% | 479 | 62 | 29.2% | 60.0% | ok |
| 2 | Dell earnings | Dell DELL 财报 AI server | 16/50 | 32.0% | 17 | 17 | 6.2% | 100.0% | ok |
| 3 | Rezolve AI earnings | Rezolve AI RZLV 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 4 | NIO earnings | NIO 蔚来 财报 | 2/5 | 40.0% | 232 | 232 | 0.0% | 100.0% | ok |
| 5 | Palo Alto Networks earnings | Palo Alto PANW 财报 | 6/15 | 40.0% | 6 | 6 | 0.0% | 83.3% | ok |
| 6 | Snowflake earnings | Snowflake SNOW 财报 AI | 4/14 | 28.6% | 107 | 107 | 0.0% | 100.0% | ok_low_relevance |
| 7 | Silver mining stocks | silver mining stocks 白银矿业股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 8 | VanEck Semiconductor ETF / SMH | SMH VanEck Semiconductor ETF 半导体 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | SEMICON Taiwan 2026 | SEMICON Taiwan 2026 半导体 展 | 17/50 | 34.0% | 1489 | 187 | 33.3% | 10.0% | ok |
| 10 | MediaTek | 联发科 MediaTek 2454 AI chip | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 11 | Quantum computing stocks | quantum computing stocks 量子计算 美股 | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 12 | Grab | Grab GRAB 股票 | 26/50 | 52.0% | 252 | 148 | 19.0% | 60.0% | ok |
| 13 | Zscaler earnings | Zscaler ZS 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 14 | HPE earnings | HPE 财报 Oracle AI data center | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 15 | MongoDB earnings | MongoDB MDB 财报 | 1/6 | 16.7% | 202 | 202 | 0.0% | 100.0% | ok_low_relevance |
| 16 | Netskope earnings | Netskope earnings cybersecurity | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 17 | Credo earnings | Credo CRDO 财报 AI networking | 2/2 | 100.0% | 20766 | 270 | 0.0% | 50.0% | ok |
| 18 | Oil stocks | oil stocks 原油 美股 | 1/43 | 2.3% | 416 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 19 | Micron Taiwan labor dispute | Micron MU 台湾 罢工 美光 | 1/2 | 50.0% | 5081 | 5081 | 100.0% | 100.0% | ok |
| 20 | Apple iPhone 18 launch | Apple AAPL iPhone 18 launch September 9 | 25/50 | 50.0% | 1190 | 378 | 46.7% | 40.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Snowflake earnings — ok_low_relevance
Relevance groups: `[["Snowflake", "SNOW"], ["earnings", "earnings call", "财报", "財報", "results", "guidance"]]`
- Rejected: 博通AI收入增221%，Snowflake产品收入增37%，预期决定价格 | 9月2日
- Rejected: AI股一夜变天：Snowflake暴涨20%，Credo暴跌20%，Palantir业绩炸裂为何也跌？普通人选股看这3项#美股 #AI股票#美股分析#人工智能
- Rejected: Snowflake盘后暴涨20%！AI终于开始真正赚钱了
- Rejected: 陈老板的饼甜又香！NaNa说美股(2026.09.02)
- Rejected: SaaS末日已过？深度复盘微软、CRM、PLTR、APP基本面，AI智能体如何重塑软件股估值！

### Quantum computing stocks — ok_no_relevant_videos
Relevance groups: `[["quantum computing stocks", "quantum stocks", "量子计算", "量子計算"]]`
- Rejected: 💥全網首發💥｜【首富逆襲：我靠24小時記憶富可敵國】重生搶佔24小時記憶，中樂透做神操作，狂斂萬億打造商業帝國！#转职 #覺醒 #new  #重生 #奇幻 #熱血 #逆襲 #動漫 #男頻

### MongoDB earnings — ok_low_relevance
Relevance groups: `[["MongoDB", "MDB"], ["earnings", "earnings call", "财报", "財報", "results"]]`
- Rejected: Snowflake 盤後暴升兩成，MongoDB 同 Palo Alto 業績後慘跌雙位數？！市場唔單止要 Beat 仲要 Acceleration！揭秘美股 SaaS 業績大分化真相！
- Rejected: 秃瓢盘后 | 贝森特一句话引爆美债血洗！#dell  暴拉 vs #mdb 闪崩：滞胀阴影下的美股绝密暗战
- Rejected: 尽早入场！这三支股票可能在2030年前造就百万富翁……（请做好准备）
- Rejected: [GI TW 晚盤] 2026-09-02 美股開盤前氣氛偏弱，高利率牽制科技股，資金轉向能源與基本面較穩個股。
- Rejected: 戴尔拿下609亿美元AI服务器订单，问题不在需求 | 9月1日

### Oil stocks — ok_low_relevance
Relevance groups: `[["oil stocks", "energy stocks", "原油股", "石油股"]]`
- Rejected: 台股重挫！美股真正風險不是戰爭？油價、美債殖利率與非農才是關鍵｜盤中速解讀 2026/09/02
- Rejected: 油价狂飙，美债暴跌！中东战火撕裂美股流动性，AI牛市还在吗？#usstocks #inflation #crudeoil #iran
- Rejected: 美股直播08/31[早盘] 中东战事升级, 石油 / VIX 反弹 今天日内多空趋势如何判断?周一美股新闻与分析总汇
- Rejected: Silas走势研判：原油行情启动！
- Rejected: 特朗普的"100年石油协议"? 19美元拿下600亿桶, 5%美债竟跑不赢印钞! #特朗普 #黄金 #美元 #美债 #油价 #委内瑞拉 #加拿大 #美股 #通胀 #投资

