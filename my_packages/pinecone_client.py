import os
from dotenv import load_dotenv

load_dotenv()


def pinecone_client():
    pine_api_client = os.getenv("pinecone_api_key")
    return pine_api_client
