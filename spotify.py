# spotify.py

import dotenv
from dotenv import find_dotenv
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv(find_dotenv())
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

scope = "user-library-read"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = spotify.playlist(
    "https://open.spotify.com/playlist/0d4WK4fZXWGWiNXTkxUIkI?si=8dfdf04239f4445c"
)
for item in results["tracks"]["items"]:
    print(item["track"]["name"] + " by " + item["track"]["artists"][0]["name"])
