from .supabase_client import my_client
import os


def create_bucket():
    supabase = my_client()
    bucket_name = os.getenv("Bucket_Name")
    response = supabase.storage.create_bucket(
        bucket_name,
        options={
            "public": False,
            "allowed_mime_types": ["image/*"],
            "file_size_limit": 5 * 1024 * 1024,
        },
    )
    return response
