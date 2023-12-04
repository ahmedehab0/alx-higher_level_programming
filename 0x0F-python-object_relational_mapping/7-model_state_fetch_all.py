#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


import sys
from model_state import State, Base
from model_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping = True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind = engine)
    session = Session()

    state1 = State(name = "California")
    state2 = State(name = "Arizona")
    state3 = State(name = "Texas")
    state4 = State(name = "New York")
    state5 = State(name = "Nevada")
    city1 = City(name = "egypt")

    session.add_all([state1, state2, state3, state4])
    session.commit()

    for i in session.query(State):
        print(i)
