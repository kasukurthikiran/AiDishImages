from sqlmodel import select
from ..my_packages.openai_client import openai_client

from contextlib import contextmanager
from ..database_configaration.models import Dishes, Restaurant
from ..database_configaration.un_matched_records_table import UNMATCHEDRECORDS
from ..database_configaration.database_connection import get_session
import os

from dotenv import load_dotenv
import asyncio
from ..my_packages.get_db_table import get_db_table
from ..my_packages.pinecone_client import pinecone_client
from ..my_packages.generate_embeddings import generate_embedding
from ..my_superbase_packages.supabase_client import my_client

import base64


client = openai_client()

load_dotenv()


@contextmanager
def get_db_session():
    yield from get_session()


async def generate_image(workers: int):
    with get_db_session() as session:
        statement = select(UNMATCHEDRECORDS)
        raw_dishes = session.exec(statement).all()
        supabase = my_client()
        bucket_name = os.getenv("Bucket_Name")
        folder_name = os.getenv("folder_path")
        dishes = [{"id": i.id, "name": i.name, "r_id": i.r_id} for i in raw_dishes]
        if dishes:
            image_prompt = os.getenv("image_prompt")
            sem = asyncio.Semaphore(workers)
            db, table = get_db_table()
            pc = pinecone_client()
            index = pc.Index(db)

            def worker(dish):
                try:
                    dish_name = dish.get("name")
                    print(f"🔄 Generating image for: {dish_name}")
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=f"{image_prompt} - {dish_name}",
                        size="1024x1024",
                        quality="standard",
                        n=1,
                        response_format="b64_json",
                    )
                    base64_image = response.data[0].b64_json
                    print(f"Image generated for: {dish_name}")
                    if not base64_image:
                        print("image is not generated")
                        return
                    if base64_image:
                        print("base image created success")
                        vectors = []
                        vector = generate_embedding(dish_name)
                        record = {
                            "id": dish.get("id"),
                            "values": vector,
                            "metadata": {
                                "title": dish_name,
                                "image_path": f"{dish.get('id')}.png",
                            },
                        }
                        vectors.append(record)

                        inserted_image = index.upsert(vectors=vectors, namespace=table)
                        print("inserted_image", inserted_image)
                        # supabase

                        dish_id = dish.get("id")

                        image_bytes = base64.b64decode(base64_image)
                        image_path = f"{folder_name}/{dish_id}.png"
                        response = supabase.storage.from_(bucket_name).upload(
                            path=image_path,
                            file=image_bytes,
                            file_options={
                                "content-type": "image/png",
                                "cache-control": "3600",
                                "upsert": "true",
                            },
                        )
                        print("storage response", response)

                        # database
                        print("🛠️ Inserting into Dishes table...")
                        # dish_record = Dishes(
                        #     id=dish_id,
                        #     name=dish_name,
                        #     image_path=f"{dish_id}.png",
                        #     restaurant_id=dish.get("r_id"),
                        # )
                        # session.add(dish_record)
                        # session.commit()
                        # print(" Dish inserted into RDBMS")

                        statement = select(Dishes).where(Dishes.id == dish_id)
                        result = session.exec(statement).first()
                        if result:
                            result.image_path = f"{dish_id}.png"
                            session.add(result)
                            session.commit()
                            session.refresh(result)
                            print("Dish updated into RDBMS ============>")

                        statement = select(UNMATCHEDRECORDS).where(
                            UNMATCHEDRECORDS.id == dish_id
                        )
                        unmatched_dish = session.exec(statement).first()
                        if unmatched_dish:
                            session.delete(unmatched_dish)
                            session.commit()
                            print(" ===>Deleted unmatched record:", dish_id)

                except Exception as e:
                    print("Error in worker:", e)

    async def run_with_semaphore(dish):
        async with sem:
            await asyncio.to_thread(worker, dish)

    async def main():
        tasks = [run_with_semaphore(dish) for dish in dishes]
        await asyncio.gather(*tasks)

    await main()
