from datetime import datetime
from ai_stock_predictor import predict_stock

def log_prediction(ticker):
    pred = predict_stock(ticker)
    with open("predictions.log", "a") as f:
        f.write(f"{datetime.now()} - {pred}
")

if __name__ == "__main__":
    log_prediction("GOOG")
