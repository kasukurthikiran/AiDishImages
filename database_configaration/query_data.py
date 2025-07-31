from .database_connection import get_session
from .models import Restaurant, Dishes
from contextlib import contextmanager
from sqlmodel import select


@contextmanager
def get_db_session():
    yield from get_session()


def query():
    with get_db_session() as session:
        statement = select(Dishes)
        dishes = session.exec(statement).all()
        for dish in dishes:
            print(dish.name)
            if dish.restaurant:
                print(dish.restaurant.name)
            else:
                print("no restarunt")
