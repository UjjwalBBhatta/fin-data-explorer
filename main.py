import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""1. Data fetching"""

# Lets use the data of Apple
ticker = "AAPL"
# Downloading data from yfinance
data = yf.download(ticker, start = "2022-01-01", end = "2025-01-01")
#Clean multinidex
data.columns = data.columns.droplevel(1) 


"""2. Feature Engineering"""
#Daily return
data["Daily Returns"] = data["Close"].pct_change()

#Moving averages
data["MA_20"]= data["Close"].rolling(20).mean()
data["MA_200"] = data["Close"].rolling(200).mean()

# Rolling volatility (20 day std)
data["Vol_20"] = data["Close"].rolling(20).std()

#Annual Volatility
data["Vol_20_Annualized"] = data["Vol_20"]*np.sqrt(252)

"""3. Risk Metrics"""

#Approx sharpe(risk-free=0)
mean_daily = data["Daily Returns"].mean()
std_daily = data["Daily Returns"].std()

sharpe = (mean_daily * 252) / (std_daily * np.sqrt(252))
print("Approx Sharpe:", sharpe)

#Max Drawdown
roll_max = data["Close"].cummax()
drawdown = (data["Close"] - roll_max) / roll_max
max_dd = drawdown.min()

print("Max Drawdown:", max_dd)

#Creating the graphs
plt.figure(figsize=(10,5))
plt.plot(data["Close"], label = "Close")
plt.plot(data["MA_20"], label = "MA 20")
plt.plot(data["MA_200"], label = "MA_200")
plt.legend()
plt.title("AAPL prices with 20 day moving average")
plt.show()