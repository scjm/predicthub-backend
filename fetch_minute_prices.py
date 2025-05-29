import yfinance as yf
import sys
import json

symbol = sys.argv[1] if len(sys.argv) > 1 else 'AAPL'
ticker = yf.Ticker(symbol)

# ✅ Get 1-minute interval data for the past 7 days (max allowed)
hist = ticker.history(period="7d", interval="1m")

# Ensure at least one row is returned
if hist.empty:
    print(json.dumps([]))
    sys.exit()

# Prepare JSON data
hist = hist.reset_index()
hist["Datetime"] = hist["Datetime"].astype(str)  # For timestamp
prices = hist[["Datetime", "Close"]].to_dict(orient='records')

print(json.dumps(prices))
