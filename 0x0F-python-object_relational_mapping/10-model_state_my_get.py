#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    for state in session.query(State):
        if state.name == state_name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")

    session.close()
