from bs4 import BeautifulSoup
from icecream import ic
#import lxml

with open("website.html", "r") as website:
    data = website.read()

soup = BeautifulSoup(data, "html.parser")
# ic(soup.title)
# ic(soup.title.name)
# ic(soup)
all_tags = soup.findAll(name="a")
# ic(all_tags)

# for tag in all_tags:
#     ic(tag.getText())
#     ic(tag.get("href"))


heading = soup.find(name="h1", id="name")
sect_heading = soup.find(name="h3", class_="heading")
ic(heading)
ic(sect_heading.getText())

company_url = soup.select_one(selector="p a")
ic(company_url)

headings = soup.select(".heading")
ic(headings)