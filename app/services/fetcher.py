import yfinance as yf

def get_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1m")

        if data is None or data.empty:
            return None

        return float(data["Close"].iloc[-1])

    except Exception as e:
        print(f"[FETCH ERROR] {symbol}: {e}")
        return None