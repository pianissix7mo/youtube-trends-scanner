# YouTube Entity Enrichment

Generated: **2026-08-25T09:49:29.243301+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Gorilla Technology earnings | GRRR Gorilla Technology 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 2 | Semiconductor ETFs | 半导体 ETF semiconductor ETF | 2/50 | 4.0% | 730 | 730 | 50.0% | 100.0% | ok_low_relevance |
| 3 | CrowdStrike earnings | CrowdStrike CRWD 财报 | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 4 | U.S. semiconductor manufacturing | 美国 半导体制造 semiconductor manufacturing | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 5 | Applied Optoelectronics | AAOI 美股 | 22/41 | 53.7% | 142 | 142 | 36.4% | 100.0% | ok |
| 6 | Disney earnings | Disney DIS 财报 | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 7 | Amazon earnings | Amazon AMZN 财报 | 2/50 | 4.0% | 254 | 254 | 0.0% | 100.0% | ok_low_relevance |
| 8 | Apple earnings | Apple AAPL 财报 | 1/25 | 4.0% | 0 | 0 | 0.0% | 100.0% | ok_low_relevance |
| 9 | NVIDIA earnings | NVIDIA NVDA 财报 | 24/50 | 48.0% | 37 | 27 | 5.0% | 70.0% | ok |
| 10 | IREN earnings | IREN 财报 AI data center | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Meta earnings | Meta META 财报 | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 12 | Memory stocks | 存储芯片 memory stocks HBM | 1/5 | 20.0% | 72 | 72 | 0.0% | 100.0% | ok_low_relevance |
| 13 | United Microelectronics | 联电 UMC 美股 半导体 | 1/2 | 50.0% | 25867 | 0 | 0.0% | 0.0% | ok |
| 14 | SpaceX | SpaceX 股票 投资 | 29/50 | 58.0% | 187 | 91 | 16.7% | 70.0% | ok |
| 15 | AI agents | AI Agent 美股 投资 | 0/48 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 16 | TSMC | 台积电 TSMC 美股 | 17/48 | 35.4% | 1167 | 599 | 50.0% | 60.0% | ok |
| 17 | ON Semiconductor | ON Semiconductor ON 美股 | 0/48 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 18 | Navitas Semiconductor | Navitas NVTS 美股 半导体 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 19 | Walmart earnings | Walmart WMT 财报 | 3/6 | 50.0% | 18 | 15 | 0.0% | 66.7% | ok |
| 20 | H-1B visa fee policy | H1B 签证 费用 科技股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor ETFs — ok_low_relevance
Relevance groups: `[["semiconductor ETF", "semiconductor ETFs", "SOXX", "SMH", "半导体ETF", "半導體ETF"]]`
- Rejected: 90%買ETF都在這犯錯!重返4萬5最後逃命波 ft. 林正峰【 小宇宙大爆發 】
- Rejected: "PBR 1.5배 밑? 미친 겁니다" 지금 삼성전자·SK하이닉스 주워 담으세요
- Rejected: 【金融市場】20260825#台股大盤跌破支撐
- Rejected: 엔비디아 주가는 7거래일 내내 떨어지는데 메모리 가격은 오르는 이유
- Rejected: SK하이닉스 ETF레버리지  ETF인버스 매매 #주식 #주식투자  #다롬컴

### CrowdStrike earnings — ok_no_relevant_videos
Relevance groups: `[["CrowdStrike", "CRWD"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 黃師傅是日選股：中國心連心化肥(1866) | 主權及長線基金對阿里配售投信任票 | DeepSeek周末半價 Minimax、智誥首當其衝 | 25-8-2026
- Rejected: 黃師傅是日選股：中國心連心化肥(1866) | 主權及長線基金對阿里配售投信任票 | DeepSeek周末半價 Minimax、智誥首當其衝 | 25-8-2026 (普)

### U.S. semiconductor manufacturing — ok_no_relevant_videos
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"], ["manufacturing", "fabrication", "fab", "fabs", "制造", "製造", "生产", "生產"]]`
- Rejected: 機器亮紅燈沒人修？中國晶片廠最怕成真#中國晶片 #ASML #中美科技戰 #半導體 #湖口老盧
- Rejected: The US Just Blacklisted BYD, Alibaba, and Baidu
- Rejected: 小米不只做手機！3nm晶片殺進AI自駕 | 小米自己做晶片！台積電3nm量產 | 手機AI汽車全包！小米打造晶片帝國 | 小米砸30億美元！3顆自研晶片一起來 | O3只是開始！小米自駕晶片全面出手
- Rejected: 毛利率衝上31%，上銀真正的成長引擎，已經不只是滾珠螺桿？
- Rejected: The Chip Map: Which Countries Really Control Semiconductors?

### Disney earnings — ok_no_relevant_videos
Relevance groups: `[["Disney", "DIS", "迪士尼"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 【漫話美股公司】迪士尼靠《動物方城市2》拯救樂園？！動物王國急補「胡蘿蔔眼鏡」新角色，是頂級IP飛輪還是炒冷飯遮掩資本開支？！
- Rejected: 巴倫周刊2026.8.24：AI浪潮引爆美國再工業化，精選10檔潛力股！跟隨頂尖基金經理人，建倉生技投資。了解GLP-1如何重塑食品板塊？從F1賽車商機與高息特別股中，打造最抗通膨的防禦組合。

### Amazon earnings — ok_low_relevance
Relevance groups: `[["Amazon", "AMZN", "亚马逊", "亞馬遜"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 美股 华尔街力挺NVDA：低估它了！MU警告：HBM远远供不应求！华尔街预测黄金目标价？SPCX多头还有戏吗？TSLA空头很强吗？SKHY、INTC、AVGO、GOOG、AAPL
- Rejected: Meta 跌跌不休! 还有救吗? 四巨头估值更新!【美股分析】
- Rejected: ENG为什么我说chanel,dior等大牌还会继续涨价？
- Rejected: 英伟达财报前夜：最危险的不是AMD，是客户开始变脸
- Rejected: 巴菲特重仓Google！AI砸下2050亿美元，暴跌后反而迎来黄金坑？          #纳斯达克 #特斯拉 #英伟达 #谷歌 #tsla #nvda #crcl #avgo #美股 #美股技术分析

### Apple earnings — ok_low_relevance
Relevance groups: `[["Apple", "AAPL", "苹果", "蘋果"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly", "earnings call"]]`
- Rejected: 美股 华尔街力挺NVDA：低估它了！MU警告：HBM远远供不应求！华尔街预测黄金目标价？SPCX多头还有戏吗？TSLA空头很强吗？SKHY、INTC、AVGO、GOOG、AAPL
- Rejected: 超級數據周砸盤？SK海力士/LITE/APPL應對邏輯，算力板塊是洗盤還是轉折？
- Rejected: 美股 跌跌何时休？英伟达AI服务器迎15%涨幅！AAPL聚焦AI与新设备！MU又要下跌？Anthropic即将登陆华尔街！TSLA、SPCX、AVGO、AMD、SOXX、SNDK、NFLX、MRVL
- Rejected: AI科技股领跌，新一轮调整行情开启了吗？8月24日盘前策略：做空AAPL，MU，SPCX #美股 #美股盘前 #美股行情 #美股分析 #盘前策略#aapl #mu#spcx
- Rejected: NVDA财报前就看空！熊市价差成功获利，这笔期权为什么敢提前布局？#nvda #美股 #美股財報 #美股分析 #期权交易 #期权

### IREN earnings — ok_no_relevant_videos
Relevance groups: `[["IREN", "Iris Energy"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 【下班國際線】台股千點殺完了？台積電、聯發科誰才是贏家？艦長程正樺：這2族群成AI新黑馬！ft.程正樺 Ep.64路怡珍 @TheStormMedia
- Rejected: What Happens When the AI Boom Stops?
- Rejected: 財報好也可能跌？英偉達之後真正要看的，是這 3 個訊號！
- Rejected: Why This Bitcoin Rally is going MUCH Higher!
- Rejected: 全家跪舔養子逼他交出科研成果，還將他扔進火海燒成毀盡！不料他重活一世看清這惡心的親情，重回豪門誓讓仇人全部陪葬！#短劇 #逆襲 #推薦 #movie

### Meta earnings — ok_no_relevant_videos
Relevance groups: `[["Meta", "Facebook", "脸书", "臉書"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: Meta 跌跌不休! 还有救吗? 四巨头估值更新!【美股分析】
- Rejected: 🚨踢爆華爾街潛規則！Meta用7層空殼藏匿250億債務？五大科技巨頭「消失的2.1萬億」驚天秘密！AI狂潮背後的次貸危機？
- Rejected: Meta一場夢蒸發6000億？暴跌70%後，點靠AI 絕地反彈？朱克伯格豪賭元宇宙到認錯，公司要賺錢，管理層有幾關鍵？【施傅教學】#Zuckerberg #公司故事
- Rejected: 川普頻繁股市交易惹議 輝達財報叫好聲四起.AI伺服器明年傳漲15% 大立光晉升輝達FAU供鏈 3年多首見!矽晶圓漲價10%｜主播鄧凱銘｜【非凡Morning Call】20260824｜非凡財經新聞
- Rejected: NVDA财报前就看空！熊市价差成功获利，这笔期权为什么敢提前布局？#nvda #美股 #美股財報 #美股分析 #期权交易 #期权

### Memory stocks — ok_low_relevance
Relevance groups: `[["memory", "DRAM", "NAND", "HBM", "存储", "存儲", "内存", "記憶體", "记忆体"]]`
- Rejected: 30年美债冲上5.23%！谷歌微软加速自研，亚马逊甲骨文却被现金流卡住#谷歌 #微软 #亚马逊 #甲骨文 #美债收益率
- Rejected: EP448｜希音估值缩水七成，东方甄选少发4亿薪酬：2026开始拼系统
- Rejected: Китай готовится завалить рынок собственной оперативной памятью
- Rejected: 长鑫上市后暴涨，国产DUV真交付了吗？三条证据拆开市场叙事

### AI agents — ok_no_relevant_videos
Relevance groups: `[["AI agent", "AI agents", "agentic AI", "智能体", "智能體", "AI代理", "AI代理人"]]`
- Rejected: 【股票】晶片巨頭搶著綁定！產能狂缺到2028，AI下半場供應鏈黑馬是他！ft.阮慕驊、廖婉婷｜下班經濟學769｜謝哲青、張珈瑄
- Rejected: Meta 跌跌不休! 还有救吗? 四巨头估值更新!【美股分析】
- Rejected: OpenAI 驚爆倒閉危機？背後 8000 億美金資金鏈恐全面崩潰！🚨 AI 泡沫終局到了？
- Rejected: 2026 AI算力芯片格局与投资机会（从GPU、CPU、云厂自研芯片到软件生态）
- Rejected: TSLA暴涨5%！马斯克AI算力计划曝光，特斯拉机器人行情要启动了？英伟达涨价15%引爆AI产业链！#美股 #股票 #股票分析 #投资 #股市  #tsla #nvda #spcx #amd

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "安森美"]]`
- Rejected: 輝達連跌5天！特斯拉卻逆勢噴發？美股本週三大重磅事件，達利歐預言「三年大危機」！哪一檔股票能追？
- Rejected: Meta 跌跌不休! 还有救吗? 四巨头估值更新!【美股分析】
- Rejected: 全网都在吹英伟达，我讲它唯一的弱点 | 软肋系列EP01
- Rejected: Intel vs AMD：AI行情谁更有爆发力？我更看好这只！ #AMD #Intel #AI #美股 #科技股 #股票
- Rejected: 美股AI牛市关键节点：PCE+英伟达财报+杰克逊霍尔沃什首秀，三大调价器各个凶险！#usstocks #bigtech #bondmarket #kevinwarsh #inflation

