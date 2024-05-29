#!/usr/bin/python3
"""
BaseModel class containing common attributes and methods for other classes.
"""

import uuid
import datetime


class BaseModel():
    """Base model class for other models."""
    def __init__(self):
        """Initialize BaseModel attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return string representation of BaseModel object."""
        self.id = uuid.uuid4()

        return f"[<{self.__class__.__name__}>] [<{self.id}>] <{self.__dict__}>"

    def save(self):
        """Update the updated_at attribute to the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel object."""
        dict_copy = self.__dict__.copy()

        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()

        return dict_copy