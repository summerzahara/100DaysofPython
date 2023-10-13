from bs4 import BeautifulSoup
from icecream import ic
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_list = []

for movie in movies:
    text = movie.get_text()
    movie_list.append(text)

movie_list.reverse()
ic(movie_list)

with open("movies.txt", "a") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")