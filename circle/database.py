from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


_engine = create_engine('sqlite:///database.sqlite', echo=True)
Base = declarative_base(bind=_engine)
_Session = scoped_session(sessionmaker(bind=_engine))


def session():
  return _Session()
