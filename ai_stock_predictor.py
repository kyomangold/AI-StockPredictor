import random

def predict_stock(ticker):
    return {"ticker": ticker, "prediction": round(random.uniform(-0.1, 0.1), 3)}

if __name__ == "__main__":
    print(predict_stock("AAPL"))
