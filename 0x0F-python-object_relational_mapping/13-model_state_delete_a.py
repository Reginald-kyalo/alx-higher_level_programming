from model_state import Base, State
import sys

if __name__ == "main":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create.all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in a_states:
        session.delete(state)
    
    session.commit()
    session.close()
