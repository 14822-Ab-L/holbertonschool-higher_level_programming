#!/usr/bin/python3
"""List cities with their corresponding state names."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(
        City
    ).order_by(City.id.asc()).all()

    for state, city in results:
        print("{}: ({}) {}".format(
            state.name, city.id, city.name
        ))

    session.close()
