import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_portfolio(portfolio):
    prompt = f"Evaluate the following stock portfolio and suggest improvements: {portfolio}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial advisor AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    sample_portfolio = {
        "AAPL": 50,
        "TSLA": 30,
        "GOOG": 20
    }
    print(evaluate_portfolio(sample_portfolio))
