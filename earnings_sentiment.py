import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_earnings_sentiment(ticker, snippet):
    prompt = f"Analyze the sentiment of the following earnings report snippet for {ticker}: {snippet}. Give a one-word sentiment (bullish, neutral, bearish) and explain why."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial sentiment analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    example = 'We beat EPS expectations and project continued growth in cloud services and international sales.'
    print(analyze_earnings_sentiment('MSFT', example))
