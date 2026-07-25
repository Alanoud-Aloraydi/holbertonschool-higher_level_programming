#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # كسر السطر لتجنب تجاوز 79 حرفاً (PEP8)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # كسر سطر الاستعلام الطويل ليتوافق مع PEP8
    query = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
