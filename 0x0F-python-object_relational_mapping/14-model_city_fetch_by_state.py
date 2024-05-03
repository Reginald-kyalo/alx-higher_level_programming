#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create.all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).all()
    for city in cities:
        print(city)

    session.commit()
    session.close()
