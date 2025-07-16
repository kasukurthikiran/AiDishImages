from UserModules.ImageToText import extract_text as textgen

from UserModules.textToImage import generate_image as imagegen
import os
import base64

try:

  image_path = "UserMenuImages/menu.jpg"
  
  prompt="extract the dish names only with ,separation"

  response=textgen(image_path,prompt)


  print(response)
  content=response.choices[0].message.content
  print(content)
  print()
  list1=response.choices[0].message.content.split()
  print(list1)
  
  image_prompt = "Realistic top-view image served on a traditional Indian plate of"
  dishes=list1
  images = imagegen(image_prompt,dishes)
  output_folder = "AiGenaratedImages"
  os.makedirs(output_folder, exist_ok=True)

  for item in images:
    dish_name = item["dish"].replace(" ", "_")  
    image_data = item["image_base64"]
    
   
    image_bytes = base64.b64decode(image_data)
    
   
    image_path = os.path.join(output_folder, f"{dish_name}.png")
    with open(image_path, "wb") as f:
        f.write(image_bytes)
    print(f"Saved: {image_path}")


except Exception as e:
  print("i am error")
  print(e)



