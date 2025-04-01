from bson import ObjectId

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Any


class Project(BaseModel):
    name: str
    data: Dict[str, Any]
    create_time: datetime = Field(default_factory=datetime.now(datetime.UTC))
    update_time: datetime = Field(default_factory=datetime.now(datetime.UTC))

    class Config:
        arbitrary_types_allowed = True
