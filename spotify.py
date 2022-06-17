# spotify.py

import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self) -> None:
        scope = "user-library-read"

        self.spot = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def get_playlist(self, url: str) -> dict:
        results = self.spot.playlist(url)
        for item in results["tracks"]["items"]:
            print(item["track"]["name"] + " by " + item["track"]["artists"][0]["name"])

        return {}
