import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()
from twilio.rest import Client

# STOCK = "TSLA"
STOCK = "CRM"
# COMPANY_NAME = "Tesla"
COMPANY_NAME = "Salesforce"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

today = datetime.today()
yesterday = str((today - timedelta(days=1)).date())
day_before_yesterday = str((today - timedelta(days=2)).date())
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

stock_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
stock_parameters = {
    "apikey": os.environ.get("STOCK_API_KEY"),
    "symbol": STOCK
}

news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    'q': COMPANY_NAME.lower(),
    'from': yesterday, 
    'apiKey': os.environ.get("NEWS_API_KEY")
}

response = requests.get(stock_url, stock_parameters).json()
yesterday_price = float(response['Time Series (Daily)'][yesterday]["4. close"])
day_before_price = float(response['Time Series (Daily)'][day_before_yesterday]["4. close"])

price_diff = yesterday_price - day_before_price
price_diff_ratio = round((price_diff / day_before_price) * 100, 2)
direction = "🔺" if price_diff > 0 else "🔻"

if abs(price_diff_ratio) > 5:
    news_response = requests.get(news_url, news_parameters).json()
    articles = news_response["articles"][:3]
    client = Client(account_sid, auth_token)
    for article in articles:
        message = (
            f"{STOCK}: {direction}{abs(price_diff_ratio)}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            to='whatsapp:+420735032331'
        )
   




