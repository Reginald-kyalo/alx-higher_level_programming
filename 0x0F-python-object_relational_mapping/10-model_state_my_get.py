from model_state import Base, State
import sys

if __name__ == "main":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create.all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name)
    if state:
        print(state)
    else:
        print("Not found")

    session.close()
