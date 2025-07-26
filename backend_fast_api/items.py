from fastapi import APIRouter
from ..database_configaration.models import Dishes, Restaurant
from ..database_configaration.database_connection import get_session

from contextlib import contextmanager

from pydantic import BaseModel

router = APIRouter()


@contextmanager
def get_db_session():
    yield from get_session()


class Dish(BaseModel):
    id: int
    name: str


@router.post("/dishes")
async def create_items(dishe: Dish):
    with get_db_session() as session:
        # Create a restaurant
        restaurant = Restaurant(name="Paradise Hotel")
        session.add(restaurant)
        session.commit()
        session.refresh(restaurant)

        # Add the dish linked to the restaurant
        dish1 = Dishes(id=dishe.id, name=dishe.name, restaurant_id=restaurant.id)
        session.add(dish1)
        session.commit()

    return {"message": f"Dish '{dishe.name}' added to restaurant 'Paradise Hotel'"}
