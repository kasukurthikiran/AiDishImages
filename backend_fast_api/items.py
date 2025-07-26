# # routers/items.py
# from fastapi import APIRouter

# router = APIRouter()


# @router.get("/items")
# async def get_items():
#     return {"message": "List of items"}


# @router.get("/items/{item_id}")
# async def get_item(item_id: int):
#     return {"item_id": item_id}


# @router.get("/items/popular")
# async def get_popular_items():
#     return {"message": "Popular items list"}


# @router.get("/items/by-name/{name}")
# async def get_item_by_name(name: str):
#     return {"message": f"Item with name {name}"}


from fastapi import APIRouter
from database_configaration import database_connection
from database_configaration.models import Dishes, Restaurant

from contextlib import contextmanager

from pydantic import BaseModel

router = APIRouter()


@contextmanager
def get_db_session():
    yield from database_connection.get_session()


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
