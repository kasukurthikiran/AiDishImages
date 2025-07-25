# routers/items.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/items")
async def get_items():
    return {"message": "List of items"}


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@router.get("/items/popular")
async def get_popular_items():
    return {"message": "Popular items list"}


@router.get("/items/by-name/{name}")
async def get_item_by_name(name: str):
    return {"message": f"Item with name {name}"}
