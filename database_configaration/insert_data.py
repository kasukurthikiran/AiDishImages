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

        # from .models import Restaurant, Dishes
        # from .database_connection import get_session

        # from contextlib import contextmanager

        # @contextmanager
        # def get_db_session():
        #     yield from get_session()

        # def insert_data_with_manual_dish_id():
        #     with get_db_session() as session:
        #         restaurant = Restaurant(name="Paradise Hotel")
        #         session.add(restaurant)
        #         session.commit()
        #         session.refresh(restaurant)  # to get the auto-generated restaurant.id

        #         dish1 = Dishes(id=101, name="Fish Fry", restaurant_id=restaurant.id)
        #         dish2 = Dishes(id=102, name="Egg Curry", restaurant_id=restaurant.id)

        #         session.add(dish1)
        #         session.add(dish2)
        session.commit()
