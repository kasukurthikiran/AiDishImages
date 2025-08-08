from sqlmodel import SQLModel, Field
import uuid
from typing import Optional, List


class UNMATCHEDRECORDS(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: Optional[str]
    r_id: Optional[str]
