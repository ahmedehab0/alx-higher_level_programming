#!/usr/bin/python3
"""
    script that prints the state object with
    name from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping = True)

    Session = sessionmaker(bind = engine)
    session = Session()

    query = session.query(State).filter(State.name == argv[4])
    if query is not None:
        for state in query:
            print("{}".format(state.id))
    else:
        print("Not found")
