import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Lets use the data of Apple
ticker = "AAPL"
# Downloading data from yfinance
data = yf.download(ticker, start = "2022-01-01", end = "2025-01-01")
#Basic pandas operations
print(type(data))
data.columns = data.columns.droplevel(1)
print(data.columns)
print(data.describe())
print(data.info())

#Adding daily return and moving averages to the datafrmae.
data["Daily Returns"] = data["Close"].pct_change()
data["MA_20"]= data["Close"].rolling(20).mean()
data["MA_200"] = data["Close"].rolling(200).mean()

print(data[["Close", "Daily Returns", "MA_20"]].tail())

#Creating the graphs
plt.figure(figsize=(10,5))
plt.plot(data["Close"], label = "Close")
plt.plot(data["MA_20"], label = "MA 20")
plt.plot(data["MA_200"], label = "MA_200")
plt.legend()
plt.title("AAPL prices with 20 day moving average")
plt.show()