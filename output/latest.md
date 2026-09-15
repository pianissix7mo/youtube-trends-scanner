# YouTube Entity Enrichment

Generated: **2026-09-15T11:31:54.635527+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | AI slowdown / frontier-model caution | AI slowdown stocks Nvidia OpenAI Anthropic | 23/50 | 46.0% | 64 | 29 | 12.5% | 30.0% | ok |
| 2 | Apple Siri AI | Apple Siri AI waitlist iOS 27 | 23/39 | 59.0% | 6495 | 352 | 40.0% | 40.0% | ok |
| 3 | Alphabet / Google earnings | GOOGL Google earnings call | 0/50 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 4 | Samsung Semiconductor Austin | Samsung Semiconductor Austin fab | 0/2 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 5 | Power semiconductors | power semiconductor stocks GaN SiC | 1/13 | 7.7% | 55 | 55 | 0.0% | 100.0% | ok_low_relevance |
| 6 | Hewlett Packard Enterprise | HPE earnings call AI servers | 1/39 | 2.6% | 2 | 2 | 0.0% | 100.0% | ok_low_relevance |
| 7 | ASML | ASML earnings call EUV | 8/50 | 16.0% | 1742 | 75 | 25.0% | 50.0% | ok_low_relevance |
| 8 | Cybersecurity stocks | cybersecurity stocks CRWD PANW FTNT | 0/6 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 9 | Robinhood | Robinhood HOOD stock | 22/50 | 44.0% | 127 | 102 | 17.6% | 60.0% | ok |
| 10 | Micron Technology | Micron MU earnings memory HBM | 7/33 | 21.2% | 34 | 34 | 0.0% | 100.0% | ok_low_relevance |
| 11 | OpenAI | OpenAI latest business AI | 21/50 | 42.0% | 3312 | 23 | 0.0% | 0.0% | ok |
| 12 | Philadelphia Semiconductor Index / SOXX | Philadelphia Semiconductor Index SOXX chip stocks | 1/6 | 16.7% | 0 | 0 | 0.0% | 100.0% | ok_low_relevance |
| 13 | Arm Holdings | ARM earnings call AI chips | 1/50 | 2.0% | 14 | 14 | 0.0% | 100.0% | ok_low_relevance |
| 14 | OpenAI / Hugging Face incident | OpenAI Hugging Face incident AI agent | 11/50 | 22.0% | 170 | 170 | 18.2% | 100.0% | ok_low_relevance |
| 15 | Junior mining stocks | junior mining stocks gold uranium silver | 1/10 | 10.0% | 22 | 22 | 0.0% | 100.0% | ok_low_relevance |
| 16 | Navitas Semiconductor | Navitas Semiconductor NVTS GaN | 5/5 | 100.0% | 26 | 26 | 0.0% | 100.0% | ok |
| 17 | Meta Platforms | Meta META earnings AI | 7/50 | 14.0% | 133 | 38 | 0.0% | 57.1% | ok_low_relevance |
| 18 | Strait of Hormuz / Iran war | Iran war Strait of Hormuz oil stocks | 10/50 | 20.0% | 1456 | 5 | 0.0% | 20.0% | ok_low_relevance |
| 19 | TSMC | TSMC 台積電 stock AI chips | 12/50 | 24.0% | 42 | 14 | 12.5% | 60.0% | ok_low_relevance |
| 20 | Microsoft | Microsoft MSFT earnings AI cloud | 2/16 | 12.5% | 1436 | 3 | 0.0% | 50.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Alphabet / Google earnings — ok_no_relevant_videos
Relevance groups: `[["Google", "Alphabet", "GOOG", "GOOGL"], ["earnings", "results"]]`
- Rejected: Ca$htag$: GOOGL Vast CapEx Justifies $500B Backlog in AI Acceleration
- Rejected: Google Exposed Apple’s iphone Duo
- Rejected: Apple Trusted Google Until Nokia Turned the Joke Around 💀
- Rejected: Google Looks Cheap. The P/E Is Lying (GOOGL Stock Analysis)
- Rejected: He Used GrapheneOS Against Federal Agents 😳 #GrapheneOS #Pixel #Privacy #Android

### Samsung Semiconductor Austin — ok_no_relevant_videos
Relevance groups: `[["Samsung"], ["Austin", "Texas", "semiconductor", "fab"]]`
- Rejected: 삼성이 텍사스 시골 마을에 17조를 묻은 진짜 이유
- Rejected: What if 38% of the world's memory went dark for 30 days?

### Power semiconductors — ok_low_relevance
Relevance groups: `[["power semiconductor", "功率半導體", "功率 半導體", "GaN", "SiC"]]`
- Rejected: Navitas Semiconductor Stock: 310% Surge, Live Oak Deal & HUGE AI Opportunity
- Rejected: 단타 계속 손절치시는 분들 보세요
- Rejected: 謝寒冰駕到，談沈伯洋，談藍白合神操作，談所有最近最刺激的內容!
- Rejected: 【Multi Sub】Her Groom Skipped the Wedding—2 Years Later, He Became Her Business Partner
- Rejected: 1人暮らし料理集｜おうちごはんを楽しむ40個の簡単レシピ・お弁当｜ 40 Japanese Homemade  Recipes VLOG

### Hewlett Packard Enterprise — ok_low_relevance
Relevance groups: `[["HPE", "Hewlett Packard Enterprise"], ["earnings", "results"]]`
- Rejected: HPE Stock Is Back in Focus — Here’s What to Watch This Week
- Rejected: CrowdStrike Rallies, Coinbase Gains, HPE Falls | Stock Movers
- Rejected: Oracle Said $95B. These 3 Stocks Jumped Instead
- Rejected: SMCI Stock: The AI Server Giant Nobody Is Pricing Correctly? 🚨  #smci #smcistock #nyse
- Rejected: Oil Hits $100 + Dell All-Time High on $95B AI Backlog | Top Winners & Losers Week of Sep 8–12, 2026

### ASML — ok_low_relevance
Relevance groups: `[["ASML"], ["earnings", "EUV", "High NA"]]`
- Rejected: ASML JUST Made History: The Biggest Chip Mask Change in 30 Years
- Rejected: ASML Stock: What It Owns in Lithography Monopoly
- Rejected: The Missing Half of ASML's $380 Million Chipmaking Machine
- Rejected: Why China Cannot Copy This $300 Million Machine
- Rejected: ASML: Lasers Hit Molten Tin 50,000 Times a Second

### Cybersecurity stocks — ok_no_relevant_videos
Relevance groups: `[["cybersecurity", "cyber security"], ["stock", "stocks", "CRWD", "PANW", "FTNT"]]`
- Rejected: Why Palo Alto Networks Is Winning As AI Bubble Fears Explode | 2026 Investor Guide
- Rejected: Is cybersecurity back in the leadership role?
- Rejected: Does 10-Year Over 5% Matter? | JR Romero - T3 | PreMarket Prep - Sep 15, 2026
- Rejected: The 10-Year Touched 5% and AI Chips Broke. Cybersecurity Had Its Best Day. Here's the Rotation.
- Rejected: AI Slowdown Fears Hit Chips as CrowdStrike Jumps 13.85% | S&P 500 (2026-09-14)

### Micron Technology — ok_low_relevance
Relevance groups: `[["Micron", "MU"], ["earnings", "HBM", "memory"]]`
- Rejected: The AI Boom’s New Risk, & What It Means for Memory Stocks
- Rejected: Micron SanDisk Nvidia AMD Stocks! Jensen Huang Just Admitted the Real Problem ($MU $SNDK $NVDA $AMD)
- Rejected: MU Stock: The Massive AI Opportunity Investors Can’t Ignore
- Rejected: MICRON STOCK EXPLODES: MU’s AI Deal With Anthropic Changes EVERYTHING!
- Rejected: MU - 11 - Why Micron Technology is the Hidden Pillar of the AI Supercycle

### Philadelphia Semiconductor Index / SOXX — ok_low_relevance
Relevance groups: `[["Philadelphia Semiconductor", "費城半導體", "SOX", "SOXX"]]`
- Rejected: Semiconductor Stocks Plunge -5.7% Breaking $500! Where Smart Money Moved Today 📈 | Sept 15 US Market
- Rejected: 美債破5%、費半殺爛！ETF資金狂撤、比特幣卻逆勢翻紅？聯準會升息倒數！這波是真脫鉤，還是空軍被迫擡轎？
- Rejected: 費半警報拉響？AI巨頭罕見聯手喊降速，聯準會升息預期走高、殖利率逼近5%警戒線：這次是危機還是進場機會？
- Rejected: AI 감속론에 반도체 급락
- Rejected: หุ้นชิปร่วง 5.9% หลังคำเตือน AI | ตลาดเริ่มกังวลอะไร? #เข้าเรื่อง #aiข่าว #ข่าววันนี้

### Arm Holdings — ok_low_relevance
Relevance groups: `[["Arm", "ARM Holdings"], ["earnings", "chips", "AI"]]`
- Rejected: Top AI chief executives publicly agree on slowing AI development
- Rejected: Huawei Drives China's Push For Advanced AI Chips and Semiconductors
- Rejected: Google Just Won The AI Race
- Rejected: Richard Duncan on Creditism, the AI Arms Race, and “Cognitism” | Macro Watch
- Rejected: Qualcomm Explained: The Chip Giant’s Risky Second Act

### OpenAI / Hugging Face incident — ok_low_relevance
Relevance groups: `[["OpenAI"], ["Hugging Face", "HuggingFace"]]`
- Rejected: Anthropic CEO tells CNN how AI 'agent swarms' could threaten humanity
- Rejected: Why AI Agents Hacked Hugging Face: A Technical Post-Mortem
- Rejected: 700 AI Agents Attacked Hugging Face — Is AI Becoming Dangerous for Humans?
- Rejected: AI Agents Hacked Hugging Face | Full Incident Explained
- Rejected: 700 AI Agents Hacked A Real Company — Here's The Bill

### Junior mining stocks — ok_low_relevance
Relevance groups: `[["junior mining", "junior miner", "mining stocks"]]`
- Rejected: ⭐️ Silver BOOM! Do This With Your SILVER & GOLD Before It's Too Late! | Rick Rule GOLD & SILVER
- Rejected: Rick Rule :"If You’re Waiting for the Silver or Gold Bottom, You Need to See This" | Silver 2026
- Rejected: **THIS is BIG!** 🦍🦍 SILVER Just had a MASSIVE Change... (FED WEEK) Gold - Precious Metals News
- Rejected: **SILVER and Gold Investors** 🚨🚨 This is CHANGING NOW! - (TRUMP, China and Precious Metals)
- Rejected: MOST Silver Investors DON'T KNOW This! 🦍🦍 (Gold Price News Update too)

### Meta Platforms — ok_low_relevance
Relevance groups: `[["Meta"], ["earnings", "AI"]]`
- Rejected: The Best Stock To Buy During The "AI Slowdown"
- Rejected: KG: Dip Buyers Move Into AI Stocks, Crude Oil Spikes Near $105
- Rejected: A.I. Doom, Rate Hikes, High Oil.. Market SELLOFF Inevitable?
- Rejected: 4 Stocks I'll Buy If We Crash This Week
- Rejected: Meta Muse makes NOISE #shorts

### Strait of Hormuz / Iran war — ok_low_relevance
Relevance groups: `[["Hormuz", "Strait of Hormuz", "霍爾木茲", "霍尔木兹"], ["Iran", "oil", "war"]]`
- Rejected: Oil Jumps as Saudi Pipeline Attack Deepens Energy Crisis
- Rejected: Eurasia Group’s Greg Brew: The conflict in Iran is being fought in the oil market
- Rejected: Oil Rises as Saudi Arabia Shuts East-West Crude Pipeline
- Rejected: IRAN WAR | Saudi Arabia oil pipeline shuts down after attack causes fire
- Rejected: Today's oil price is still wrong and too low, says Amos Hochstein

### TSMC — ok_low_relevance
Relevance groups: `[["TSMC", "台積電", "台积电", "TSM"]]`
- Rejected: 【股票】AI三巨頭突發震撼彈！台股崩盤危機再現？高手揭歷史數據：恐慌真相全拆解！ft.蔡明翰｜下班經濟學778｜謝哲青、張瓊方
- Rejected: 技术分析无用？股市从业十余年，我为什么还在看技术分析？
- Rejected: Emad Mostaque | AI Labs Are Playing Russian Roulette With Humanity
- Rejected: 下一檔護國神山？老AI、設備廠務、散熱、CPO掀新革命！｜林昌興、白昀霏【#賺錢放大術】20260914 PART2
- Rejected: 晶圓代工巨頭力推矽光子！留意3檔CPO測試設備股【股市漲知識｜Shorts】

### Microsoft — ok_low_relevance
Relevance groups: `[["Microsoft", "MSFT"], ["earnings", "AI", "cloud"]]`
- Rejected: Global Markets Today: Oracle, Microsoft, OpenAI & ECB Rate Decision
- Rejected: Is MSFT Stock Ready to EXPLODE, AGAIN?! Microsoft at $600 Makes Sense If THIS Happens!
- Rejected: ⚡AI雲端大戰最大伏位：四大巨頭已簽落逾1萬億美元未來賬單？
- Rejected: AI Capex: Oracle Reverses as Chipmakers Rally
- Rejected: Warning: Open AI Is Going Bankrupt By 2028 And Taking These Stocks With It

