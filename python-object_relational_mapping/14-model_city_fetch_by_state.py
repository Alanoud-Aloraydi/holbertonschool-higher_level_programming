#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).join(City).order_by(City.id)
    for state, city in query.all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
