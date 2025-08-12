import os
import time
from dotenv import load_dotenv
from .text_to_image import generate_image
from .insert_records import insert_records
from ..my_superbase_packages.upload_images import upload_images


def image_generation(items):
    load_dotenv()
    gen_image_workers = int(os.getenv("gen_image_workers"))
    image_prompt = os.getenv("image_prompt")
    start_time = time.time()
    images = generate_image(image_prompt, items, gen_image_workers)
    end_time = time.time()
    print("Image generation time:", end_time - start_time)
    insert_records(images)
    imagepaths = upload_images(images)
    return imagepaths
