#!/usr/bin/python3
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind = engine)
    session = Session()

    city1 = City(name = "San Fransisco", state_id = 1)
    city2 = City(name = "san jose", state_id = 1)
    city3 = City(state_id = 1)
    setattr(city3, "name", "cali")

    session.add_all([city1, city2, city3])
    session.commit()

    for i, state in session.query(City, State).join(State).order_by(City.state_id).all():
        print("{}: ({}) {}".format(state.name, i.state_id, i.name))
