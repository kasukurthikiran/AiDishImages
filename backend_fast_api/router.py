from fastapi import APIRouter, UploadFile, File, Form, Query, BackgroundTasks
import base64
from pydantic import BaseModel
from sqlmodel import select
from contextlib import contextmanager
import uuid
from ..my_packages.dish_name_extraction import dish_name_extraction
from ..my_packages.filter_records import filter_records
from ..my_packages.image_generation import image_generation
from ..my_superbase_packages.fetch_images import fetch_images

from ..database_configaration.models import Dishes, Restaurant
from ..database_configaration.un_matched_records_table import UNMATCHEDRECORDS
from ..database_configaration.database_connection import get_session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from .background_task import generate_image

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@contextmanager
def get_db_session():
    yield from get_session()


class RestaurantDetails(BaseModel):
    name: str


@router.get("/dishes_by_r_id")
def get_dishes_by_restaurant(
    id: str = Query(...),
):
    with get_db_session() as session:
        stmt = (
            select(Dishes, Restaurant.name)
            .join(Restaurant, Dishes.restaurant_id == Restaurant.id)
            .where(Restaurant.id == id)
        )
        results = session.exec(stmt).all()

        response = []

        for dish, restaurant_name in results:
            dish_data = dish.model_dump()
            dish_data["restaurant_name"] = restaurant_name
            response.append(dish_data)

        t = fetch_images(response)

        signed_url_map = {item["image_path"]: item["signed_url"] for item in t}

        for dish in response:
            image_path = dish.get("image_path")
            if image_path in signed_url_map:
                dish["signed_url"] = signed_url_map[image_path]

    return {"dishes": response}


@router.post("/upload/")
async def upload_image(
    file: UploadFile = File(...),
    restaurant_name: str = Form(...),
):
    try:
        print("restaurant_name", restaurant_name)
        restaurant_data = RestaurantDetails(name=restaurant_name)

    except Exception as e:
        print(e, "Error while parsing restaurant data")
        return {"error": "Invalid restaurant data"}

    contents = await file.read()
    image_base64 = base64.b64encode(contents).decode("utf-8")

    dishes = dish_name_extraction(image_base64)
    print(dishes)
    r_id = str(uuid.uuid4())

    if dishes:
        matched_records, unmatched_records = filter_records(dishes)
        print("matched_records", matched_records)
        print("unmatched_records", unmatched_records)

        if matched_records:
            print("matched records")

            with get_db_session() as session:
                restaurant = Restaurant(id=r_id, name=restaurant_data.name)
                session.add(restaurant)
                session.commit()
                for i in matched_records:
                    dish = Dishes(
                        id=str(uuid.uuid4()),
                        name=i.get("dish"),
                        image_path=i.get("image_path"),
                        restaurant_id=r_id,
                    )
                    session.add(dish)
                session.commit()

        if unmatched_records:
            print("i am entered into unmatched_records")
            with get_db_session() as session:
                restaurant = Restaurant(id=r_id, name=restaurant_data.name)
                session.add(restaurant)
                session.commit()
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
    return {"restaurant_ids": r_id}


@router.get("/dishes_by_all_r_id")
def get_all_dishes():
    with get_db_session() as session:
        stmt = select(Dishes, Restaurant.name).join(
            Restaurant, Dishes.restaurant_id == Restaurant.id
        )
        results = session.exec(stmt).all()

        response = []

        for dish, restaurant_name in results:
            dish_data = dish.model_dump()
            dish_data["restaurant_name"] = restaurant_name
            response.append(dish_data)

        t = fetch_images(response)

        signed_url_map = {item["image_path"]: item["signed_url"] for item in t}

        for dish in response:
            image_path = dish.get("image_path")
            if image_path in signed_url_map:
                dish["signed_url"] = signed_url_map[image_path]

    return {"dishes": response}


@router.post("/uploads/")
async def upload_images(
    file: UploadFile = File(...),
    restaurant_name: str = Form(...),
):
    try:
        print("restaurant_name", restaurant_name)
        restaurant_data = RestaurantDetails(name=restaurant_name)
    except Exception as e:
        print(e, "Error while parsing restaurant data")
        return {"error": "Invalid restaurant data"}

    r_id = str(uuid.uuid4())

    with get_db_session() as session:
        restaurant = Restaurant(id=r_id, name=restaurant_data.name)
        session.add(restaurant)
        session.commit()

    contents = await file.read()
    image_base64 = base64.b64encode(contents).decode("utf-8")

    dishes = dish_name_extraction(image_base64)
    print(dishes)

    if dishes:
        matched_records, unmatched_records = filter_records(dishes)
        print("matched_records", matched_records)
        print("unmatched_records", unmatched_records)

        with get_db_session() as session:
            if matched_records:
                print("matched records")
                for i in matched_records:
                    dish = Dishes(
                        id=str(uuid.uuid4()),
                        name=i.get("dish"),
                        image_path=i.get("image_path"),
                        restaurant_id=r_id,
                    )
                    session.add(dish)

            if unmatched_records:
                print("entered unmatched_records")
                for i in unmatched_records:
                    dish_id = str(uuid.uuid4())
                    dish_unmatched_data = UNMATCHEDRECORDS(
                        id=dish_id, name=i, r_id=r_id
                    )
                    dish_data = Dishes(
                        id=dish_id,
                        name=i,
                        image_path="",
                        restaurant_id=r_id,
                    )
                    session.add(dish_unmatched_data)
                    session.add(dish_data)

            session.commit()

    return {"restaurant_ids": r_id}


@router.get("/restaurants_data")
def get_restaurant_data():
    with get_db_session() as session:
        statement = select(Restaurant)
        restaurants = session.exec(statement).all()
        restaurants_data = [{"id": i.id, "name": i.name} for i in restaurants]
        print(restaurants_data)

    return {"restaurants_data": restaurants_data}
