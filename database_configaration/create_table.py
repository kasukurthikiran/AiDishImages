# create_db.py
from .database_connection import engine
from .models import SQLModel  # This will include all models

from .models import Dishes, Restaurant  # Import your models


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
