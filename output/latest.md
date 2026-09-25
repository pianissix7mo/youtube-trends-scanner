# YouTube Entity Enrichment

Generated: **2026-09-25T11:31:59.219999+00:00**

This is a measurement table, not the final editorial ranking. ChatGPT reviews it after enrichment.

| # | Entity | YouTube query | Relevant sample | Relevant % | Relevant median views/day | Small-channel median views/day | Small-channel hit | Top-10 small share | Status |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Costco | costco earnings | 48/50 | 96.0% | 70 | 40 | 17.1% | 50.0% | ok |
| 2 | Semiconductor ETFs | best semiconductor etf | 0/49 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 3 | Robinhood | hood earnings | 2/50 | 4.0% | 817 | 817 | 0.0% | 100.0% | ok_low_relevance |
| 4 | Robotics stocks | robotics stocks | 1/50 | 2.0% | 82 | 82 | 0.0% | 100.0% | ok_low_relevance |
| 5 | Meta Muse AI | meta muse ai | 31/50 | 62.0% | 7440 | 324 | 38.5% | 20.0% | ok |
| 6 | indie Semiconductor | indie semiconductor | 0/12 | 0.0% | 0 | 0 | 0.0% | 0.0% | ok_no_relevant_videos |
| 7 | Micron Technology | micron | 48/50 | 96.0% | 1284 | 1026 | 51.5% | 50.0% | ok |
| 8 | Semiconductor shortage | semiconductor shortage | 3/50 | 6.0% | 202 | 202 | 0.0% | 100.0% | ok_low_relevance |
| 9 | Alphabet | googl earnings call | 6/50 | 12.0% | 7 | 4 | 20.0% | 83.3% | ok_low_relevance |
| 10 | Tesla | tsla earnings call | 22/50 | 44.0% | 1827 | 33 | 37.5% | 30.0% | ok |
| 11 | CoreWeave | crwv earnings call | 5/15 | 33.3% | 32 | 32 | 0.0% | 100.0% | ok |
| 12 | AI glasses | ai 眼鏡 | 17/50 | 34.0% | 7556 | 93 | 33.3% | 10.0% | ok |
| 13 | Semiconductor packaging | semiconductor packaging | 5/50 | 10.0% | 12 | 12 | 0.0% | 100.0% | ok_low_relevance |
| 14 | TSMC | taiwan semiconductor | 20/50 | 40.0% | 1489 | 413 | 33.3% | 20.0% | ok |
| 15 | Meta AI glasses | meta ai glasses | 49/50 | 98.0% | 1848 | 79 | 20.8% | 10.0% | ok |
| 16 | NVIDIA | nvda earnings call | 10/23 | 43.5% | 10 | 10 | 20.0% | 100.0% | ok |
| 17 | Microsoft | msft earnings call | 8/50 | 16.0% | 5 | 5 | 0.0% | 87.5% | ok_low_relevance |
| 18 | AUO | 友達 股票 | 44/50 | 88.0% | 4855 | 353 | 47.1% | 0.0% | ok |
| 19 | ON Semiconductor | on semiconductor | 4/50 | 8.0% | 2186 | 290 | 0.0% | 50.0% | ok_low_relevance |
| 20 | Semiconductor stocks | semiconductor stocks | 8/50 | 16.0% | 175 | 136 | 16.7% | 75.0% | ok_low_relevance |

- Window: last 3 days.
- Small channel: fewer than 50,000 subscribers.
- Small-channel hit: at least 1,000 views/day.
- Rejected-title diagnostic sample: up to 5 titles per low/no-relevance entity.
- Relevance rules are generated dynamically by the selection-stage ChatGPT.
- YouTube totalResults remains a raw approximate count and is not treated as a clean relevant-video count.

## Relevance filter diagnostics

### Semiconductor ETFs — ok_no_relevant_videos
Relevance groups: `[["semiconductor ETF", "SOXX", "SMH", "半導體 ETF"]]`
- Rejected: The Biggest ETF Trends Investors Should Know Now | Market Sense | Fidelity Investments
- Rejected: YieldMax CHPY: The BEST Weekly Income Fund? 60%+ Distribution Rate Explained
- Rejected: The ETF Roundup with Étienne Joncas-Bouchard – September 2026
- Rejected: If I started investing from $100 in Australia in 2026
- Rejected: WARNING: This Is Where Most Investors Mess It All Up! [This Is My Plan]

### Robinhood — ok_low_relevance
Relevance groups: `[["Robinhood", "HOOD"]]`
- Rejected: THIS Stock Will Print Millionaires AGAIN
- Rejected: Why They Murdered the 300,000 Mile Engine
- Rejected: Morning Call Sheet: AI, rates and China drive the market outlook
- Rejected: SoFi Is Down 40%. Here's the Truth About The Situation
- Rejected: Somebody Has To Eat The $40 Trillion Loss | Jack Mallers

### Robotics stocks — ok_low_relevance
Relevance groups: `[["robotics stocks", "robot stocks"]]`
- Rejected: The $6 Billion Gamble Behind XPENG's Robot
- Rejected: AI Investors Looking At WRONG Stocks Following Meta's Muse Release
- Rejected: Is Ouster Stock The Ultimate Physical AI Winner? $OUST
- Rejected: AI has a power problem. These 5 stocks are built to solve it.
- Rejected: China's Unitree Robotics Stock Plunges 53 Percent After IPO

### indie Semiconductor — ok_no_relevant_videos
Relevance groups: `[["indie Semiconductor", "INDI"]]`
- Rejected: ASML Says It's Selling Zero Chip Machines In Europe | Here's Why That's A Warning Sign
- Rejected: 소니는 패키지를 없애서 무엇을 얻을 수 있을까요? | 할 일 없을 때 몰아보기
- Rejected: ALERT: India and EU Are Building a Joint AI Chip and 6G Alliance While the UN Calls AI Existential
- Rejected: Infineon To Add 750 Employees In India, Bets Big On AI Data Centres | Startup Street
- Rejected: ‘India has enough capacity for mobile screen protectors…’: says MeitY Secy S Krishnan

### Semiconductor shortage — ok_low_relevance
Relevance groups: `[["semiconductor shortage", "chip shortage"]]`
- Rejected: Micron to report earnings amid AI boom and memory shortage
- Rejected: Why Elon Musk Is Building TeraFab: The AI Compute Shortage Explained
- Rejected: The Coming AI Memory Shortage
- Rejected: Oracle Shares Fall 5% Amid Data Center Backlash | FBI Hacking Unit Exposed?
- Rejected: Logitech CEO: “AI is Eating My Chips”

### Alphabet — ok_low_relevance
Relevance groups: `[["Alphabet", "Google", "GOOGL", "GOOG"]]`
- Rejected: ESDS Software Solution Earnings Call for Q1FY27
- Rejected: AI Can Book Your Hotel. Why Is Wall Street Worried?
- Rejected: SPX Nears All-Time High, Diesel Sees Key Support as UN General Assembly Begins
- Rejected: US, Iran Said to Be Exploring Phased Deal to Open Hormuz
- Rejected: AI Keeps Getting Cheaper. So Why Is the Bill Going Up?

### Semiconductor packaging — ok_low_relevance
Relevance groups: `[["semiconductor packaging", "advanced packaging"]]`
- Rejected: SEMICON Exclusive Interview｜Powering the AI Era: The Role of Advanced Materials
- Rejected: How Microchips Are Made: The $200M Machine That Prints Every AI Chip
- Rejected: Terafab Explained: Elon Musk’s Plan for the AI Chip Factory
- Rejected: How a Transistor works
- Rejected: Why Heat Warps and Breaks Microchips | Avecas

### Microsoft — ok_low_relevance
Relevance groups: `[["Microsoft", "MSFT"]]`
- Rejected: AI Takes Center Stage From Oracle to the White House
- Rejected: The Trillion-Dollar AI Buildout: What If It Doesn't Pay Off?
- Rejected: The Nasdaq surge: The Investment Committee's strategy
- Rejected: Shopify Q2 2026 Earnings: AI, Sidekick & Record $116B GMV Growth
- Rejected: 【AMD 2Q26】$11.5B Revenue & $6.7B Data Center Surge! Lisa Su’s 2000x AI Inference Bombshell Revealed!

### ON Semiconductor — ok_low_relevance
Relevance groups: `[["ON Semiconductor", "onsemi", "ON"]]`
- Rejected: The Insane Engineering Behind Semiconductors
- Rejected: Is Taiwan Semiconductor Stock an Undervalued AI Stock to Buy Right Now? | TSM STock Analysis
- Rejected: Taiwan: Home of semiconductor giants at the centre of AI race • FRANCE 24 English
- Rejected: Why Heat Warps and Breaks Microchips | Avecas
- Rejected: How are Semiconductor Chips made? The complete story from sand to 2nm chip

### Semiconductor stocks — ok_low_relevance
Relevance groups: `[["semiconductor stocks", "chip stocks"]]`
- Rejected: Is Western Digital an Undervalued Semiconductor Stock to Buy Right Now? | WDC STock Analysis
- Rejected: The Warning In These Stocks (Micron SanDisk SK Hynix Nvidia AMD Seagate Western Digital Meta)
- Rejected: Is Taiwan Semiconductor Stock an Undervalued AI Stock to Buy Right Now? | TSM STock Analysis
- Rejected: TSM Taiwan Semiconductor: 3 Stock Price Scenarios After Sep 24 Close + Friday Predicted Opening? 🚀
- Rejected: Did OpenAI Just Changed the Memory Trade?

