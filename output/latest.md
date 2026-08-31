# YouTube Entity Enrichment

Generated: **2026-08-31T13:10:44.039567+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Dell earnings | Dell DELL 财报 | 9/50 | 18.0% | 14 | 14 | 33.3% | 100.0% | ok_low_relevance |
| 2 | Amazon | Amazon AMZN 财报 | 8/50 | 16.0% | 24 | 6 | 0.0% | 87.5% | ok_low_relevance |
| 3 | Snowflake | Snowflake SNOW 财报 | 1/2 | 50.0% | 0 | 0 | 0.0% | 100.0% | ok |
| 4 | Tesla | Tesla TSLA 财报 | 10/15 | 66.7% | 336 | 165 | 25.0% | 80.0% | ok |
| 5 | Palantir | Palantir PLTR 财报 | 2/4 | 50.0% | 300 | 300 | 0.0% | 100.0% | ok |
| 6 | VanEck Semiconductor ETF | SMH 半导体 ETF | 5/15 | 33.3% | 127 | 95 | 0.0% | 80.0% | ok |
| 7 | Gold | 黄金 gold 美股 | 16/50 | 32.0% | 100 | 39 | 0.0% | 70.0% | ok |
| 8 | Trump AI policy | Trump AI 政策 | 6/50 | 12.0% | 865 | 214975 | 100.0% | 16.7% | ok_low_relevance |
| 9 | Semiconductor packaging | 半导体 封装 AI 芯片 | 2/34 | 5.9% | 307 | 307 | 0.0% | 100.0% | ok_low_relevance |
| 10 | AI agents | AI Agent 美股 | 1/50 | 2.0% | 10 | 10 | 0.0% | 100.0% | ok_low_relevance |
| 11 | NVIDIA | NVIDIA NVDA 财报 | 36/50 | 72.0% | 55 | 55 | 11.8% | 90.0% | ok |
| 12 | IREN | IREN 财报 AI 数据中心 | 4/50 | 8.0% | 59 | 59 | 25.0% | 100.0% | ok_low_relevance |
| 13 | TSMC | TSMC TSM 台积电 | 5/6 | 83.3% | 32 | 32 | 0.0% | 100.0% | ok |
| 14 | ON Semiconductor | ON Semiconductor ON 美股 | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | Navitas Semiconductor | Navitas Semiconductor NVTS | 5/6 | 83.3% | 42 | 42 | 0.0% | 100.0% | ok |
| 16 | Marvell | Marvell MRVL 财报 | 9/19 | 47.4% | 28 | 28 | 11.1% | 100.0% | ok |
| 17 | Salesforce | Salesforce CRM 财报 | 9/20 | 45.0% | 20 | 20 | 0.0% | 100.0% | ok |
| 18 | Copper | 铜 copper stocks 美股 | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 19 | Uranium | 铀 uranium stocks 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 20 | Lattice Semiconductor | Lattice Semiconductor LSCC | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Dell earnings — ok_low_relevance
Relevance groups: `[["Dell", "戴尔", "戴爾"]]`
- Rejected: 8月30日复盘 #美伊衝突 #美股 #美股财报 #美股入门 #美股投資 #美股分析 #特朗普 #美股趋势分析 #黄金 #英伟达 #ai #avgo #nonfarmpayroll #沃什 #btc
- Rejected: 英伟达财报超预期，却遭鹰派压力！资金撤离高估值板块，两大信号决定后市，市场机会正在重新洗牌 #美股 #美股分析 #美联储 #英伟达 #科技股 #财报 #谷歌 #华尔街 #半导体 #特斯拉
- Rejected: 下周非农直接影响9月加息决议 #美股 #非农就业 #美联储 #加息
- Rejected: ✨【投资TALK君1481期】三个超卖的板块！大非农有多重要？2%的通胀，很难✨20260830#CPI #nvda #美股 #投资 #英伟达 #ai #特斯拉
- Rejected: 華許放鷹 嚴防非農再添變數 不能過熱更不能過冷!和CPO同行能力抗亂流?PCB上游會不會被拖下水?｜20260831(第3/8段)股市現場*曾鐘玉(蔡明翰)

### Amazon — ok_low_relevance
Relevance groups: `[["Amazon", "AMZN", "亚马逊", "亞馬遜"]]`
- Rejected: 美股大盘与个股盘前再度迎来杀跌，暂无见底信号！美伊地缘黑天鹅突袭，WTI原油狂飙冲高逢高获利了结！黄金回落测试关键支撑节点，比特币跳水插针血洗多头，行情已至，布局开启！#美股,#比特币#黄金#原油
- Rejected: 美股一周总结｜下周定牛熊？非农+博通财报双重决战，下一个爆发点会是谁？｜JohnLu谈股 #股票分析
- Rejected: 軟件股暴漲，半導體股票11月-明年4月啟動，9月16日必須小心加息，防範黃金科技股大跌！
- Rejected: MarvelIl财报超预期却遭回调!谷歌大单要等到2029?回撤后哪里是真正的黄金坑?深度拆解 Marvell的合作，财报与估值!MRVL,GOOG#trading #投資 #美股
- Rejected: 英伟达财报超预期，却遭鹰派压力！资金撤离高估值板块，两大信号决定后市，市场机会正在重新洗牌 #美股 #美股分析 #美联储 #英伟达 #科技股 #财报 #谷歌 #华尔街 #半导体 #特斯拉

### Trump AI policy — ok_low_relevance
Relevance groups: `[["Trump", "特朗普"], ["AI", "artificial intelligence", "人工智能"]]`
- Rejected: TDS strikes again! Group of women DENY FACTS about Trump policies that help their community!
- Rejected: Immigration, Tariffs and J6ers: Destiny vs Tim Pool | Faceoff
- Rejected: MAGA Supporters Attacked With Paint at California Starbucks as Employees Refuse — Part 2/2
- Rejected: 【下班國際線】輝達營收創新高!黃仁勳最大勁敵是誰?Google等巨頭為何自研晶片?曲博揭AI晶片戰的最大贏家! ft.曲博 Ep.65路怡珍 @TheStormMedia
- Rejected: "Canada Is Not China": Susan Collins Slams Trump’s "Devastating" Tariffs on Ally

### Semiconductor packaging — ok_low_relevance
Relevance groups: `[["advanced packaging", "semiconductor packaging", "半導體封裝", "半导体封装", "先进封装", "先進封裝"]]`
- Rejected: 100%关税倒逼，AI芯片集体涨价！巨头疯狂扩产的背后，你的筹码还安全吗？  #nvda #intc #mu #fomc #aimemory #whitehouse
- Rejected: 軟件股暴漲，半導體股票11月-明年4月啟動，9月16日必須小心加息，防範黃金科技股大跌！
- Rejected: Beyond Huawei: The Rise of the Chinese Technology Stack
- Rejected: 显卡买不到的真凶:HBM,3家公司垄断了12年
- Rejected: 你的錢包正在為AI重複買單！M6 Mac mini暗藏的算力陰謀：32GB是省錢神器，還是蘋果新的收租工具？

### AI agents — ok_low_relevance
Relevance groups: `[["AI agent", "AI agents", "智能体", "智能體"]]`
- Rejected: 100%关税倒逼，AI芯片集体涨价！巨头疯狂扩产的背后，你的筹码还安全吗？  #nvda #intc #mu #fomc #aimemory #whitehouse
- Rejected: ✨【投资TALK君1481期】三个超卖的板块！大非农有多重要？2%的通胀，很难✨20260830#CPI #nvda #美股 #投资 #英伟达 #ai #特斯拉
- Rejected: 美股 沃什放鹰！加息预期升温、SOX 夜星反转、恐持续二次探底？甚至更深度回调？
- Rejected: LITE：AI光通信核心平台，CPO时代为什么它仍然领先？｜#lumentum   #lite   #美股 #ai   #光通信 #光模块 #cpo    #ocs   #英伟达 #ai数据中心
- Rejected: ✨【投资TALK君1480期】沃什意外放鹰，和贝森特对着干？半导体机会来了✨20260829#CPI #nvda #美股 #投资 #英伟达 #ai #特斯拉

### IREN — ok_low_relevance
Relevance groups: `[["IREN", "Iris Energy"]]`
- Rejected: This 1 Stock Will Run NEXT! | 下一只起飞的股票！| HelloYFi
- Rejected: 详细结构英伟达财报，AI需求增速大于产能，AI营收出现拐点，新时代浪潮刚刚开始
- Rejected: AI產業鏈大家互相欠錢......這個結構有多脆弱？( AI CC字幕 )
- Rejected: 英伟达营收暴增106%，223.3亿美元却撤出美股基金！机构到底在换仓什么？AI牛市下半场曝光
- Rejected: Nvidia 财报分析! 估值被严重低估? 循环融资需要担心吗?【美股分析】

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: 本周博通财报，美股科技心惊肉跳！会不会重演Marvell暴跌？AI 芯片最后一环大审判！#broadcom #avgo #asics #usstocks #semiconductor
- Rejected: 美股9月魔咒又来了？美联储+美债+AI财报三大调价器，各个险象环生！#broadcom #usstocks #fed #inflation
- Rejected: ✨【投资TALK君1480期】沃什意外放鹰，和贝森特对着干？半导体机会来了✨20260829#CPI #nvda #美股 #投资 #英伟达 #ai #特斯拉
- Rejected: 沃什放鷹！加息恐逼近 9月美股打防守？Nvidia業績靚 AI硬件股仍熄火？軟件股可接力？｜黃國英【美股FocUS】#黃國英 #沃什 #nvda #生物科技 #etf
- Rejected: Nvidia 财报分析! 估值被严重低估? 循环融资需要担心吗?【美股分析】

### Copper — ok_no_relevant_videos
Relevance groups: `[["copper", "铜", "銅", "copper stocks"]]`
- Rejected: 英伟达单季狂卖962亿美元！美联储新主席放鹰，9月加息概率飙到57%

