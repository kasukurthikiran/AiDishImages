import os
import base64
import time
from dotenv import load_dotenv
from my_packages.text_to_image import generate_image


def image_generation(items):
    load_dotenv()
    # print("======> started the text_to_image")
    gen_image_workers = os.getenv("gen_image_workers")
    image_prompt = os.getenv("image_prompt")
    output_folder = os.getenv("output_folder")
    os.makedirs(output_folder, exist_ok=True)
    start_time = time.time()

    images = generate_image(image_prompt, items, gen_image_workers)

    end_time = time.time()
    print("Image generation time:", end_time - start_time)

    image_paths = []

    for image in images:
        try:
            dish_name = image["dish"]
            image_data = image["image_base64"]
            image_bytes = base64.b64decode(image_data)
            image_path = os.path.join(output_folder, f"{dish_name}.png")

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(f"{dish_name}.png")

        except Exception as e:
            print("Error saving image:", e)
    metadatas = [{"title": d, "image_path": i} for d, i in zip(dishes, image_paths)]
    return metadatas


# print(text_to_image(["tomato", "chicken 78"]))
