import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
db_path = os.path.join(os.path.dirname(__file__), 'koperasi.db')
db_uri = 'sqlite:///{}'.format(db_path)
engine = create_engine(db_uri)

__SessionFactory = sessionmaker(bind=engine)

def sessionFactory():
    Base.metadata.create_all(engine)
    return __SessionFactory()
