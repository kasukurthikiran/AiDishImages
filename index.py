from fastapi import FastAPI
from .backend_fast_api import router
from fastapi.middleware.cors import CORSMiddleware

# from pydantic import BaseModel
from fastapi import APIRouter, UploadFile, File, Form
import base64

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/users")
def get_users():
    print("i am get users")
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]


list1 = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]


# @app.post("/upload/")
# async def upload_restaurant(
#     file: UploadFile = File(...),
#     restaurant_id: int = Form(...),
#     restaurant_name: str = Form(...),
# ):
# # Example: just return the name back
# return {"details": list1}


app.include_router(router.router)
