from sqlmodel import Session, select
from .models import Dishes
from .database_connection import engine


def delete_dish_by_id(dish_id: int):
    with Session(engine) as session:
        statement = select(Dishes).where(Dishes.id == dish_id)
        dish = session.exec(statement).first()

        if dish:
            session.delete(dish)
            session.commit()
            print(f"Deleted dish with id={dish_id}")
        else:
            print("Dish not found")
