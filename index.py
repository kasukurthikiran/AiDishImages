# main.py
from fastapi import FastAPI  # Import the router
from .backend_fast_api import items

from pydantic import BaseModel

app = FastAPI()

# Include the router
# app.include_router(items.router)
app.include_router(items.router)
