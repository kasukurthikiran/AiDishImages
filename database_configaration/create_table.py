from .database_connection import engine
from .models import SQLModel
from .models import Dishes, Restaurant


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
