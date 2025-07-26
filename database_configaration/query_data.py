from .database_connection import get_session
from .models import Restaurant, Dishes  # assuming this contains your model
from contextlib import contextmanager
from sqlmodel import select


@contextmanager
def get_db_session():
    yield from get_session()  # get_session yields the session


def query():
    with get_db_session() as session:
        # statement = select(Restaurant)
        # results = session.exec(statement).all()
        # for r in results:
        #     print(f"{r.name} with dishes:")
        #     for d in r.dishes:
        #         print(f"  - {d.name}")
        statement = select(Dishes)
        dishes = session.exec(statement).all()
        for dish in dishes:
            print(dish.name)
            if dish.restaurant:
                print(dish.restaurant.name)
            else:
                print("no restarunt")
