from sqlmodel import Session, select
from .models import Dishes
from .un_matched_records_table import UNMATCHEDRECORDS
from .database_connection import engine


def delete_dish_by_id(dish_id: str):
    with Session(engine) as session:
        statement = select(UNMATCHEDRECORDS).where(UNMATCHEDRECORDS.id == dish_id)
        dish = session.exec(statement).first()

        if dish:
            session.delete(dish)
            session.commit()
            print(f"Deleted dish with id={dish_id}")
        else:
            print("Dish not found")
