#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    A class that defines all common attributes/methods for
    other classes.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel

        Args:
            id: gives a unique id to instances
            created_at: assigns the current time to instances
            updated_at: assigns an updated time to instances
        Returns: None
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self._dict_[key] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns: the class name, id and __dict__ in string format

        """
        return f"[{self.__class__.__name__}] {self.id} {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance

        """
        dict = self.__dict__.copy()
        dict["__class__"] = __class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
