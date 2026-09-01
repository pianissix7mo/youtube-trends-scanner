# YouTube Entity Enrichment

Generated: **2026-09-01T23:09:51.750333+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NIO earnings | NIO 蔚来 财报 | 1/2 | 50.0% | 12 | 12 | 0.0% | 100.0% | ok |
| 2 | Dell earnings | Dell DELL 财报 | 12/50 | 24.0% | 32 | 32 | 25.0% | 100.0% | ok_low_relevance |
| 3 | Strategy / MSTR | MSTR Strategy 比特币 | 33/50 | 66.0% | 2327 | 791 | 50.0% | 40.0% | ok |
| 4 | SEMICON Taiwan / semiconductor exhibition | SEMICON Taiwan 半导体 展 | 28/50 | 56.0% | 48 | 31 | 14.3% | 40.0% | ok |
| 5 | ASE Technology | 日月光 ASE Technology 半导体 | 1/5 | 20.0% | 50565 | 0 | 0.0% | 0.0% | ok_low_relevance |
| 6 | Broadcom earnings | Broadcom AVGO 财报 | 14/46 | 30.4% | 651 | 107 | 30.0% | 60.0% | ok |
| 7 | Rezolve AI earnings | Rezolve AI RZLV 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 8 | Robinhood earnings | Robinhood HOOD 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 9 | Tesla earnings | Tesla TSLA 财报 | 3/25 | 12.0% | 148 | 148 | 0.0% | 100.0% | ok_low_relevance |
| 10 | Meta earnings | Meta META 财报 | 2/50 | 4.0% | 135 | 135 | 0.0% | 100.0% | ok_low_relevance |
| 11 | DoorDash earnings | DoorDash DASH 财报 | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 12 | NVIDIA earnings | NVIDIA NVDA 财报 | 15/50 | 30.0% | 103 | 90 | 7.1% | 90.0% | ok |
| 13 | TSMC | TSMC TSM 台积电 | 6/8 | 75.0% | 34 | 34 | 0.0% | 100.0% | ok |
| 14 | UMC | 联电 UMC 半导体 | 3/5 | 60.0% | 8 | 4 | 0.0% | 66.7% | ok |
| 15 | Magnachip Semiconductor | Magnachip MX 半导体 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 16 | Valens Semiconductor | Valens Semiconductor VLN | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 17 | U.S. semiconductor tariffs | 美国 半导体 关税 Trump | 1/12 | 8.3% | 6390 | 6390 | 100.0% | 100.0% | ok_low_relevance |
| 18 | VanEck Semiconductor ETF | SMH VanEck 半导体 ETF | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 19 | Uranium | 铀 uranium stocks 核电 | 5/7 | 71.4% | 82 | 82 | 20.0% | 100.0% | ok |
| 20 | Trump AI policy | Trump AI 政策 美股 | 0/12 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Dell earnings — ok_low_relevance
Relevance groups: `[["Dell", "戴尔", "戴爾"], ["earnings", "earnings call", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: 8月30日复盘 #美伊衝突 #美股 #美股财报 #美股入门 #美股投資 #美股分析 #特朗普 #美股趋势分析 #黄金 #英伟达 #ai #avgo #nonfarmpayroll #沃什 #btc
- Rejected: 科技圈的“广适种”：读懂戴尔40年生存密码，你就不再为技术壁垒焦虑
- Rejected: ✨【投资TALK君1481期】三个超卖的板块！大非农有多重要？2%的通胀，很难✨20260830#CPI #nvda #美股 #投资 #英伟达 #ai #特斯拉
- Rejected: 英伟达财报超预期，却遭鹰派压力！资金撤离高估值板块，两大信号决定后市，市场机会正在重新洗牌 #美股 #美股分析 #美联储 #英伟达 #科技股 #财报 #谷歌 #华尔街 #半导体 #特斯拉
- Rejected: 各擁題材+投信護航 強股誰有續航力?股債同步承壓 股市多頭亮起紅燈?台股大跳震胸舞 跟著主動ETF換股,更有保障?｜20260831(周一)股市現場(完整版)*曾鐘玉(李蜀芳×蔡明翰×謝明哲)

### ASE Technology — ok_low_relevance
Relevance groups: `[["ASE Technology", "日月光", "日月光投控"]]`
- Rejected: 原本以為 PC 市場死氣沉沉... 為何輝達與聯發科聯手的「11 萬 AI 筆電」才剛開賣就被秒殺？｜2026/08/31 (一)
- Rejected: 輝達.聯發科合作升級!輝達1100億重金投資 首度入股台灣企業 聯發科亮紅燈鎖住｜非凡財經新聞｜20260901
- Rejected: 日圓跌破160警戒升溫！鴻海、聯發科面臨日廠價格競爭壓力【8月31日】
- Rejected: CoPoS 面板級封裝｜台積電說良率還要一年，台股誰在做？

### Tesla earnings — ok_low_relevance
Relevance groups: `[["Tesla", "TSLA", "特斯拉"], ["earnings", "earnings call", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: 美股 特斯拉(TSLA) 股价要喷了？Cybercab 9/3登场！373缺口近在眼前，小心利多出尽！
- Rejected: TSLA暴涨能追吗？期权数据指示方向；利率飙升，9月美股最危险的剧本来了？｜8月31日Meow聊记 TSLA AMZN NET NBIS FIG
- Rejected: 特斯拉防守K线，不破不卖？【美股直通车】2026.08.30 #sam谈美股 #美股分析 #tsla #nvda #特斯拉 #英伟达
- Rejected: 特斯拉Robotaxi到底是不是画饼？英伟达高位放量还能拿多久？
- Rejected: 美股一周总结｜下周定牛熊？非农+博通财报双重决战，下一个爆发点会是谁？｜JohnLu谈股 #股票分析

### Meta earnings — ok_low_relevance
Relevance groups: `[["Meta", "Facebook", "脸书", "臉書"], ["earnings", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: 美股继续看反弹？TSLA买入大涨，这次反弹会到哪？NVDA财报行情真正的买点！
- Rejected: 财报越好股价越跌？AI巨头为什么开始被现金流重新定价
- Rejected: MarvelIl财报超预期却遭回调!谷歌大单要等到2029?回撤后哪里是真正的黄金坑?深度拆解 Marvell的合作，财报与估值!MRVL,GOOG#trading #投資 #美股
- Rejected: 突發！中國商務部出手：MANUS與META被迫「離婚」
- Rejected: 沃什突然放鹰，美股为何转跌？｜英伟达财报这么强，为什么还跌4.5%？

### DoorDash earnings — ok_no_relevant_videos
Relevance groups: `[["DoorDash", "DASH"], ["earnings", "results", "财报", "財報", "业绩", "業績"]]`
- Rejected: 巴倫周刊2026.8.31：從歷史找出AI風險投資時機！輝達會是下一個蘋果?比特幣衝破八萬投資風險評估，美債殖利率與新恐慌指標， AI 泡沫警告與板塊輪動，，萬豪酒店的投資價，高殖利率下投資市政債！

### U.S. semiconductor tariffs — ok_low_relevance
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"], ["tariff", "tariffs", "关税", "關稅"]]`
- Rejected: 川普再出招？電子代工五大龍頭恐面暴擊 #川普 #關稅 #電子代工 #台灣 #代工
- Rejected: 트럼프 반도체 관세 폭탄… 삼성·하이닉스에 함부로 못 때리는 이유
- Rejected: 美農民40年來最慘危機！630億美元蒸發、中國抽走大豆、加拿大卡住化肥！中印俄抱團反擊！川普打中、制印、封俄 反逼三國聯手【#環球大戰線】20260826-完整版 葉思敏 侯漢廷 苑舉正 彭華幹
- Rejected: 加拿大不當美附屬品！150萬戶電力、九成進口鉀肥全成反擊王牌！荷蘭斷供反逼安世自立門戶 12吋晶圓硬闖成功！國產化狂飆近100%【#環球大戰線】20260827-完整版 葉思敏 賴岳謙 楊永明 栗正傑
- Rejected: 不要放過美國‘’自毀長城‘’帶來的機會｜美國加速自毀長城！中國外交與金融戰局的重大戰略機遇！｜卡尼"痛苦"反美 ！中加關係是否迎來曙光？｜譚新強世界ZOOM︱Sun Channel︱20260829

### Trump AI policy — ok_no_relevant_videos
Relevance groups: `[["Trump", "特朗普"], ["AI", "artificial intelligence", "人工智能"]]`
- Rejected: ⚠️恐慌指數失靈，萬億AI泡沫還能吹多久？📉美債狂飆戳破股市繁榮假象❗️看透巴倫最新趨勢，提前避開財富收割陷阱❗️｜經濟學人 2026.08.31「財商版塊」｜TheEconomist
- Rejected: 經濟學人｜2026.08.29《財經版塊》投資高手的秘密：運氣還是性格？中國隱形大追稅隱藏何種財政危機？川普嚴打移民與慈善減稅的隱性代價？俄故意讓貨幣貶值？印度天價補貼僑民｜TheEconomist
- Rejected: 肉球日報 09/01 川普籲力挺AI資料中心、Cronos遭駭7500萬鎂、比特礦持倉逼近5%ETH
- Rejected: 美股九月魔咒｜中期選舉危與機｜100%勝率的交易機會？ #election #us #trading #stockmarket
- Rejected: 沃什突然“反了”？特朗普亲手选的美联储主席，竟要在9月加息！

