from .models import Restaurant, Dishes
from .database_connection import get_session

from contextlib import contextmanager
from .un_matched_records_table import UNMATCHEDRECORDS


@contextmanager
def get_db_session():
    yield from get_session()


def insert_data():
    with get_db_session() as session:
        # restaurant = Restaurant(name="Tea Planent")
        dish1 = UNMATCHEDRECORDS(name="chicken Biryani", r_id=123)
        dish2 = UNMATCHEDRECORDS(name="tea", r_id=123)
        session.add(dish1)
        session.add(dish2)
        session.commit()
