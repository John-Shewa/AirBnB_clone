#!/usr/bin/python3
from datetime import datetime
import uuid


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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns: the class name, id and __dict__ in string format

        """
        return "[{}] ({}) {})".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime.
        """
        now = datetime.datetime.now()
        self.updated_at = now.isoformat()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance

        """
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = value
        new_dict["__class__"] = type(self).__name__
        return new_dict
