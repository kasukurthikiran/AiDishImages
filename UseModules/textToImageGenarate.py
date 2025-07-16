import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_image(prompt: str, model: str, size: str, quality: str, dishes: list[str]) -> list[dict]:
    
    results = []

    for dish in dishes:
        response = client.images.generate(
            model=model,
            prompt=f"{prompt} - {dish}",
            size=size,
            quality=quality,
            n=1,
            response_format="b64_json"
        )

        base64_image = response.data[0].b64_json
        results.append({
            "dish": dish,
            "image_base64": base64_image
        })
    return results
