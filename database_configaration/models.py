from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
import uuid


class Dishes(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    restaurant_id: Optional[str] = Field(default=None, foreign_key="restaurant.id")
    price: int = Field(default=0)
    image_path: Optional[str]
    restaurant: Optional["Restaurant"] = Relationship(back_populates="dishes")


class Restaurant(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    dishes: List[Dishes] = Relationship(back_populates="restaurant")


class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password: str
