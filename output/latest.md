# YouTube Entity Enrichment

Generated: **2026-09-09T11:30:47.595860+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Oracle | Oracle ORCL earnings AI cloud | 15/32 | 46.9% | 14 | 14 | 7.7% | 90.0% | ok |
| 2 | GameStop | GameStop GME earnings collectibles | 6/6 | 100.0% | 77 | 58 | 0.0% | 83.3% | ok |
| 3 | Pinterest | Pinterest PINS earnings | 2/50 | 4.0% | 29 | 29 | 0.0% | 100.0% | ok_low_relevance |
| 4 | Casey's General Stores | Casey's CASY earnings | 8/50 | 16.0% | 197 | 63 | 20.0% | 62.5% | ok_low_relevance |
| 5 | Lyft | Lyft LYFT earnings | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 6 | NVIDIA | NVIDIA NVDA earnings AI chips | 20/50 | 40.0% | 51 | 42 | 11.1% | 80.0% | ok |
| 7 | OpenAI | OpenAI AI agents enterprise | 30/50 | 60.0% | 638 | 86 | 35.0% | 40.0% | ok |
| 8 | Meta AI / Muse agent | Meta META Muse AI agent WhatsApp Instagram | 6/18 | 33.3% | 158 | 56 | 0.0% | 83.3% | ok |
| 9 | Hugging Face / AI agent security | Hugging Face attack OpenAI agent security sandbox | 8/38 | 21.1% | 8 | 8 | 12.5% | 100.0% | ok_low_relevance |
| 10 | Claude / Anthropic | Anthropic Claude AI enterprise | 38/50 | 76.0% | 29 | 27 | 8.3% | 80.0% | ok |
| 11 | Semiconductor manufacturing process | semiconductor manufacturing process advanced nodes TSMC | 1/17 | 5.9% | 2 | 2 | 0.0% | 100.0% | ok_low_relevance |
| 12 | Power semiconductors | power semiconductor stocks GaN SiC | 0/11 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 13 | SEMICON Taiwan 2026 | SEMICON Taiwan 2026 semiconductor exhibition | 7/50 | 14.0% | 51 | 51 | 0.0% | 100.0% | ok_low_relevance |
| 14 | Sheng Yang Semiconductor 8028 | 8028 昇陽半導體 stock semiconductor | 0/0 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_videos |
| 15 | Mining stocks | mining stocks gold copper US equities | 1/50 | 2.0% | 1061 | 1061 | 100.0% | 100.0% | ok_low_relevance |
| 16 | Astra AI | Astra AI model agent | 50/50 | 100.0% | 15338 | 4712 | 80.0% | 0.0% | ok |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Pinterest — ok_low_relevance
Relevance groups: `[["Pinterest", "PINS"], ["earnings", "results", "guidance", "财报", "財報"]]`
- Rejected: 🚨 Pinterest LOVES This Content (But It Pays Less)
- Rejected: This 2026 Pinterest Strategy Is Working For Me ($400+/Day)
- Rejected: Automate Pinterest Pins: Free Organic Traffic to Affiliate Marketing Passive Income
- Rejected: How I Built My Pinterest Digital Product Funnel in 2 Hours (No Website, No Followers)
- Rejected: Pinterest + ChatGPT:  Online Earning ఎలా! | affiliate marketing 2026 | online earning Telugu

### Casey's General Stores — ok_low_relevance
Relevance groups: `[["Casey's", "CASY"], ["earnings", "results", "guidance"]]`
- Rejected: The Casey’s Stock Secret: Why This “Gas Station” Is Different
- Rejected: The Most Anticipated Earnings Releases for the Week of September 7, 2026
- Rejected: Earning Gabriel Seth's Respect
- Rejected: "MOST Investors Don't Understand This...." - Doug Casey
- Rejected: 5 Stupid Things I Did That Made Me a Better Real Estate Investor

### Lyft — ok_no_relevant_videos
Relevance groups: `[["Lyft"], ["earnings", "results", "guidance"]]`
- Rejected: Uber & Lyft Are Taking MORE, Quests Are Changing & Is Lyft Elite Still Worth It?
- Rejected: Is That Uber or Lyft Ride Worth It? | Rideshare Trip Profitability Calculator Demo
- Rejected: 🔥 UBER & LYFT DRIVERS: ARE RIDERS RUSHING YOU TO PICK THEM UP? HERE'S WHAT I DO!
- Rejected: YOU’RE ALREADY PAYING FOR LYFT OR UBER… BUT ARE YOU EARNING CASHBACK?
- Rejected: Idaho woman sues rideshare company Lyft, alleging 'gross negligence' after assault by driver

### Hugging Face / AI agent security — ok_low_relevance
Relevance groups: `[["Hugging Face", "OpenAI"], ["attack", "hack", "security", "sandbox"]]`
- Rejected: 700 AI Agents Attacked Hugging Face!
- Rejected: OpenAI shipped the AI that escaped and hacked Hugging Face
- Rejected: Is AI Out of Control? Asking Claude About the 700 Agent Escape
- Rejected: Securing AI Agents at Runtime
- Rejected: The Hugging Face Incident - OpenAI loses control

### Semiconductor manufacturing process — ok_low_relevance
Relevance groups: `[["semiconductor process", "semiconductor manufacturing", "半導體 製程", "半导体制程"]]`
- Rejected: ASML: The Machine the World Couldn’t Build
- Rejected: How They Print a Computer Chip With Light (And Why Only One Company Can Do It)
- Rejected: TSM Stock: Why Taiwan's $265B Chip Monopoly Matters
- Rejected: ASML’s EUV Monopoly Is About to Get Even BIGGER
- Rejected: Sony Controls 50% of Camera Chips. Why Spend $4.7B?

### Power semiconductors — ok_no_relevant_videos
Relevance groups: `[["power semiconductor", "power semiconductors", "功率 半導體", "功率半导体", "GaN", "SiC"]]`
- Rejected: NVTS Stock: The AI Power Revolution Is Just Beginning
- Rejected: All Ignored The Poor Girl's Cries For Help—Only A Waiter Saved Her,Who Was Secretly Billionaire CEO!
- Rejected: 🔴【FULL】开朗少女为父报仇嫁进豪门，冷酷少爷竟是她苦寻多年的旧爱！两人开启隐婚生活，一边斗嘴撒糖，一边偷偷调查，没想到真凶竟是身边人！
- Rejected: 【短劇全集】她扮成醜女嫁給傳聞中又殘又狠的豪門三少，誰知新婚夜男人反手甩來一張黑卡！直到她偷偷恢復絕美容貌，他突然從輪椅站起來，雙雙看傻眼！【我扮醜來你裝殘，湊成一對笑翻天2】
- Rejected: 【短劇全集】覺醒異能綁定消費系統後我越花錢越暴富，狂賺千億逆襲成女總裁，窮親戚上門搶家產被我直接甩黑卡轟出門，捐掉財產我狠狠打惡人臉【財富逆襲女王】

### SEMICON Taiwan 2026 — ok_low_relevance
Relevance groups: `[["SEMICON Taiwan", "半導體 展", "半导体展"]]`
- Rejected: Taiwan draws worldwide chip industry to semiconductor trade show | Paraluman News
- Rejected: SEMICON 2026: Why California and Arizona Want Taiwan’s Chipmakers｜Zoom In Zoom Out
- Rejected: Taiwan draws worldwide chip industry to semiconductor trade show | Paraluman News
- Rejected: Global shortage of semiconductor chips dominates SEMICON expo in Taiwan
- Rejected: SEMICON 2026: Why California and Arizona Want Taiwan’s Chipmakers | Zoom In Zoom Out

### Mining stocks — ok_low_relevance
Relevance groups: `[["mining stocks", "miners", "gold miners", "copper miners", "矿业股", "礦業股"]]`
- Rejected: Gold Is Falling Again — This Is the Buy Setup I Was Waiting For
- Rejected: Gold Stocks Catch Up as Copper Supply Tightens | Nicole Adshead-Bell
- Rejected: All 3 of My Gold Buy Zones Hit — Here's Where I'm Buying Now
- Rejected: Discussion with Dan O'Flaherty | Versamet Royalties (NASDAQ:VMET) | Gold, Silver & Copper
- Rejected: Starcore International Mines Ltd. Builds Three Revenue Streams Across Gold and Silver

