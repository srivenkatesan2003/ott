from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from .db import Base

class Account(Base):
    __tablename__ = "account"

    account_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    created_at=Column(DateTime)


class Select_Movie(Base):
    __tablename__ = "select_movies"

    account_id = Column(Integer,primary_key=True)
    user_name = Column(String)
    movies = Column(String,unique=bool)
    category = Column(Integer)
    year = Column(Integer)


