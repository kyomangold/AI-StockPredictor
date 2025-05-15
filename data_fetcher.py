def fetch_historical_data(ticker):
    return [{"date": "2024-05-01", "close": 123.45}, {"date": "2024-05-02", "close": 124.67}]

if __name__ == "__main__":
    print(fetch_historical_data("TSLA"))
