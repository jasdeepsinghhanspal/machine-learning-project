import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and date range
ticker = 'ULTRACEMCO.BO'  # UltraTech Cement stock on BSE
start_date = '2010-01-01'
end_date = '2025-12-31'

# Download historical stock price data using Yahoo Finance API
stock_data = yf.download(ticker, start=start_date, end=end_date)['Close']

# Create a time series plot
plt.figure(figsize=(12, 6))
plt.plot(stock_data)
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()

# Calculate the rolling mean (moving average)
window_size = 30  # You can adjust the window size as needed
rolling_mean = stock_data.rolling(window=window_size).mean()

# Make predictions (forecasting)
n_forecast = 30  # Number of days to forecast
last_observation = stock_data.iloc[-1]  # Get the last observed price
forecast = pd.Series([last_observation] * n_forecast)  # Forecasted prices as a constant value

# Create a plot for the forecast
plt.figure(figsize=(12, 6))
plt.plot(stock_data[-100:], label='Actual Prices', color='blue')
plt.plot(range(len(stock_data), len(stock_data) + n_forecast), forecast, label='Forecast', color='red')
plt.title(f"{ticker} Stock Price Forecast (Moving Average)")
plt.xlabel("Days")
plt.ylabel("Price (INR)")
plt.legend()
plt.show()
