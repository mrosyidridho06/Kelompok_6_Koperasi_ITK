from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database/kantin.db')
Base = declarative_base()

def modelFactory():
    return Base.metadata.create_all(bind=engine)


SessionFactory = sessionmaker(bind=engine)
SessionFactory.configure(bind=engine)

def sessionFactory():
    return SessionFactory()
