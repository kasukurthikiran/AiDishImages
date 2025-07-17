import os
import base64
import threading
import time
from queue import Queue

from UserModules.ImageToText import extract_text as textgen
from UserModules.textToImage import generate_image as imagegen

output_folder = "AiGenaratedImages"
os.makedirs(output_folder, exist_ok=True)


save_image_q = Queue()

def worker():
    while not save_image_q.empty():
        try:
            item = save_image_q .get() 
            dish_name = item["dish"]
            image_data = item["image_base64"]

            image_bytes = base64.b64decode(image_data)
            image_path = os.path.join(output_folder, f"{dish_name}.png")
            with open(image_path, "wb") as f:
                f.write(image_bytes)

            print(f"Saved: {image_path}")
            save_image_q .task_done()

        except Exception as e:
            print("Error in thread:", e)
            save_image_q .task_done()

try:
  
    image_path = "UserMenuImages/menu.jpg"
    prompt = "extract the dish names only with ,separation"
    response = textgen(image_path, prompt)
    content = response.choices[0].message.content
    dishes = [dish.strip() for dish in content.split(',') if dish.strip()]
    print("Dishes:", dishes)
    # dishes=["chicken","mutton"]
    gen_image_workers=5
    image_prompt = "Realistic top-view image served on a traditional Indian plate of"
    start_time = time.time()
    images = imagegen(image_prompt, dishes,gen_image_workers)
    end_time = time.time()
    print("Image generation time:", end_time - start_time)

    for item in images:
       save_image_q.put(item)

    threads = []
    num_threads = 4
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("All images saved.")

except Exception as e:
    print("Error:", e)
