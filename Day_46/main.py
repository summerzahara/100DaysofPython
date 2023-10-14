import os

from bs4 import BeautifulSoup
from icecream import ic
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ["CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["CLIENT_SECRET"]

# prompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
prompt_date = "2000-08-12"

URL = f"https://www.billboard.com/charts/hot-100/{prompt_date}/"

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

songs = soup.select("li ul li h3")
song_titles = [song.get_text().strip() for song in songs]


ic(song_titles)