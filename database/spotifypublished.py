try:
    from database import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column
from sqlalchemy.sql.expression import false
from sqlalchemy.sql.sqltypes import DateTime, String
from datetime import datetime

# I guess it might be a better idea to switch to a nosql database rather than using a sql based database.
# i am not sure on that front but if that feels like a right choice here, I will do it
class SpotifyPlayed(BASE):
    __tablename__ = "spotifyplayedsong"
    name = Column(String(255), primary_key=True)
    album = Column(String(255), primary_key=True)
    artist = Column(String(255), primary_key=True)
    last_played = Column(DateTime(), nullable=False)

    def __init__(self, name, album, artist, last_played):
        self.name = name
        self.album = album
        self.artist = artist
        self.last_played = last_played
        return

SpotifyPlayed.__table__.create(checkfirst=True)

def is_song_published(name, album, artist):
    try:
        return SESSION.query(SpotifyPlayed).\
            filter(SpotifyPlayed.name == str(name), SpotifyPlayed.album == str(album), SpotifyPlayed.artist == str(artist)).one()
    except BaseException as ex:
        return None
    finally:
        SESSION.close()

def publish_song(name: str = None, album: str = None, artist: str = None, song_detail: SpotifyPlayed = None):
    # If song detail is none, it means that the song is being published for the first time
    # else we simply persist the existing data that was fetched from the DB earlier
    if (song_detail is None):
        data_item: SpotifyPlayed = SpotifyPlayed(name=name, album=album, artist=artist, last_played=datetime.now())
        SESSION.add(data_item)
    else:
        song_detail.last_played = datetime.now()
    SESSION.commit()
        