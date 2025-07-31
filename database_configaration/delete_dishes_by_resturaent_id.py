from sqlmodel import Session, select
from .models import Dishes
from .database_connection import engine
from .models import Restaurant, Dishes


def delete_restaurant_and_dishes(restaurant_id: int):
    with Session(engine) as session:
        statement = select(Dishes).where(Dishes.restaurant_id == restaurant_id)
        for dish in session.exec(statement).all():
            session.delete(dish)

        restaurant = session.get(Restaurant, restaurant_id)
        if restaurant:
            session.delete(restaurant)

        session.commit()
        print(f"Deleted restaurant {restaurant_id} and its dishes")
