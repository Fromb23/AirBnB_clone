#!/usr/bin/python3

import json
import os


class FileStorage:
    """
    A class for handling storage and retrieval of objects in a JSON file.
    """

    __file_path = "/root/AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.
        """
        return self.__objects  # Return objects dictionary

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to be added to the storage dictionary.
        """
        key = obj.__class__.__name__ + "." + obj.id  # Create key
        self.__objects[key] = obj.to_dict()  # object instance

    def save(self):
        """
        Saves the objects dictionary to a JSON file.
        """
        with open(self.__file_path, 'w') as file:
            json_string = json.dumps(self.__objects)
            file.write(json_string)

    def reload(self):
        """
        Reloads objects from a JSON file into the objects dictionary.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = file.read()
                objects_data = json.loads(data)
                self.__objects = objects_data
