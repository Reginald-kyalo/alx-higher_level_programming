#!/usr/bin/python3
"""contains class state
inherits from sqlalchemy Base and links to mysql tables
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """represents a state for sql

    __tablename__ (str): name of sql table to store to
    id: state id
    name: state name
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
