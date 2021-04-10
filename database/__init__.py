from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from spotifypublisher import DB_URI

BASE = declarative_base()

engine = create_engine(DB_URI)
BASE.metadata.bind = engine
BASE.metadata.create_all(engine)

SESSION : scoped_session = scoped_session(sessionmaker(bind=engine, autoflush=False))
 
