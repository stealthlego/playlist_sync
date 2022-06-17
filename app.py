# main.py

import dotenv
from sqlmodel import SQLModel, Session, create_engine

from schemas import Playlist, Artist, Track
from spotify import Spotify
from plex import Plex

db_url = "sqlite://"
engine = create_engine(db_url, echo=True)


def create_db_tables():
    SQLModel.metadata.create_all(engine)


def main():
    dotenv.load_dotenv(dotenv.find_dotenv())
    create_db_tables()
    sp = Spotify()
    px = Plex()

    playlist = sp.get_playlist(
        "https://open.spotify.com/playlist/0d4WK4fZXWGWiNXTkxUIkI?si=8dfdf04239f4445c",
    )
    print(playlist)

    artist = px.get_artist("Daft Punk")
    print(artist.albums())


if __name__ == "__main__":
    main()
