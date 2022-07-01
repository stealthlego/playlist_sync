# main.py

import dotenv

from spotify_wrapper import SpotifyWrapper
from plex_wrapper import PlexWrapper
from crud import create_db_tables

dotenv.load_dotenv(dotenv.find_dotenv())


def main():
    create_db_tables()
    sp = SpotifyWrapper()
    px = PlexWrapper()

    # import playlist from spotify
    sp.import_playlist(
        "https://open.spotify.com/playlist/0d4WK4fZXWGWiNXTkxUIkI?si=8dfdf04239f4445c",
    )

    # check and see if artist and track is on plex, update in db
    px.update_if_exists("Lazer Lemonade")

    # calculate percentage of playlist in plex libarary
    percentage = px.percentage_on_plex("Lazer Lemonade")
    print(f"{round(percentage, 0)}%")

    # artist = px.get_artist("Daft Punk")
    # print(artist.albums())


if __name__ == "__main__":
    main()
