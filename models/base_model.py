#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
   
    created_at = datetime.isoformat()
    updated_at = datetime.isoformat()

    def __str__(self):
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"