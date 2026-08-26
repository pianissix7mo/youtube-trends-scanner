# YouTube Entity Enrichment

Generated: **2026-08-26T09:47:09.590603+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NVIDIA earnings | NVIDIA NVDA 财报 輝達 | 21/42 | 50.0% | 95 | 73 | 5.3% | 80.0% | ok |
| 2 | Intuit earnings | Intuit INTU 财报 | 0/3 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 3 | Semiconductor ETFs | 半导体 ETF semiconductor ETF SMH SOXX | 1/3 | 33.3% | 537 | 537 | 0.0% | 100.0% | ok |
| 4 | U.S. semiconductor manufacturing | 美国 半导体制造 芯片 manufacturing | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 5 | CrowdStrike earnings | CrowdStrike CRWD 财报 | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 6 | Bank of Nova Scotia earnings | Scotiabank BNS 财报 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 7 | Dick's Sporting Goods earnings | Dick's Sporting Goods DKS 财报 | 0/4 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 8 | Zoom earnings | Zoom ZM 财报 | 1/2 | 50.0% | 64 | 64 | 0.0% | 100.0% | ok |
| 9 | Circle Internet Group | Circle CRCL 美股 USDC | 5/5 | 100.0% | 13 | 13 | 0.0% | 100.0% | ok |
| 10 | AU Optronics | 友达 AUO 面板 股票 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 11 | Semiconductor supply chain | 半导体 供应链 semiconductor supply chain | 6/50 | 12.0% | 170 | 170 | 16.7% | 100.0% | ok_low_relevance |
| 12 | Defense stocks | 美国 军工股 defense stocks | 0/5 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 13 | Gold mining stocks | 黄金矿业股 gold mining stocks | 2/15 | 13.3% | 22 | 22 | 0.0% | 100.0% | ok_low_relevance |
| 14 | Silver mining stocks | 白银矿业股 silver mining stocks | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | AI agents | AI Agent 智能体 美股 | 0/14 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 16 | Claude AI / Anthropic | Claude AI Anthropic 美股 | 1/9 | 11.1% | 32 | 32 | 0.0% | 100.0% | ok_low_relevance |
| 17 | ON Semiconductor | ON Semiconductor ON 美股 芯片 | 0/26 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 18 | TSMC | 台积电 TSMC 半导体 | 33/50 | 66.0% | 725 | 410 | 29.4% | 20.0% | ok |
| 19 | Navitas Semiconductor | Navitas NVTS 美股 半导体 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 20 | Power semiconductors | 功率半导体 power semiconductor 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Intuit earnings — ok_no_relevant_videos
Relevance groups: `[["Intuit", "INTU", "QuickBooks", "TurboTax"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 【美股】财捷暴跌11%只是开始？800→250美元！财报越好股价越跌，AI正在掏空它的护城河？250美元到底能不能抄底？#美股 #美股分析 #财捷 #intc #财报 #暴跌 #裁员 #科技股
- Rejected: 2026/08/26(三) 美債空頭回補，科技股警報解除？
- Rejected: 中东局势骤变油价跳水，芯片股绝地大反击！DKS暴跌30%敲响消费警钟，还有哪些公司要被AI砸盘？#turbotax #quickbooks #dks

### U.S. semiconductor manufacturing — ok_no_relevant_videos
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"], ["manufacturing", "fab", "fabs", "foundry", "foundries", "制造", "製造", "晶圆厂", "晶圓廠", "reshoring"]]`
- Rejected: Chip Design से Artificial Intelligence तक, कैसे Future-Ready बन रहे हैं भारत के युवा? #NextGenBharat
- Rejected: How a Computer Chip Is Made: From Sand to Billions of Transistors #shorts #chip
- Rejected: Musk Is Betting Against 40 Years of Chip History
- Rejected: U.S. Turns Korea’s Chip Cluster Into Leverage #Semiconductors #SouthKorea
- Rejected: The US Just Blacklisted BYD, Alibaba, and Baidu

### CrowdStrike earnings — ok_no_relevant_videos
Relevance groups: `[["CrowdStrike", "CRWD"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 黃師傅是日選股：中國心連心化肥(1866) | 主權及長線基金對阿里配售投信任票 | DeepSeek周末半價 Minimax、智誥首當其衝 | 25-8-2026
- Rejected: 黃師傅是日選股：中國心連心化肥(1866) | 主權及長線基金對阿里配售投信任票 | DeepSeek周末半價 Minimax、智誥首當其衝 | 25-8-2026 (普)

### Dick's Sporting Goods earnings — ok_no_relevant_videos
Relevance groups: `[["Dick's Sporting Goods", "DICK'S", "DKS"], ["earnings", "results", "财报", "財報", "业绩", "業績", "quarterly"]]`
- Rejected: 中东局势骤变油价跳水，芯片股绝地大反击！DKS暴跌30%敲响消费警钟，还有哪些公司要被AI砸盘？#turbotax #quickbooks #dks
- Rejected: 芯片全线反弹，最惨的却是一家卖运动鞋的
- Rejected: [GI TW 晚盤] 2026-08-25 今晚美股偏科技反彈但震盪加劇，低殖利率撐起半導體買盤，財報與通膨數據仍壓抑追價。
- Rejected: 油价跌→利率降→成长股涨 英伟达止跌+2.19%  8月25日美股复盘

### Semiconductor supply chain — ok_low_relevance
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"], ["supply chain", "供应链", "供應鏈"]]`
- Rejected: The Helium Chokepoint: How a Party Balloon Gas Control the Tech War
- Rejected: 日月光一家就砸了 3,300 億... 封測五雄狂燒 4,600 億是在搶什麼大單？｜2026/08/24 (一)
- Rejected: 機器人崛起｜張振驊ft.工研院南分院執行長 周大鑫｜#shorts｜台灣大時代｜2026.08.29｜
- Rejected: 88核对决256核，还有一家交不出时间表：Nvidia、AMD、Intel争的根本不是核数
- Rejected: ST’s Third 2026 Price Hike Warns on Power Chips #Semiconductors #SupplyChain

### Defense stocks — ok_no_relevant_videos
Relevance groups: `[["defense", "defence", "aerospace and defense", "军工", "軍工", "国防", "國防"]]`
- Rejected: 美國首次重稀土商用認證！利好不斷卻腰斬一半？Energy Fuels (UUUU) 完整深度拆解
- Rejected: 【完结】與高冷校花意外一夜後她懷孕了！豪門父母百般刁難，殊不知我覺醒全能係統，化身投資之神逆襲暴富，跨越階層迎娶白富美，走上人生巔峰！#minidrama  #中國短劇#精彩大陸短劇
- Rejected: 【精選】 習近平30年前求台商投資歷史重演！美國人名片「改印繁體」再偉大只能靠台灣？！ -《寶傑怎麼說》 劉寶傑
- Rejected: 印尼KF-21毫無羞恥地再次要求降價，若這次讓步一次，其他國家肯定也會以此為先例
- Rejected: 日本一鬆手，中國高階製造就停擺：五軸工具機全世界只有3個國家做得出來，卡了中國20年

### Gold mining stocks — ok_low_relevance
Relevance groups: `[["gold", "黄金", "黃金"], ["miner", "miners", "mining", "矿业", "礦業", "矿商", "礦商", "矿股", "礦股"]]`
- Rejected: Gold price — this is my next buying level
- Rejected: Newmont Mining #stock NEM hit a new high and here is why it matters for the #goldprice and you
- Rejected: Why Most Mining Speculators Fail
- Rejected: Copper Equivalent: What Does 100m at 1% REALLY Mean ⁉️
- Rejected: FEG Idenburg Study: 390Koz @ 9.2g/t Gold Confirmed

### Silver mining stocks — ok_no_relevant_videos
Relevance groups: `[["silver", "白银", "白銀"], ["miner", "miners", "mining", "矿业", "礦業", "矿商", "礦商", "矿股", "礦股"]]`
- Rejected: MultiSUB🔥合伙开矿被兄弟背刺，一千块打发走！觉醒淘金系统疯狂挖矿，从穷光蛋逆袭成矿业巨头！

### AI agents — ok_no_relevant_videos
Relevance groups: `[["AI agent", "AI agents", "agentic AI", "智能体", "智能體", "AI代理", "AI代理人"]]`
- Rejected: OpenAI联手博通造推理芯片，英伟达垄断地位危险了？#nvidia #openai #broadcom #tsmc #semiconductor #aichips #gpu #asics
- Rejected: 輝達下一季指引多少才算驚喜？卡位AI存儲入口、鎖定算力供應鏈、開放小模型，三條新護城河能否讓NVDA再重估？
- Rejected: 美股英伟达7连跌，AI硬件很便宜，PE 跌到18倍是黄金坑还是陷阱？#nvidia #nvda #jensenhuang #usstocks #stockmarket #semiconductor
- Rejected: 英伟达财报有2810亿波动? AMD将超越英特尔再涨40%? 卖220亿算力META飙升52%? NVDA SMCI SNDK BE MRVL! 08252026 #美股 #股票 #美股分析 #投資
- Rejected: OpenAI 驚爆倒閉危機？背後 8000 億美金資金鏈恐全面崩潰！🚨 AI 泡沫終局到了？

### Claude AI / Anthropic — ok_low_relevance
Relevance groups: `[["Claude", "Claude AI", "Anthropic"]]`
- Rejected: 美股MSFT（微软）是一台无敌的复利机器么？持仓214天复盘
- Rejected: OpenAI 驚爆倒閉危機？背後 8000 億美金資金鏈恐全面崩潰！🚨 AI 泡沫終局到了？
- Rejected: 為什麼會有開源和閉源之爭? 背後有什麼陰謀? 主權AI成為最新投資趨勢! 黃仁勳為什麼要高舉開源?《投資唔講廢話》Ep304【阿樂】
- Rejected: 【AI大考】輝達連跌7天！財報再好也沒用？ #鐵板神授 謝晨彥分析師
- Rejected: 阿里難敵AI燒錢？現金流變負數要配股？投資越來越危險？【邵博看新聞】［AI字幕］#am730 #邵志堯 #阿里巴巴 #配股 #ai #港股

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "ON Semi"]]`
- Rejected: OpenAI联手博通造推理芯片，英伟达垄断地位危险了？#nvidia #openai #broadcom #tsmc #semiconductor #aichips #gpu #asics
- Rejected: 美股V型反弹！半导体、内存今天还能不能抄底？#美股 #美股直播 #美股行情 #科技股 #半导体 #内存 #光通信 #半导体ETF #AI芯片
- Rejected: 美股英伟达7连跌，AI硬件很便宜，PE 跌到18倍是黄金坑还是陷阱？#nvidia #nvda #jensenhuang #usstocks #stockmarket #semiconductor
- Rejected: 需求明明還在，美光與費半為什麼一直跌？機構正在悄悄切換定價邏輯！英偉達財報前必看！
- Rejected: 秃瓢0824盘后 | 芯片重挫 | 美加摩擦 | 伊朗制裁 | 后市怎么走 | 明天怎么布局

