#!/home/ad/venv/bin/python3
"""
 a script that creates the State “California” with the City
 “San Francisco” from the database hbtn_0e_100_usa:
 (100-relationship_states_cities.py)
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """
    Access to the database and get a relationsip state
    from the database 100.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name='California')
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_city)
    session.commit()
