# main.py

from sqlmodel import SQLModel, Session, create_engine

from schemas import Playlist, Artist, Track

db_url = "sqlite://"
engine = create_engine(db_url, echo=True)


def create_db_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_tables()


if __name__ == "__main__":
    main()
