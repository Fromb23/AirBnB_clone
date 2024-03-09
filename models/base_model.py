#!/usr/bin/python3

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage

class BaseModel:
    """
    Base class for other classes to inherit common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime): Timestamp representing creation time.
            updated_at (datetime): Timestamp representing the last update time.
        """

        self.id = kwargs.get("id", str(uuid.uuid4()))

        if "created_at" in kwargs:
            self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()

        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.updated_at = datetime.now()


        for key, value in kwargs.items():
            if key not in ["__class__", "id", "created_at", "updated_at"]:
                setattr(self, key, value)

        storage.new(self)


    def __str__(self):
        """
        Returns (str) string representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Saves the current instance to the storage.

        Updates the 'updated_at' attribute and calls the storage save method.
        """
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__

        # Convert datetime objects to ISO format strings
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy
