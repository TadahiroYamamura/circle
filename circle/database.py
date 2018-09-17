from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


_engine = create_engine('sqlite:///database.sqlite', echo=True)

Base = declarative_base(bind=_engine)
print('database imported')
