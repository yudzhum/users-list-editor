from sqlalchemy import Column, Integer, String, create_engine
from user_db.db import BaseDBModel


#engine = create_engine('postgresql://yudzhum:charbox@localhost:5432/fastapitest')


class User(BaseDBModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True)
    group = Column(String(64), nullable=False)
    password_hash = Column(String(128), nullable=False)
    salt = Column(String(128), nullable=False, unique=True)
