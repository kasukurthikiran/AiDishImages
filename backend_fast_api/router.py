from fastapi import APIRouter, UploadFile, File, Form
import base64
from pydantic import BaseModel
from sqlmodel import select
from contextlib import contextmanager

from ..my_packages.dish_name_extraction import dish_name_extraction
from ..my_packages.filter_records import filter_records
from ..my_packages.image_generation import image_generation
from ..my_superbase_packages.fetch_images import fetch_images

from ..database_configaration.models import Dishes, Restaurant
from ..database_configaration.database_connection import get_session

router = APIRouter()


@contextmanager
def get_db_session():
    yield from get_session()


class RestaurantDetails(BaseModel):
    id: str
    name: str


@router.post("/upload/")
async def upload_image(
    file: UploadFile = File(...),
    restaurant_id: str = Form(...),
    restaurant_name: str = Form(...),
):
    try:
        restaurant_data = RestaurantDetails(id=restaurant_id, name=restaurant_name)
        print(restaurant_data.id)
    except Exception as e:
        print(e, "Error while parsing restaurant data")
        return {"error": "Invalid restaurant data"}

    contents = await file.read()
    image_base64 = base64.b64encode(contents).decode("utf-8")

    dishes = dish_name_extraction(image_base64)
    print(dishes)
    matched_records_data = []

    if dishes:
        matched_records, unmatched_records = filter_records(dishes)
        print("matched_records", matched_records)
        print("unmatched_records", unmatched_records)
        # Process matched records
        if matched_records:
            with get_db_session() as session:
                for i in matched_records:
                    statement = select(Dishes).where(Dishes.id == i.get("id"))
                    print(statement)
                    dish = session.exec(statement).first()
                    print(dish)
                    if dish:
                        matched_records_data.append(
                            {
                                "id": dish.id,
                                "name": dish.name,
                                "price": dish.price,
                                "restaurant_id": dish.restaurant_id,
                                "image_path": dish.image_path,
                            }
                        )

        # Process unmatched records
        if unmatched_records:
            print("i am entered into unmatched_records")
            with get_db_session() as session:
                # Check if restaurant already exists
                statement = select(Restaurant).where(
                    Restaurant.id == restaurant_data.id
                )
                existing_restaurant = session.exec(statement).first()
                if not existing_restaurant:
                    restaurant = Restaurant(
                        id=restaurant_data.id, name=restaurant_data.name
                    )
                    session.add(restaurant)
                    session.commit()
                else:
                    restaurant = existing_restaurant

                temp_paths = image_generation(unmatched_records)

                for i in temp_paths:
                    dish = Dishes(
                        id=i.get("id"),
                        name=i.get("name"),
                        image_path=i.get("image_path"),
                        restaurant_id=restaurant.id,
                    )
                    print(dish)
                    session.add(dish)
                session.commit()

    # Combine and fetch image URLs
    if unmatched_records and matched_records:
        result = matched_records_data + temp_paths
        t = fetch_images(result)
    elif unmatched_records:
        t = fetch_images(temp_paths)
    elif matched_records:
        t = fetch_images(matched_records_data)

    return {"details": t}
