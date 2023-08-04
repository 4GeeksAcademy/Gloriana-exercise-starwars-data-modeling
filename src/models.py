import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    height = Column(Float)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    id_planet = Column(Integer,ForeignKey('planets.id'))
    planets = relationship('Planet', back_populates='characters') 

class Starship(Base):
    __tablename__  = 'starships'
    id = Column(Integer,primary_key = True)
    name = Column(String(250))
    model = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))

class Pilot_Starship(Base):
    __tablename__ = 'pilot-starship'
    id_starship = Column(Integer,ForeignKey('starships.id'),primary_key = True)
    starships = relationship('Starship', back_populates='pilot-starship') 
    id_character = Column(Integer,ForeignKey('characters.id'),primary_key = True)
    characters = relationship('Character', back_populates='pilot-starship') 

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    id_character = Column(Integer,ForeignKey('characters.id'),primary_key = True)
    characters = relationship('Character', back_populates='favorite_characters') 

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    id_planet = Column(Integer,ForeignKey('planets.id'),primary_key = True)
    planets = relationship('Planet', back_populates='favorite_planets') 

class FavoriteStarship(Base):
    __tablename__ = 'favorite_starships'
    id_starship = Column(Integer,ForeignKey('starships.id'),primary_key = True)
    starships = relationship('Starship', back_populates='favorite_starships') 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
