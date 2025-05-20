import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_risk(portfolio):
    total = sum(portfolio.values())
    tech_stocks = ["AAPL", "TSLA", "NVDA", "MSFT", "GOOG"]
    tech_ratio = sum(portfolio.get(s, 0) for s in tech_stocks) / total
    risk_level = "High" if tech_ratio > 0.6 else "Moderate" if tech_ratio > 0.3 else "Low"
    prompt = f"Assess the risk of this portfolio: {portfolio}. It has {risk_level} tech exposure. Suggest diversification."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial risk advisor."},
            {"role": "user", "content": prompt}
        ]
    )
    return risk_level, response['choices'][0]['message']['content']

if __name__ == "__main__":
    portfolio = {"AAPL": 50, "TSLA": 30, "GOOG": 20}
    level, explanation = analyze_risk(portfolio)
    print(f"📊 Risk Level: {level}
🧠 GPT Insight: {explanation}")
