# plex.py

import os
from plexapi.audio import Artist
from plexapi.exceptions import NotFound
from plexapi.server import PlexServer


class Plex:
    def __init__(self):
        url = os.getenv("PLEX_URL")
        token = os.getenv("PLEX_API_TOKEN")
        self.server = PlexServer(url, token)

    def get_artist(self, artist_name: str) -> Artist:
        try:
            return self.server.library.section("Music").get(artist_name)
        except NotFound:
            return None
