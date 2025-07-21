import os
from dotenv import load_dotenv
from .image_to_text import extract_text


def dish_name_extraction():
    load_dotenv()
    image_path = os.getenv("image_path")
    prompt = os.getenv("prompt")
    response = extract_text(image_path, prompt)
    content = response.choices[0].message.content
    dishes = [dish.strip() for dish in content.split(",") if dish.strip()]
    return dishes
