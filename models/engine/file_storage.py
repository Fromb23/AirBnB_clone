#!/usr/bin/python3

import json
import os

class FileStorage:
    """
    A class for handling storage and retrieval of objects in a JSON file.
    """


    def __init__(self):
        """
        Initializes File storage with a default file path and an empty
        objects dictionary.
        """
        self.__file_path = "/root/AirBnB_clone/file.json"
        self.__objects = {}  # Initialize objects dictionary

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
        self.__objects[key] = obj  # Add object to dictionary


    def save(self):
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        """
        Saves the objects dictionary to a JSON file.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Split self.__file_path at the last slash (/) to get the directory
            directory = os.path.dirname(self.__file_path)

            # If the directory doesn't exist, create it
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(self.__file_path, 'w') as file:
                # Convert objects dictionary to JSON string
                instances = [
                        User().to_dict_user(),
                        City().to_dict_city(),
                        Amenity().to_dict_amenity(),
                        Place().to_dict_place(),
                        Review().to_dict_review(),
                        State().to_dict_state()
                        ]
                json_string = json.dumps(instances)
                # Write JSON string to file at file path
                file.write(json_string)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False

    def reload(self):
        """
        Reloads objects from a JSON file into the objects dictionary.

        Returns:
            bool: True if successful, False otherwise.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    data = file.read()
                    objects_data = json.loads(data)
                    for obj_data in objects_data:
                        class_name = obj_data['__class__']
                        if class_name == 'User':
                            obj = User(**obj_data)
                        elif class_name == 'City':
                            obj = City(**obj_data)
                        elif class_name == 'Amenity':
                            obj = Amenity(**obj_data)
                        elif class_name == 'Review':
                            obj = Review(**obj_data)
                        elif class_name == 'State':
                            obj = State(**obj_data)
                        else:
                            obj = BaseModel(**obj_data)
                        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
                return True
            except Exception as e:
                print(f"Error reloading file: {e}")
                return False
