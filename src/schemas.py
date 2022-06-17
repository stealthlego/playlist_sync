# schemas.py

from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
import datetime


class Playlist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spotify_id: str
    name: str
    synced: bool
    last_synced: datetime.datetime = None
    length: int
    tracks: List["Track"] = Relationship(back_populates="playlist")


class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spotify_id: str
    name: str
    on_plex: bool
    tracks: Optional[List["Track"]] = Relationship(back_populates="artist")


class Track(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    spotify_id: str
    name: str
    artist: Artist = Relationship(back_populates="track")
    on_plex: bool
    playlists: Optional[List[Playlist]] = Relationship(back_populates="track")
