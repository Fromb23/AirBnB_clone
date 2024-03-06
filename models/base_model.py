#!/usr/bin/python3

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()

        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key not in ["__class__", "created_at", "updated_at"]:
                setattr(self, key, value)

        if not kwargs:
            storage.new(self)


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__

        # Convert datetime objects to ISO format strings
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()

        return dict_copy

# Assume dict_instance is a dictionary representation of an instance
dict_instance = {'name' : 'Rombo', 'age' : 22}
new_instance = BaseModel(**dict_instance)
