import os

import requests
from icecream import ic
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/gp/product/B0B7RSV894/ref=ox_sc_saved_title_6?smid=A3H3ISK374NPRT&th=1"
c_url = " https://camelcamelcamel.com/product/B0B7RSV894"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "PHPSESSID=a4abda42bdd862cc97c46e85503723be; _ga=GA1.2.2122134454.1697330988; "
              "_gid=GA1.2.543873955.1697330988; _ga_VL41109FEB=GS1.2.1697330988.1.0.1697330988.0.0.0",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}

response = requests.get(url=c_url, headers=header)
response.raise_for_status()
data = response.text

# Scrape site for price
soup = BeautifulSoup(data, "html.parser")
price = float(soup.find(name="span", class_="green").get_text()[1:])
product = soup.select("h2 a")[0].get_text()
ic(price)
ic(product)

# Send email when price drops below target

sender_email = os.environ["SENDER_EMAIL"]
password = os.environ["APP_PASSWORD"]
to_email = os.environ["TO_EMAIL"]

target_price = 60.00
message = f"{product} is now {price}\n{url}"
ic(message)
if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=to_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )