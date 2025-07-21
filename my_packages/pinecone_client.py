import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()


def pinecone_client():
    pine_api = os.getenv("pinecone_api_key")
    pine_api_client = Pinecone(pine_api)
    return pine_api_client
