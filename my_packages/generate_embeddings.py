from .openai_client import openai_client
import os

from dotenv import load_dotenv

client = openai_client()

load_dotenv()

model = os.getenv("model")


def generate_embedding(text, model=model):
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding
