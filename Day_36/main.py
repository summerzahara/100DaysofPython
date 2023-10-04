import os
import requests
from datetime import datetime as dt, timedelta
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

API_KEY = os.environ.get("API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
PHONE = os.environ.get("PHONE")

date = dt.now()
TODAY = f"{date.year}-{date.month:02d}-{date.day:02d}"
TODAY_NEWS = date.strftime("%Y%m%dT%H%M")
YESTERDAY = f"{date.year}-{date.month:02d}-{date.day - 1:02d}"
YESTERDAY_NEWS = (date - timedelta(days=1)).strftime("%Y%m%dT%H%M")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_price_delta():
    today = float(data["Time Series (Daily)"][TODAY]["2. high"])
    yesterday = float(data["Time Series (Daily)"][YESTERDAY]["2. high"])
    positive = True
    # delta = today - yesterday
    delta = -20
    percent_delta = today * .05
    percent_change = round((delta / today) * 100, 2)
    if delta < 0:
        positive = False
        delta *= -1

    if delta >= percent_delta:
        articles = get_news()
        messages = []
        for n in range(0, 2):
            if positive:
                messages.append(f"{STOCK}: 🔺{percent_change}%\nHeadline: {articles[0][n]}\nBrief: {articles[1][n]}")
            else:
                messages.append(f"{STOCK}: 🔻{percent_change}%\nHeadline: {articles[0][n]}\nBrief: {articles[1][n]}")
        for message in messages:
            send_text(message)
            print(message)
            print("\n")
    else:
        print("Low change")


# check_price_delta()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
news_response.raise_for_status()
news_data = news_response.json()


def get_news():
    top_three = news_data["articles"]
    n = 0
    headlines = []
    briefs = []
    for article in top_three:
        n += 1
        if n <= 3:
            headlines.append(article["title"])
            briefs.append(article["description"])
    articles = [headlines, briefs]
    return articles


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


def send_text(msg):
    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18885962831',
        body=f"{msg}",
        to=PHONE
    )
    print(message.status)


check_price_delta()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
