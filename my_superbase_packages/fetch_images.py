from .supabase_client import my_client
import os
from dotenv import load_dotenv


def fetch_images(images):
    load_dotenv()
    image_urls = []
    supabase = my_client()

    bucket_name = os.getenv("Bucket_Name")
    folder_name = os.getenv("folder_path")

    if not bucket_name or not folder_name:
        print("Missing environment variables: 'Bucket_Name' or 'folder_path'")
        return

    for image in images:
        try:
            full_path = f"{folder_name}/{image.get('image_path')}"
            response = supabase.storage.from_(bucket_name).create_signed_url(
                full_path,
                expires_in=3600,
            )

            signed_url = response.get("signedURL") or response.get("signed_url")
            if signed_url:
                image_urls.append({"signed_url": signed_url})
            else:
                print(f"Failed to generate URL for {image}: {response}")
        except Exception as e:
            print(f"Error generating signed URL for {image}: {e}")

    return image_urls
