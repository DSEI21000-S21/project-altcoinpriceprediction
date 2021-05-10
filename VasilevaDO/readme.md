Slide 1.
Altcoin Price Prediction
By Daria Vasileva, Estrella Moreira, Michael Wander, and Andreas Michael


Slide 2. 
What is cryptocurrency and why people use it?
A cryptocurrency (or “crypto”) is a digital currency that can be used to buy goods and services, but uses an online ledger with strong cryptography to secure online transactions.
People use cryptocurrency for quick payments, to avoid transaction fees that regular banks charge, or because it offers some anonymity. Others hold cryptocurrency as an investment, hoping the value goes up.

Types of Cryptocurrency
The first blockchain-based cryptocurrency was Bitcoin, which still remains the most popular and most valuable. Today, there are thousands of alternate cryptocurrencies with various functions and specifications. Some of these are clones or forks of Bitcoin, while others are new currencies that were built from scratch.
Bitcoin was launched in 2009 by an individual or group known by the pseudonym "Satoshi Nakamoto."

Some of the competing cryptocurrencies spawned by Bitcoin’s success, known as "altcoins," include Litecoin, Peercoin, and Namecoin, as well as Ethereum, Cardano.

Slide 3. 
What did we do and why?
Develop althogitm that will predict price movement for 2 days (Daria)
Same for 7 days (Michael)
Shitcoins (Andreas)
Pair trading (Estrella)

Slide 4.
Data.
The dataset has one csv file for each currency. Price history is available on a daily basis starting from April 28, 2013. This dataset has the historical price information of some of the top crypto currencies by market capitalization. Sourced from CoinMarketCap.com

Date : date of observation
Open : Opening price on the given day
High : Highest price on the given day
Low : Lowest price on the given day
Close : Closing price on the given day
Volume : Volume of transactions on the given day, in USD
Market Cap : Market capitalization in USD

Slide 5.
How we do it?
Our methodology
Exploratory Data Analysis
Time Series Analysis
Machine Learning (Arima, Autoreg, Vector autoregression, Vector autoregressive moving average models , Long Term-Short Term Memory )

Slide 6.
Technical Indicators
Moving Average (lagging) analyze whether a market is moving up, down, or sideways over time.
Bollinger Bands (lagging) measure how far a price swing will stretch before a counter impulse triggers a retracement.
MACD (leading) evaluate the speed of price change over time.
Volume indicators (leading or lagging) tally up trades and quantify whether bulls or bear are in control.

Slide 7. 

Autocorrelation function revealed that there is no significant correlation between data points, making the algorithm not suitable for this kind time-series analysis.  

Slide 8/9 
Bollinger Bands and MACD
Simple trading strategy based on technical indicators, such as Bollinger Bands and MACD can work as alternative to 2-day trading technique.










