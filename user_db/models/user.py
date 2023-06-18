from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

engine = create_engine('postgresql://yudzhum:charbox@localhost:5432/fastapitest')


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    group = Column(String(64))
    password = Column(String(128))
