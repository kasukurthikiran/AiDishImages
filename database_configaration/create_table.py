from .database_connection import engine
from .models import SQLModel
# from .models import Dishes, Restaurant

from .user_models import User


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
