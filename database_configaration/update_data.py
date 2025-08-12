from .models import Restaurant, Dishes
from .database_connection import get_session

from contextlib import contextmanager
from .un_matched_records_table import UNMATCHEDRECORDS
from sqlmodel import select


@contextmanager
def get_db_session():
    yield from get_session()


def update_data():
    with get_db_session() as session:
        statement = select(UNMATCHEDRECORDS).where(UNMATCHEDRECORDS.id == "1")
        result = session.exec(statement).first()
        if result:
            result.name = "horse"
            session.add(result)
            session.commit()
            session.refresh(result)
            return {"message": "Updated successfully", "data": result}
        else:
            return {"error": "Restaurant not found"}
        # restaurant = Restaurant(name="Tea Planent")
        # dish1 = UNMATCHEDRECORDS(name="chicken Biryani", r_id=123)
        # dish2 = UNMATCHEDRECORDS(name="tea", r_id=123)
        # session.add(dish1)
        # session.add(dish2)
        # session.commit()
        # statement = select(Restaurant).where(Restaurant.id == restaurant_id)


# statement = select(UNMATCHEDRECORDS).where(UNMATCHEDRECORDS.id == restaurant_id)
#         result = session.exec(statement).first()

#         if result:
#             result.name = new_name
#             session.add(result)
#             session.commit()
#             session.refresh(result)
#             return {"message": "Updated successfully", "data": result}
#         else:
#             return {"error": "Restaurant not found"}
