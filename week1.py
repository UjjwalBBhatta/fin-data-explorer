import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Function for daily returns
def daily_returns(prices):
    return prices.pct_change()*100

def moving_avg(prices, frame):
    return prices.rolling(frame).mean()

def rolling_volatility(prices, frame=20):
    returns = daily_returns(prices)
    return returns.rolling(frame).std()

prices = pd.Series([100,102,101,105,110,108,111,115,117,116])

returns = daily_returns(prices)
ma3 = moving_avg(prices,3)
vol = rolling_volatility(prices,3)

print(returns, ma3, vol)

#Plotting shit now
plt.figure( figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(prices, label="Price")
plt.plot(ma3, label="MA_3")
plt.legend()

plt.subplot(2,1,2)
plt.plot(vol, label="Rolling Volatility")
plt.plot(returns, label = "Returns")
plt.legend()

plt.tight_layout()
plt.show()