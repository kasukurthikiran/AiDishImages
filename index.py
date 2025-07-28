from fastapi import FastAPI
from .backend_fast_api import router

# from pydantic import BaseModel

app = FastAPI()


app.include_router(router.router)
