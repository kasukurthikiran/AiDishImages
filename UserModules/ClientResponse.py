import os
from openai import OpenAI
from dotenv import load_dotenv



load_dotenv()   #loading dotenv file

def client_response():
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)