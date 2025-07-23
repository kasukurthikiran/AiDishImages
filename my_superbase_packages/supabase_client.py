from supabase import create_client
import os

from dotenv import load_dotenv


def my_client():
    load_dotenv()
    url = os.getenv("supabase_url")
    key = os.getenv("supabase_apikey")
    supabase_cleint = create_client(url, key)
    return supabase_cleint
