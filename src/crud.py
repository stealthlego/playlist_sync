# crud.py

from sqlalchemy.orm import selectinload
from sqlmodel import Session, SQLModel, create_engine, select
from schemas import Playlist, Artist, Track, PlaylistTrackLink

db_url = "sqlite://"
engine = create_engine(db_url)


def create_db_tables():
    global engine
    SQLModel.metadata.create_all(engine)


def create_playlist(spotify_id: str, name: str) -> Playlist:
    with Session(engine) as session:
        playlist = Playlist(spotify_id=spotify_id, name=name, tracks=[])

        session.add(playlist)
        session.commit()
        session.refresh(playlist)
        # print(playlist)

    # print(playlist)
    # return playlist


def create_track(spotify_id: str, name: str, artist_id: str) -> Track:
    with Session(engine) as session:
        statement = select(Artist).where(Artist.spotify_id == artist_id)
        artist = session.execute(statement).first()[0]

        track = Track(
            spotify_id=spotify_id,
            name=name,
            artist=artist,
            artist_id=artist.id,
            playlists=[],
        )

        session.add(track)
        session.commit()
    #     session.refresh(track)

    # return track


def create_artist(spotify_id: str, name: str) -> Artist:
    with Session(engine) as session:
        artist = Artist(spotify_id=spotify_id, name=name)

        session.add(artist)
        session.commit()
        session.refresh(artist)

    return artist


def add_track_to_playlist(track_id: Track, playlist_id: Playlist):
    with Session(engine) as session:
        statement = select(Playlist).where(Playlist.spotify_id == playlist_id)
        playlist = session.execute(statement).first()[0]

        statement = select(Track).where(Track.spotify_id == track_id)
        track = session.execute(statement).first()[0]

        track.playlists.append(playlist)
        playlist.tracks.append(track)
        playlist.length += 1

        session.add(track)
        session.add(playlist)
        session.commit()
        session.refresh(playlist)
        session.refresh(track)


def get_playlist_tracks(playlist_name: str):
    with Session(engine) as session:
        statement = select(Playlist).where(Playlist.name == playlist_name)
        return session.exec(statement).first().tracks


def get_track_artist(track_name: str):
    with Session(engine) as session:
        statement = select(Track).where(Track.name == track_name)
        return session.exec(statement).first().artist


def artist_on_plex(artist_name: str):
    with Session(engine) as session:
        statement = select(Artist).where(Artist.name == artist_name)
        artist = session.exec(statement).first()
        artist.on_plex = True
        session.add(artist)
        session.commit()


def track_on_plex(track_name: str):
    with Session(engine) as session:
        statement = select(Track).where(Track.name == track_name)
        track = session.exec(statement).first()
        track.on_plex = True
        session.add(track)
        session.commit()


def get_playlist(playlist_name: str):
    with Session(engine) as session:
        statement = select(Playlist).where(Playlist.name == playlist_name)
        return session.exec(statement).first()


def tracks_on_plex(playlist_name: str) -> int:
    with Session(engine) as session:
        statement = (
            select(Playlist)
            .where(Playlist.name == playlist_name)
            .where(Track.on_plex == True)
        )
        tracks = session.exec(statement).fetchall()
        return len(tracks)
