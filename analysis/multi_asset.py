import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""1. Data fetching"""

#Lets get the data for Apple, Google, and Microsoft
tickers = ["AAPL", "MSFT", "GOOG"]
data = yf.download(tickers, start = "2022-01-01", end = "2025-01-01")
#Clean the data
print(data.head())

#Get the closing prices
close_prices = data["Close"]

#Get the returns
returns = close_prices.pct_change()

#Correlation matrix
corr_matrix = returns.corr()

sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()