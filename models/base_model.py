#!/usr/bin/python3
from datetime import datetime
import uuid


class BaseModel:
    """
    A class that defines all common attributes/methods for
    other classes.

    """
    id: str
    created_at = datetime
    updated_at = datetime

    def __init__(self):
        """
        Initializes the BaseModel

        Args:
            id: gives a unique id to instances
            created_at: assigns the current time to instances
            updated_at: assigns an updated time to instances
        Returns: None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """
        Returns: the class name, id and __dict__ in string format

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime.
        """
        self.update_updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance

        """
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_[created_at].isoformat()
        dict_["updated_at"] = dict_[updated_at].isoformat()
        return dict_
