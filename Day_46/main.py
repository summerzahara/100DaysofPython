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
SCOPE = "playlist-modify-private"
REDIRECT_URI = "http://example.com"
USER_NAME = "Summer Zahara"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    username=USER_NAME,
    show_dialog=True,
    cache_path="token.txt",
))

user_id = sp.current_user()["id"]

# Scrape the billboard top 100
prompt = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{prompt}/"

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

songs = soup.select("li ul li h3")
song_titles = [song.get_text().strip() for song in songs]

# Search for tracks in Spotify
spotify_search = []
for title in song_titles:
    track = sp.search(
        f"track:{title} year:{prompt[:4]}",
        limit=5,
        offset=0,
        type="track",
        market=None
    )
    try:
        uri = track["tracks"]["items"][0]["uri"]
        spotify_search.append(uri)
        ic("added")
    except IndexError:
        ic("skipped")

ic(len(spotify_search))

# Create a new playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{prompt} Billboard 100",
    public=False,
    collaborative=False,
    description="Billboard top 100 by date"
)


sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=spotify_search,
)

