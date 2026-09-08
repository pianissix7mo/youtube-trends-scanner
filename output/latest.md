# YouTube Entity Enrichment

Generated: **2026-09-08T11:32:25.356827+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Pinterest | Pinterest PINS earnings | 2/50 | 4.0% | 28 | 28 | 0.0% | 100.0% | ok_low_relevance |
| 2 | Lululemon | Lululemon LULU stock earnings | 30/39 | 76.9% | 22 | 22 | 3.3% | 100.0% | ok |
| 3 | CoreWeave | CoreWeave CRWV earnings AI cloud | 1/4 | 25.0% | 22 | 22 | 0.0% | 100.0% | ok_low_relevance |
| 4 | Magnachip Semiconductor | Magnachip MX semiconductor stock | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 5 | TSMC | TSMC TSM Taiwan Semiconductor | 5/9 | 55.6% | 13 | 13 | 0.0% | 100.0% | ok |
| 6 | ON Semiconductor | ON Semiconductor onsemi ON stock | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 7 | OpenAI Astra | OpenAI Astra AI model agents | 50/50 | 100.0% | 7462 | 3189 | 60.7% | 10.0% | ok |
| 8 | Indie Semiconductor | Indie Semiconductor INDI stock | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Fubon Semiconductor ETF 00892 | 00892 富邦半導體 ETF | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 10 | Navitas Semiconductor | Navitas NVTS semiconductor stock | 6/7 | 85.7% | 28 | 28 | 0.0% | 100.0% | ok |
| 11 | Oracle | Oracle ORCL earnings AI cloud | 13/26 | 50.0% | 10 | 10 | 0.0% | 90.0% | ok |
| 12 | NVIDIA | NVIDIA NVDA earnings AI chips | 25/50 | 50.0% | 36 | 35 | 12.5% | 90.0% | ok |
| 13 | Micron Technology | Micron MU stock HBM memory | 8/40 | 20.0% | 49 | 38 | 14.3% | 87.5% | ok_low_relevance |
| 14 | Nanya Technology | Nanya Technology 南亞科 DRAM memory | 0/1 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 15 | AI agents | AI agents enterprise software stocks | 6/50 | 12.0% | 33 | 33 | 0.0% | 100.0% | ok_low_relevance |
| 16 | Robinhood | Robinhood HOOD stock | 25/50 | 50.0% | 74 | 31 | 22.2% | 50.0% | ok |
| 17 | Foxconn / Hon Hai | Foxconn Hon Hai 鴻海 AI server stock | 1/1 | 100.0% | 0 | 0 | 0.0% | 100.0% | ok |
| 18 | Power semiconductors | power semiconductor stocks GaN SiC | 0/7 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 19 | Advanced semiconductor packaging | advanced semiconductor packaging CoWoS HBM | 2/12 | 16.7% | 9 | 9 | 0.0% | 100.0% | ok_low_relevance |
| 20 | Oil stocks / crude oil | oil stocks crude oil WTI Brent | 15/50 | 30.0% | 208 | 63 | 0.0% | 60.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Pinterest — ok_low_relevance
Relevance groups: `[["Pinterest", "PINS"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: How to Make Money with Pinterest in 2026 | Affiliate Marketing
- Rejected: How I Built My Pinterest Digital Product Funnel in 2 Hours (No Website, No Followers)
- Rejected: How a Random Pinterest Pin Made Me $500 (Digital Product Strategy)
- Rejected: Get Sales on Shopify - Easy Pinterest Marketing (Automated)
- Rejected: How to Make Money with Pinterest in 2026 | Affiliate Marketing

### CoreWeave — ok_low_relevance
Relevance groups: `[["CoreWeave", "CRWV"], ["earnings", "results", "guidance", "AI", "cloud"]]`
- Rejected: CRWV Revenue Doubled to $2.58B with $104B Backlog, Best Stock to Buy! CRWV Stock Analysis
- Rejected: IREN has absurd upside and absurd downside. Both hosts stepped aside.
- Rejected: Nvidia's CEO just told you exactly where to invest. Here are the 5 layers and the stocks in each.

### ON Semiconductor — ok_no_relevant_videos
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: NVTS Stock: The AI Power Revolution Is Just Beginning
- Rejected: China Pours Billions Into Mega Banks and Insurers | The China Show | 9/7/2026

### Indie Semiconductor — ok_no_relevant_videos
Relevance groups: `[["Indie Semiconductor", "INDI"]]`
- Rejected: अंटार्कटिका में माइनस 50 डिग्री पर विदेशी साजिश-भारत के आवारा लड़के ने ऐसे किया बेनकाब! | Story

### Micron Technology — ok_low_relevance
Relevance groups: `[["Micron", "MU", "美光"], ["HBM", "memory", "DRAM", "NAND", "存储", "記憶體"]]`
- Rejected: Micron technology analysis by Muffett investments #stockanalysis #investing #ai
- Rejected: I Investigated the Memory Trade - Here Is What I Found!
- Rejected: A New Threat Just Hit Samsung & SK Hynix!
- Rejected: MU - 04 - Micron's New High Margin Business Unit is Driving Stability and Massive Profitability #MU
- Rejected: The AI Stock You Need to Watch Right Now (It's Not Nvidia)

### Nanya Technology — ok_no_relevant_videos
Relevance groups: `[["Nanya Technology", "南亞科", "南亚科"], ["DRAM", "memory", "記憶體", "存储"]]`
- Rejected: 記憶體股票最後的機會，錯過，99%的人將要買在山頂。

### AI agents — ok_low_relevance
Relevance groups: `[["AI agent", "AI agents", "agentic AI", "智能体", "代理"]]`
- Rejected: NVDA Stock: $13B Hugging Face Deal — What Happens Next?
- Rejected: Foxconn Just Sent Nvidia Investors a Powerful AI Signal
- Rejected: AI and software can 'live together in harmony': Jefferies’ Brent Thill
- Rejected: ServiceNow (NOW) Stock: Buy After the +53% Rally, or Huge Valuation Trap?
- Rejected: REZOLVE AI: SOMETHING BIG IS HAPPENING THIS WEEK! | RZLV Stock

### Power semiconductors — ok_no_relevant_videos
Relevance groups: `[["power semiconductor", "power semiconductors", "功率 半導體", "功率半导体", "GaN", "SiC"]]`
- Rejected: NVTS Stock: The AI Power Revolution Is Just Beginning
- Rejected: 🔴【FULL】开朗少女为父报仇嫁进豪门，冷酷少爷竟是她苦寻多年的旧爱！两人开启隐婚生活，一边斗嘴撒糖，一边偷偷调查，没想到真凶竟是身边人！
- Rejected: [FULL]穿书嫁恋爱脑霸总，谁知他能听见我心声，我嘴上乖巧扮贤妻心里疯狂吐槽想跑路，他看穿我所有小心思疯狂吃醋强制偏爱【婚約讀心大亂鬥】
- Rejected: 【短劇全集】說好只做兩年隱婚夫妻，她卻被便宜老公越寵越心動，全然不知他竟是隱藏總裁！消失五年她帶娃歸來，男人紅著眼求婚：老婆孩子，這次都別走！【今我來思】
- Rejected: 窮小伙被雷劈後覺醒天生神力，全村笑他傻人有傻福，殊不知美女們深夜排隊上門示好，他反手一巴掌打飛村霸，一夜暴富成傳奇!

### Advanced semiconductor packaging — ok_low_relevance
Relevance groups: `[["advanced packaging", "semiconductor packaging", "半導體 封裝", "半导体封装", "CoWoS"]]`
- Rejected: TSMC SoIC Explained: Hybrid Bonding and the Vertical Architecture of AI Compute
- Rejected: Why AI Chips Are So Hard to Build
- Rejected: The Entire AI Memory Industry Explained: Why the Fastest Chips Are Starving
- Rejected: 輝達還能漲多久？台積電推遲封裝訂單，手裡有AI股票到底該賣還是該扛？
- Rejected: The AI Dividend Stock Behind Nvidia, Micron & AMD

