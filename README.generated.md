# AI Stock Predictor Using LSTM

## Description
This AI Stock Predictor employs a Long Short-Term Memory (LSTM) network to predict the closing stock price of a publicly-traded company based on the past 60 days' stock prices.

## Disclaimer
This code is for educational purposes and NOT intended for actual stock trading.

## Features
- Utilizes LSTM, a type of Recurrent Neural Network (RNN).
- Predicts stock prices based on historical data.
- Includes visualization of stock price trends.
- Modular design with additional AI-powered analysis tools.
- Fun stock facts and logging utilities.
- Portfolio evaluation, risk analysis, and sentiment analysis using OpenAI's GPT-based large language models (LLM).

## Libraries Used
- TensorFlow
- Pandas DataReader
- NumPy
- Pandas
- Scikit-Learn
- Keras
- Matplotlib

## Implementation
- Data preprocessing with MinMaxScaler.
- Defining LSTM model layers.
- Model compilation and training.
- Stock price prediction and evaluation.
- Visualization of training and prediction results.
- Modular scripts for portfolio evaluation, risk analysis, and sentiment analysis.

## Usage
Replace the stock symbol in `DataReader` with the desired corporation's stock symbol to analyze different stocks.

## Project Structure
- `main.py`: LSTM-based stock price prediction.
- `ai_stock_predictor.py`: Simple AI-based stock prediction.
- `portfolio_evaluator.py`: Portfolio evaluation using GPT.
- `risk_analyzer.py`: Risk analysis using GPT.
- `earnings_sentiment.py`: Earnings sentiment analysis.
- `stock_fun_fact.py`: Fun stock facts.
- `logger.py`: Logging predictions.
- `data_fetcher.py`: Fetches historical stock data.

## Testing
No test files were found in the codebase, and thus there are no documented test commands or frameworks used for testing.

## Configuration
No specific configuration files or settings were found in the codebase. 

## Deployment
No deployment instructions or configuration files (like Docker or CI/CD configurations) were found in the codebase.

## Contributing
Information not found in codebase.

## License
Information not found in codebase.

---

### Notes:
- Consider adding instructions for setup and installation, as well as any potential contributing guidelines or licensing information if they are to be included in the repository.
- Including examples of stock prediction usage would enhance the README.
- Testing frameworks and commands should be added if they are implemented in the future.