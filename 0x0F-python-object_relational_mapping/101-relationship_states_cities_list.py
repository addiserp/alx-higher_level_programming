#!/usr/bin/python3
"""
  a script that lists all State objects, and corresponding City objects,
  contained in the database hbtn_0e_101_usa
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """
    Access to the database and get a relationsip state
    from the database 100.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    result_q = session.query(State).order_by(State.id)

    for state in result_q:
        print("{}: {}".format(state.id, city.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
