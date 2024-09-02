from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    tg_id = Column(Integer, primary_key=True, nullable=False)
    fortnite_username = Column(String)
    kills = Column(Integer, nullable=False, default=0)
    deaths = Column(Integer, nullable=False, default=0)
    matches = Column(Integer, nullable=False, default=0)
