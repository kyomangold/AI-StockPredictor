# Description: This code uses an Recurrent Neural Network (RNN) structure called Long-Short-Term-Memory (LSTM) to predict the closing stock price of a corporation using past 60 days stock price
# This code is for educational purposes only and is not recommended for use in trading stocks

# import necessary libraries
import math
import tensorflow as tf
import pandas_datareader as web
import numpy as np
import pandas as pd
#pd.options.mode.chained_assignment = None  # default='warn'
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

# define past days to be looked at (aka timestep)
past_days = 60

# get the stock quote
df = web.DataReader("AAPL", data_source="yahoo", start="2012-01-01", end="2022-10-24")

# visualize closing prize history
plt.figure(figsize=(16,8))
plt.title("Closing prize history")
plt.plot(df["Close"])
plt.xlabel("Data", fontsize=18)
plt.ylabel("Close price USD", fontsize=18)
plt.show()

# create a new dataframe with only close column
data = df.filter(["Close"])
# convert dataframe to numpy array
dataset = data.values
# get number of rows to train model
training_data_len = math.ceil(len(dataset) *0.8)

# scale the data (preprocessing)
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

# create training dataset
# create scaled training dataset
train_data = scaled_data[0:training_data_len, :]
# split data in x_train, y_train
x_train = []
y_train = []

for i in range(past_days, len(train_data)):
    x_train.append(train_data[i-past_days:i, 0])
    y_train.append(train_data[i, 0])
    if i<=past_days:
        print(x_train)
        print(y_train)
        print()
    
# convert x_train, y_train  to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)

# reshape the data (why: lstm expects 3d data) we have 1 feature which is closing price
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# build lstm model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# compile model
model.compile(optimizer="adam", loss="mean_squared_error")

# train model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# create the testing dataset
# create new array containing scaled values
test_data = scaled_data[training_data_len-past_days: , :]
# create datasest for test
x_test = []
y_test = dataset[training_data_len:, :]

for i in range(past_days, len(test_data)):
    x_test.append(test_data[i-60:i, 0])
    
# convert data to numpy array
x_test = np.array(x_test)

# reshape data (number of rows/entries/samples, number of columns/timesteps, number of features (close price))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# get model's predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# evaluate model by RMSE
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(rmse)

# plot data
train = data[:training_data_len]
valid = data[training_data_len:]
valid["Predictions"] = predictions

# visualize
plt.figure(figsize=(16,8))
plt.title("Model")
plt.xlabel("Date", fontsize=18)
plt.ylabel("Close Prize in USD", fontsize=18)
plt.plot(train["Close"])
plt.plot(valid[["Close", "Predictions"]])
plt.legend(["Train","Validation", "Predictions"], loc="lower right")
plt.show()

# get the quote
aapl_quote = web.DataReader("AAPL", data_source="yahoo", start="2012-01-01", end="2022-10-24")
# creat a new dataframe
new_df = aapl_quote.filter(["Close"])
# get last 60 day closing price values and convert df to array
last_60_days = new_df[-60:].values
# scale data
last_60_days_scaled = scaler.transform(last_60_days)
# create empty list
X_test = []
X_test.append(last_60_days_scaled)
#convert X_test dataset to numpy array
X_test = np.array(X_test)
# reshape the data
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
# get predicted scaled price
pred_price = model.predict(X_test)
# undo scaling
pred_price = scaler.inverse_transform(pred_price)
print(pred_price)

