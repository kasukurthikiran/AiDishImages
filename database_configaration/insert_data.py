from .models import Restaurant, Dishes
from .database_connection import get_session

from contextlib import contextmanager


@contextmanager
def get_db_session():
    yield from get_session()


def insert_data():
    with get_db_session() as session:
        restaurant = Restaurant(name="Tea Planent")
        dish1 = Dishes(name="Mutton Biryani", restaurant=restaurant)
        dish2 = Dishes(name="pork", restaurant=restaurant)
        session.add(restaurant)
        session.add(dish1)
        session.add(dish2)
        session.commit()
