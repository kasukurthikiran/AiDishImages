import base64

from .openai_client import openai_client


client = openai_client()


def extract_text(image_path: str, prompt: str):
    base64_image = image_path

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        max_tokens=1024,
    )

    return response
