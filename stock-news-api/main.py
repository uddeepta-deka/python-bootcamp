import yfinance as yf
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_TOKEN = "c10defddb27f4241ae7f36b05c291f81"

tk = yf.Ticker(ticker=STOCK_NAME)
hist = tk.history(period="2d")

positive_diff = abs(hist.Close[0]-hist.Close[1])
perc_diff = positive_diff * 100 / hist.Close[1]

if perc_diff > 5:
    # print("Get News")
    news_api_params = {
        "apiKey": NEWS_API_TOKEN,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_api_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
