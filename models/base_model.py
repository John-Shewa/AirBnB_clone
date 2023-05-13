#!/usr/bin/python3
import datetime
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
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

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
        now = datetime.datetime.now()
        self.updated_at = now.isoformat()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance

        """
        return self.__dict__
