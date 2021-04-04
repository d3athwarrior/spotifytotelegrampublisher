try:
    from database import BASE, SESSION
except ImportError:
    raise AttributeError
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String

class SpotifyPlayedDB(BASE):
    __tablename__ = "spotifyplayedsong"
    name = Column(String(255), primary_key=True)
    album = Column(String(255), primary_key=True)
    artist = Column(String(255), primary_key=True)

    def __init__(self, name, album, artist):
        self.name = name
        self.album = album
        self.artist = artist
        return

SpotifyPlayedDB.__table__.create(checkfirst=True)

def is_song_published(name, album, artist):
    try:
        return SESSION.query(SpotifyPlayedDB).\
            filter(SpotifyPlayedDB.name == str(name), SpotifyPlayedDB.album == str(album), SpotifyPlayedDB.artist == str(artist)).one()
    except BaseException as ex:
        return None
    finally:
        SESSION.close()

def publish_song(name, album, artist):
    data_item = SpotifyPlayedDB(name=name, album=album, artist=artist)
    SESSION.add(data_item)
    SESSION.commit()
        