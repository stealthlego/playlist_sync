# spotify.py

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import crud
from schemas import Playlist


class SpotifyWrapper:
    def __init__(self) -> None:
        scope = "user-library-read"

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def get_spotify_playlist(self, url: str):
        return self.sp.playlist(url)

    def import_playlist(self, url: str) -> None:
        playlist_data = self.get_spotify_playlist(url)

        # TODO parse playlist_data

        crud.create_playlist(spotify_id=playlist_data["id"], name=playlist_data["name"])
        for track_obj in playlist_data["tracks"]["items"]:

            # parse track and artist data
            track_data = track_obj["track"]
            track_id = track_data["id"]
            track_name = track_data["name"]
            artist_id = track_data["artists"][0]["id"]
            artist_name = track_data["artists"][0]["name"]

            # add the artist
            crud.create_artist(spotify_id=artist_id, name=artist_name)

            # add the track
            track = crud.create_track(
                spotify_id=track_id, name=track_name, artist_id=artist_id
            )

            # add update the playlist
            crud.add_track_to_playlist(track_id, playlist_data["id"])
