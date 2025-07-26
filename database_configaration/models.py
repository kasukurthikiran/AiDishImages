from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Dishes(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    restaurant_id: Optional[int] = Field(default=None, foreign_key="restaurant.id")

    restaurant: Optional["Restaurant"] = Relationship(back_populates="dishes")


class Restaurant(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    dishes: List[Dishes] = Relationship(back_populates="restaurant")
