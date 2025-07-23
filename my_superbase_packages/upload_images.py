from .supabase_client import my_client
import os
import base64


def upload_images(images):
    image_paths = []
    supabase = my_client()
    bucket_name = os.getenv("Bucket_Name")
    folder_name = os.getenv("folder_path")

    for image in images:
        print(image.get("id"))
        try:
            image_base64 = image.get("image_base64")
            dish_name = image.get("id")

            image_bytes = base64.b64decode(image_base64)
            image_path = f"{folder_name}/{dish_name}.png"
            image_paths.append({"image_path": f"{dish_name}.png"})

            response = supabase.storage.from_(bucket_name).upload(
                path=image_path,
                file=image_bytes,
                file_options={
                    "content-type": "image/png",
                    "cache-control": "3600",
                    "upsert": "false",
                },
            )

            print(f"Uploaded {dish_name}: {response}")
        except Exception as e:
            print(f"Failed to upload image for {image.get('dish')}: {e}")

    return image_paths
