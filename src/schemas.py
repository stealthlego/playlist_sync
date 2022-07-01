# schemas.py

from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
import datetime


class PlaylistTrackLink(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    playlist_id: int = Field(default=None, foreign_key="playlist.id", primary_key=True)
    track_id: int = Field(default=None, foreign_key="track.id", primary_key=True)


class Playlist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spotify_id: str
    name: str
    synced: bool = False
    last_synced: Optional[datetime.datetime]
    length: int = 0

    tracks: List["Track"] = Relationship(
        back_populates="playlists", link_model=PlaylistTrackLink
    )


class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spotify_id: str
    name: str
    on_plex: bool = False

    tracks: List["Track"] = Relationship(back_populates="artist")


class Track(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spotify_id: str
    name: str
    on_plex: bool = False

    artist_id: int = Field(foreign_key="artist.id")
    artist: Artist = Relationship(back_populates="tracks")

    playlists: List[Playlist] = Relationship(
        back_populates="tracks", link_model=PlaylistTrackLink
    )
