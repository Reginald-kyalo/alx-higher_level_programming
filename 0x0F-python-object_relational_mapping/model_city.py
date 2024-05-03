#!/usr/bin/python3
"""contains class City
inherits from sqlalchemy Base and links to mysql tables
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

"""Defines class State"""
class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False ForeignKey('states.id'))

    state = relationship("State", backref="cities")

    def __repr__:
        return f"{State.name}: ({City.id}) {City.name}"
