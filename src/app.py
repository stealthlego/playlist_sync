# main.py

import dotenv

from spotify_wrapper import SpotifyWrapper
from plex_wrapper import PlexWrapper
from crud import create_db_tables

dotenv.load_dotenv(dotenv.find_dotenv())
create_db_tables()

sp = SpotifyWrapper()
px = PlexWrapper()


def import_playlist():
    global sp, px
    playlist_url = input("URL for playlist to import: ")

    # import playlist from spotify
    playlist_name = sp.import_playlist(
        playlist_url,
    )

    if px.does_playlist_exist(playlist_name=playlist_name):
        print("Playlist already exists in Plex, try updating instead")
    else:
        print(f"Importing {playlist_name} from Spotify...")

        # check and see if artist and track is on plex, update in db
        px_track_objs = px.update_if_exists(playlist_name=playlist_name)

        # calculate percentage of playlist in plex libarary
        print(f"Calculating overlap of {playlist_name} with Plex Library...")
        percentage = px.percentage_on_plex(playlist_name=playlist_name)
        print(f"{round(percentage, 0)}%")

        px.create_playlist(playlist_name=playlist_name, tracks=px_track_objs)


def update():
    global sp, px
    pass


def main():
    commands = {"1": import_playlist, "2": update, "3": quit}

    print("Welcome to Spotify to Plex Playlist Manager")
    while True:
        command = input(
            "What would you like to do?\n1: Import Playlist\n2: Update existing playlist\n3: Exit\nSelection: "
        )
        try:
            commands[command]()
        except KeyError:
            print("\nBad input, try again\n")


if __name__ == "__main__":
    main()
