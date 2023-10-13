from bs4 import BeautifulSoup
import requests
from icecream import ic

response = requests.get("https://news.ycombinator.com/")
y_website = response.text

soup = BeautifulSoup(y_website, "html.parser")

a_tags = soup.findAll(name="span", class_="titleline")
# ic(a_tags)

span_title = soup.find_all(name="span", class_="titleline")
ic(span_title)
article_text = []
article_links = []
for article_span in span_title:
    text = article_span.get_text()
    article_text.append(text)
    link = article_span.contents[0].get("href")
    article_links.append(link)
# ic(article_text)
# ic(article_links)

article_upvote = soup.find_all(name="span", class_="score")
article_upvotes = []
for upvote in article_upvote:
    count = int(upvote.get_text().split()[0])
    article_upvotes.append(count)
# ic(article_upvotes)

highest = 0
for item in article_upvotes:
    if item > highest:
        highest = item

highest_check = max(article_upvotes)
ic(highest_check)

highest_index =article_upvotes.index(highest)
ic(highest_index)
ic(article_text[highest_index])
ic(article_links[highest_index])