# Stock Price Prediction Using LSTM

This repository provides a machine learning solution to predict stock closing prices using an LSTM (Long Short-Term Memory) model. The code retrieves historical stock price data and preprocesses it for training and testing an RNN model to make predictions based on the past 60 days of stock prices.

## Key Modules
- **TensorFlow and Keras:** Used for building and training the LSTM model.
- **Pandas & Numpy:** For data manipulation and numerical computations.
- **Matplotlib:** For visualizing stock price trends and predictions.
- **Pandas Datareader:** To fetch historical stock price data from Yahoo Finance.

## Installation
To get started, clone this repository and install the required dependencies:

```bash
git clone https://github.com/your_username/stock-price-prediction.git
cd stock-price-prediction
pip install -r requirements.txt
```

Ensure that you have Python 3.x installed.

## Quick Start
1. Import the necessary libraries:
   ```python
   import math
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   from sklearn.preprocessing import MinMaxScaler
   from keras.models import Sequential
   from keras.layers import Dense, LSTM
   from pandas_datareader import data as web
   ```

2. Preprocess the data:
   ```python
   # Fetch historical data
   df = web.DataReader("AAPL", data_source="yahoo", start="2012-01-01", end="2022-10-24")
   
   # Prepare data for LSTM
   data = df.filter(["Close"])
   dataset = data.values
   training_data_len = math.ceil(len(dataset) * 0.8)
   scaler = MinMaxScaler(feature_range=(0, 1))
   scaled_data = scaler.fit_transform(dataset)

   # Create training dataset
   train_data = scaled_data[0:training_data_len, :]
   past_days = 60
   x_train, y_train = [], []
   for i in range(past_days, len(train_data)):
       x_train.append(train_data[i-past_days:i, 0])
       y_train.append(train_data[i, 0])
   x_train, y_train = np.array(x_train), np.array(y_train)
   x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
   ```

3. Build and train the model:
   ```python
   model = Sequential()
   model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
   model.add(LSTM(50, return_sequences=False))
   model.add(Dense(25))
   model.add(Dense(1))
   model.compile(optimizer="adam", loss="mean_squared_error")
   model.fit(x_train, y_train, batch_size=1, epochs=1)
   ```

4. Make predictions and visualize:
   ```python
   # Create test dataset
   test_data = scaled_data[training_data_len - past_days:, :]
   x_test, y_test = [], dataset[training_data_len:, :]
   for i in range(past_days, len(test_data)):
       x_test.append(test_data[i-past_days:i, 0])
   x_test = np.array(x_test)
   x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
   
   # Make predictions
   predictions = model.predict(x_test)
   predictions = scaler.inverse_transform(predictions)

   # Visualize results
   train = data[:training_data_len]
   valid = data[training_data_len:]
   valid["Predictions"] = predictions
   plt.figure(figsize=(16,8))
   plt.title("Model")
   plt.xlabel("Date", fontsize=18)
   plt.ylabel("Close Price USD", fontsize=18)
   plt.plot(train["Close"])
   plt.plot(valid[["Close", "Predictions"]])
   plt.legend(["Train", "Validation", "Predictions"], loc="lower right")
   plt.show()
   ```

This code offers an excellent starting point for implementing stock price prediction using LSTM networks. Be sure to review and modify parameters based on your specific use case!