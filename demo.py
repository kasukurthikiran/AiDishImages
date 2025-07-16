import os
import base64
from openai import OpenAI
from dotenv import load_dotenv 


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


with open("menu.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')


response = client.chat.completions.create(
    model="gpt-4.1",  
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "extract the dish names only with ,separation "},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }
    ],
    max_tokens=1024 
)


print("Extracted Text:")

print(response)
print(response.choices[0].message.content)

list1=response.choices[0].message.content.split()
print(list1)
for dish in list1:
    print(f" Generating image for: {dish}...")

    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Realistic top-view image of {dish} served on a traditional Indian plate",
        size="1024x1024",
        quality="standard",
        n=1,
        response_format="b64_json"
    )

    image_base64 = response.data[0].b64_json

   
    image_data = base64.b64decode(image_base64)
    filename = f"{dish.replace(' ', '_')}.png"
    with open(filename, "wb") as f:
        f.write(image_data)

    print(f"Saved: {filename}")

print("\n All images generated and saved successfully!")
