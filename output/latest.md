# YouTube Entity Enrichment

Generated: **2026-08-24T09:45:20.539449+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | NVIDIA earnings | NVIDIA NVDA 财报 | 18/50 | 36.0% | 18 | 13 | 0.0% | 80.0% | ok |
| 2 | Semiconductor stocks | 半导体 美股 semiconductor stocks | 9/45 | 20.0% | 52 | 47 | 0.0% | 88.9% | ok_low_relevance |
| 3 | ON Semiconductor | ON Semiconductor ON 美股 | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 4 | Semiconductor supply chain | 半导体供应链 美股 | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 5 | Applied Optoelectronics | AAOI 美股 光通信 | 3/9 | 33.3% | 7406 | 7406 | 66.7% | 100.0% | ok |
| 6 | Tesla | Tesla TSLA 美股 | 35/50 | 70.0% | 193 | 149 | 22.6% | 90.0% | ok |
| 7 | Roblox | Roblox RBLX 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 8 | Yageo | 国巨 Yageo 2327 | 2/2 | 100.0% | 401 | 72 | 0.0% | 50.0% | ok |
| 9 | Navitas Semiconductor | Navitas NVTS 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 10 | Silver mining stocks | 白银矿业股 silver mining stocks | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 11 | Evergreen Marine | 长荣海运 Evergreen Marine 2603 | 3/3 | 100.0% | 403 | 403 | 0.0% | 100.0% | ok |
| 12 | Robinhood | Robinhood HOOD 美股 | 7/16 | 43.8% | 50 | 50 | 14.3% | 100.0% | ok |
| 13 | TSMC | 台积电 TSMC 美股 | 12/49 | 24.5% | 1403 | 293 | 37.5% | 60.0% | ok_low_relevance |
| 14 | AI agents | AI Agent 美股 | 0/44 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | Claude AI / Anthropic | Claude AI Anthropic 美股 | 9/18 | 50.0% | 78 | 78 | 0.0% | 100.0% | ok |
| 16 | Walmart earnings | Walmart WMT 财报 | 6/12 | 50.0% | 6 | 7 | 20.0% | 83.3% | ok |
| 17 | Sunrise Semiconductor | 昇阳半导体 8028 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 18 | Magnachip Semiconductor | Magnachip MX 美股 | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"]]`
- Rejected: 美股还能追吗？黄金、AI与中概股全面复盘｜GDX、NVDA、MU、BABA
- Rejected: 放水上漲！年底要發財，這些股票必須提前佈局！
- Rejected: 美股上周五彈 美債息.黃金.比特幣衝!輝達財報27日公布 華爾街齊叫好!傑克森洞央行年會本周登場 Fed華許能否安撫市場成焦點｜主播貝庭｜【非凡Morning Call】20260824｜非凡財經新聞
- Rejected: AI晶片狂歡終結？指數大漲背後，資金竟在暗中暴逃…
- Rejected: 【美股深度】MRVL凭什么撑起2000亿估值？从光互连垄断到定制ASIC全面爆发的底层逻辑。

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "安森美"]]`
- Rejected: 半导体止跌！内存、光通信今天能不能抄底？#美股 #美股直播  #美股行情 #美股分析 #半导体 #科技股 #内存 #存储芯片 #光通信 #AI #AI芯片 #西部数据 #美光 #AMD
- Rejected: AI晶片狂歡終結？指數大漲背後，資金竟在暗中暴逃…
- Rejected: 美股还能追吗？黄金、AI与中概股全面复盘｜GDX、NVDA、MU、BABA
- Rejected: 【Dennis湯紹彰專訪】半導體潮完未?Ai泡沫要爆破？拆解AI巨頭燒錢真相與中美算力下半場發展 | 新手Algo投資 | Ai交易 | Ai模型股仲可以玩? (上集)
- Rejected: 7月股災會重演嗎？高盛揭密「去槓桿已結束」！真正殺跌AI科技股的不是泡沫？抄底前看懂這三個訊號

### Semiconductor supply chain — ok_no_relevant_videos
Relevance groups: `[["semiconductor", "semiconductors", "chip", "chips", "半导体", "半導體"], ["supply chain", "供应链", "供應鏈"]]`
- Rejected: 股市以盤待變? 壓力鍋快爆了? 美股|陽明|聯電|力積電|仁寶|台積電|微軟|特斯拉|美光|升息|記憶體|台積電|輝達|美債|財經|股票|投資理財|美元| 08/24/26【宏爺講股】
- Rejected: AI牛市要变天？下周美股将迎来三场大考！决定美股命运的是这3件事！#美股#美股分析#美股投资#美股散户#美股行情#英伟达#QQQ#半导体#美联储#杰克逊霍尔#利率#降息#高利率#华尔街#华尔街投资
- Rejected: 美股见顶信号全面显现，盘前个股应声下跌，接下来行情何处寻底？黄金如期大涨迎来持续狂飙，比特币面临关键阻力压制，但回调后看涨趋势极其明确，仍是大买特买的黄金节点！#美股,#纳斯达克,#道琼斯
- Rejected: 下半年AI投资 3只孤岛股逆势爆发
- Rejected: 七巨頭估值比台積便宜 美股ETF他先卡位 !｜楚狂人 ft. 證券分析師 股添樂｜財富狂犇｜玩股網20260822

### Silver mining stocks — ok_no_relevant_videos
Relevance groups: `[["silver", "白银", "白銀"], ["miner", "miners", "mining", "矿业", "礦業", "矿商", "礦商"]]`
- Rejected: 【全集】💎陈峰遭合伙好友暗算夺走金矿，被千元打发，母亲重病受尽周遭白眼。觉醒淘金系统后不断发掘珍稀矿产，创立公司碾压各路敌人，协助警方侦破走私案件，落魄矿工蜕变为威震一方的矿业大佬#短剧 #短劇

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "Taiwan Semiconductor", "台积电", "台積電", "台积", "台積"]]`
- Rejected: 【AI風暴】拉積盤 還能撐多久?  2026.08.22 #週末加班 謝晨彥分析師
- Rejected: 美光再砸百億美元擴建晶圓廠！AI熱潮帶動股價狂飆 搶攻龐大晶片商機｜94要賺錢
- Rejected: 美債殖利率成雷區 台股多空激戰
- Rejected: 放水上漲！年底要發財，這些股票必須提前佈局！
- Rejected: 南韓還在吵台灣先發錢?普發一萬AI變現? 台灣經濟輾壓南韓!GDP狂飆不只靠神山還靠..?│20260824│Catch大錢潮 feat.黃世聰

### AI agents — ok_no_relevant_videos
Relevance groups: `[["AI agent", "AI agents", "agentic AI", "智能体", "智能體", "AI代理", "AI 代理"]]`
- Rejected: 【不用擔心！】AI泡沫台股會跌破4萬？這族群會發大財！ (有字幕好幸福) 2026.08.22
- Rejected: Rick：AI 沒泡沫！這輪 Crypto 押美股上鏈和 Agent 經濟
- Rejected: 一次搞懂Token與API：AI到底怎麼運作、怎麼計費？Understanding Tokens and APIs: How Does AI Work and How Is It Billed?
- Rejected: 88核对决256核，还有一家交不出时间表：Nvidia、AMD、Intel争的根本不是核数
- Rejected: 美股MSFT（微软）是一台无敌的复利机器么？持仓214天复盘

