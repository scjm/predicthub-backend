import yfinance as yf
import sys
import json
import pandas as pd

symbol = sys.argv[1] if len(sys.argv) > 1 else 'AAPL'
ticker = yf.Ticker(symbol)

# Get last 2 days of 1-minute data
hist = ticker.history(period="5d", interval="1m")

# Drop any rows with NaNs (common with pre/post market)
hist = hist.dropna(subset=["Close"])
hist = hist.reset_index()
hist["Datetime"] = hist["Datetime"].astype(str)

# Calculate previous close (last value from first day)
hist["Date"] = pd.to_datetime(hist["Datetime"]).dt.date
prev_day = hist["Date"].min()
prev_close_row = hist[hist["Date"] == prev_day].iloc[-1]
prev_close = prev_close_row["Close"]

# Convert to JSON structure
data = hist[["Datetime", "Close"]].to_dict(orient='records')

output = {
    "PrevClose": round(float(prev_close), 2),
    "Data": data
}

print(json.dumps(output))
