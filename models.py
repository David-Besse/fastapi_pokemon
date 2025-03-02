from sqlalchemy import Column, Integer, String
from database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    type = Column(String)
    image_url = Column(String)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    speed = Column(Integer)
    special_attack = Column(Integer)
    special_defense = Column(Integer)
