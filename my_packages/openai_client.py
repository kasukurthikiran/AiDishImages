import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


def openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)
