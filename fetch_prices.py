import yfinance as yf
import sys
import json

symbol = sys.argv[1] if len(sys.argv) > 1 else 'AAPL'
ticker = yf.Ticker(symbol)
hist = ticker.history(period="1mo")

# Ensure at least one row is returned
if hist.empty:
    print(json.dumps([]))
    sys.exit()

# Prepare JSON data
hist = hist.reset_index()
hist["Date"] = hist["Date"].astype(str)
prices = hist[["Date", "Close"]].to_dict(orient='records')

print(json.dumps(prices))