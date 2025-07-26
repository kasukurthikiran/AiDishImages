from fastapi import APIRouter
from fastapi import UploadFile, File
# from ..database_configaration.models import Dishes, Restaurant
# from ..database_configaration.database_connection import get_session

# from contextlib import contextmanager

from pydantic import BaseModel

router = APIRouter()


# @contextmanager
# def get_db_session():
#     yield from get_session()


# @router.post("/dishes")
# async def create_items(dishe: Dish):
#     with get_db_session() as session:
#         # Create a restaurant
#         restaurant = Restaurant(name="Paradise Hotel")
#         session.add(restaurant)
#         session.commit()
#         session.refresh(restaurant)

#         # Add the dish linked to the restaurant
#         dish1 = Dishes(id=dishe.id, name=dishe.name, restaurant_id=restaurant.id)
#         session.add(dish1)
#         session.commit()

#     return {"message": f"Dish '{dishe.name}' added to restaurant 'Paradise Hotel'"}


@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    print(f"File name: {file.filename}")
    print(f"File type: {file.content_type}")
    print(f"Size: {len(contents)} bytes")

    # with open(f"uploaded_{file.filename}", "wb") as f:
    #     f.write(contents)

    return {"filename": file.filename, "size": len(contents)}
