# plex.py

import os
from plexapi.audio import Artist
from plexapi.exceptions import NotFound
from plexapi.server import PlexServer
import crud


class PlexWrapper:
    def __init__(self):
        url = os.getenv("PLEX_URL")
        token = os.getenv("PLEX_API_TOKEN")
        self.server = PlexServer(url, token)

    def get_artist(self, artist_name: str) -> Artist:
        try:
            return self.server.library.section("Music").get(artist_name)
        except NotFound:
            return None

    def get_track(self, track_name: str, artist_name: str) -> Artist:
        try:
            artist = self.server.library.section("Music").get(artist_name)
            return artist.track(title=track_name)
        except NotFound:
            return None

    def update_if_exists(self, playlist_name: str) -> None:
        tracks = crud.get_playlist_tracks(playlist_name=playlist_name)
        for track in tracks:
            artist = crud.get_track_artist(track.name)
            if self.get_artist(artist_name=artist.name):
                print(self.get_artist(artist_name=artist.name))
                crud.artist_on_plex(artist.name)
            if self.get_track(track_name=track.name, artist_name=artist.name):
                print(self.get_track(track_name=track.name, artist_name=artist.name))
                crud.track_on_plex(track_name=track.name)

    def percentage_on_plex(self, playlist_name: str) -> float:
        track_count = crud.get_playlist(playlist_name=playlist_name).length
        tracks = crud.tracks_on_plex(playlist_name=playlist_name)

        return (tracks / track_count) * 100
