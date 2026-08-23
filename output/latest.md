# YouTube Entity Enrichment

Generated: **2026-08-23T09:47:56.244844+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NVIDIA earnings | NVIDIA NVDA 财报 | 11/50 | 22.0% | 43 | 37 | 20.0% | 90.0% | ok_low_relevance |
| 2 | Walmart earnings | Walmart WMT 财报 | 8/22 | 36.4% | 27 | 27 | 25.0% | 100.0% | ok |
| 3 | Robinhood | Robinhood HOOD 美股 | 7/13 | 53.8% | 56 | 56 | 0.0% | 100.0% | ok |
| 4 | indie Semiconductor | indie Semiconductor INDI 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 5 | Silver mining stocks | 白银 矿业 股 silver miners | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 6 | Tesla | Tesla TSLA 美股 | 35/50 | 70.0% | 409 | 187 | 24.1% | 70.0% | ok |
| 7 | IREN earnings | IREN 财报 AI data center | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 8 | Navitas Semiconductor | Navitas Semiconductor NVTS 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | Evergreen Marine | 长荣海运 2603 股票 | 4/4 | 100.0% | 322 | 43 | 0.0% | 75.0% | ok |
| 10 | TECO Electric & Machinery | 东元 1504 股票 AI 数据中心 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 11 | Moderna | Moderna MRNA 美股 | 41/50 | 82.0% | 18 | 16 | 7.7% | 80.0% | ok |
| 12 | TSMC | 台积电 TSMC | 38/50 | 76.0% | 1357 | 430 | 30.0% | 20.0% | ok |
| 13 | ON Semiconductor | ON Semiconductor ON 美股 | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 14 | Semiconductor stocks | 半导体 美股 AI chips | 0/20 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | Nanya Plastics | 南亚 1303 股票 | 3/8 | 37.5% | 15 | 15 | 0.0% | 100.0% | ok |
| 16 | Yang Ming Marine Transport | 阳明海运 2609 股票 | 4/4 | 100.0% | 121 | 121 | 0.0% | 100.0% | ok |
| 17 | Canadian bank stocks | 加拿大 银行股 Canadian bank stocks | 1/15 | 6.7% | 320 | 320 | 0.0% | 100.0% | ok_low_relevance |
| 18 | Binance Agent OS | Binance Agent OS AI 交易 | 3/8 | 37.5% | 5 | 5 | 0.0% | 100.0% | ok |
| 19 | AI agents | AI Agent 美股 | 0/42 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 20 | SpaceX | SpaceX 美股 投资 | 33/50 | 66.0% | 175 | 132 | 10.0% | 90.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### NVIDIA earnings — ok_low_relevance
Relevance groups: `[["NVIDIA", "NVDA", "英伟达", "輝達", "辉达"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 美股一周总结｜回调风险升温？下周3大重磅事件来袭，特斯拉该卖吗？｜#英伟达｜#特斯拉｜#美股｜#股票｜JohnLu谈股 #股票分析
- Rejected: NVDA 還會漲嗎？未來 5 大關鍵找到了！【方舟運算 - 大俠武林】
- Rejected: NVIDIA如果再創新高，為什麼投資人反而要小心？
- Rejected: 超超超详细拆解#比特币74000 #英伟达 210关键多头阵地争夺！！🔥🔥处暑时节㊗️新老朋友秋日大丰收！ #美股趋势分析 #加密币 #比特币怎么玩 #技术分析教学 #均线 #股票當沖 #nvda
- Rejected: Why NVIDIA's 11.5% Growth Isn't the Bear Case You Think

### Silver mining stocks — ok_no_relevant_videos
Relevance groups: `[["silver", "白银", "白銀"], ["miner", "miners", "mining", "矿业", "礦業", "矿商", "礦商"]]`
- Rejected: 【全集】💎陈峰遭合伙好友暗算夺走金矿，被千元打发，母亲重病受尽周遭白眼。觉醒淘金系统后不断发掘珍稀矿产，创立公司碾压各路敌人，协助警方侦破走私案件，落魄矿工蜕变为威震一方的矿业大佬#短剧 #短劇

### IREN earnings — ok_no_relevant_videos
Relevance groups: `[["IREN", "Iris Energy"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 經濟學人 2026.08.22「商業版塊」解析：🇨🇳中國砸重金包圍全球供應鏈！AI 準備接管世界金融體系？Meta 迎來千億美金世紀大審判！企業砸錢買AI竟淪為一場空❓｜TheEconomist
- Rejected: “消失”的万亿债务：深扒数据中心“影子借贷”、GPU金融化与次贷风险
- Rejected: AI业务暴增181%！这只股票从$902跌到$600，我开始关注了. SiTime现在到底值不值得买？
- Rejected: 【下班國際線】台股千點殺完了？台積電、聯發科誰才是贏家？艦長程正樺：這2族群成AI新黑馬！ft.程正樺 Ep.64路怡珍 @TheStormMedia
- Rejected: 英偉達這1050億合約瘋了？揭秘 AI 盛世下隱藏的「信用騙局」！

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "ON Semi"]]`
- Rejected: 半导体止跌！内存、光通信今天能不能抄底？#美股 #美股直播  #美股行情 #美股分析 #半导体 #科技股 #内存 #存储芯片 #光通信 #AI #AI芯片 #西部数据 #美光 #AMD
- Rejected: 美股还能追吗？黄金、AI与中概股全面复盘｜GDX、NVDA、MU、BABA
- Rejected: 財政部出手救美債，美股止跌是陷阱？費半破萬二、AI晶片估值爆殺！莫德納噴177%軋空大屠殺，特斯拉是下一檔暴漲的？
- Rejected: AI业务暴增181%！这只股票从$902跌到$600，我开始关注了. SiTime现在到底值不值得买？
- Rejected: SK Hynix、Micron、NVIDIA、Tesla、Apple走势解析！AI科技股开始分化？｜US Stock Market Live【美股直播】Ep.037｜26.08.2026

### Semiconductor stocks — ok_no_relevant_videos
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半導體", "半导体"]]`
- Rejected: 美股还能追吗？黄金、AI与中概股全面复盘｜GDX、NVDA、MU、BABA
- Rejected: 財政部出手救美債，美股止跌是陷阱？費半破萬二、AI晶片估值爆殺！莫德納噴177%軋空大屠殺，特斯拉是下一檔暴漲的？
- Rejected: 放水上漲！年底要發財，這些股票必須提前佈局！
- Rejected: AI晶片狂歡終結？指數大漲背後，資金竟在暗中暴逃…
- Rejected: 芯片格局今夜改写！Moderna引爆AI医疗变局！财政部救市真相曝光，美股下一步怎么走？#美股#美股分析#莫德纳#Moderna#英伟达#博通#AI医疗#癌症疫苗#美联储#美股大跌#美股暴涨#美股散户

### Canadian bank stocks — ok_low_relevance
Relevance groups: `[["Canadian bank", "Canadian banks", "加拿大银行", "加拿大銀行", "RBC", "TD Bank", "BMO", "Scotiabank", "CIBC"]]`
- Rejected: 放水上漲！年底要發財，這些股票必須提前佈局！
- Rejected: U.S. economy is losing momentum: Rosenberg
- Rejected: 连续跌跌跌跌跌！｜ 空头太强，多头无力，这是最后防线！｜ 第1838期「幂笈投资」2026 moomoo
- Rejected: 命理師把日期講死了：九月和十二月防大震，這種點名到月份的預警，過去對過幾次？
- Rejected: FAULTLINE | THRILLER | Full Movie in English

### AI agents — ok_no_relevant_videos
Relevance groups: `[["AI agent", "AI agents", "agentic AI", "智能体", "智能體", "AI代理"]]`
- Rejected: Michael Burry做空NBIS ，三大逻辑到底是什么？｜Neocloud基本面｜AI融资分析
- Rejected: 【漫話美股公司】華爾街把你的股票帳戶交給了AI！24小時自動炒股狂攬超額收益，還是半夜閃崩清空錢包的終極陷阱？！AI the Keys to Your Portfolio
- Rejected: 一次搞懂Token與API：AI到底怎麼運作、怎麼計費？Understanding Tokens and APIs: How Does AI Work and How Is It Billed?
- Rejected: Google发明了AI时代，却为什么没能定义AI时代？
- Rejected: 美國財政部救美債！美股先撐不住？殖利率壓不住的風險，正在轉向美元與黃金？｜盤中速解讀 2026/08/20

