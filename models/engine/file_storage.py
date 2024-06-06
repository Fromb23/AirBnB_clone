#!/usr/bin/python3

import json
import os

class FileStorage():
    def __init__(self):
        self.__file_path= 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        from models.base_model import BaseModel

        basemodel = BaseModel()
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    existing_data = json.load(file)
                except:
                    existing_data = {}
        else:
            existing_data = {}

        dict_obj = basemodel.to_dict()
        obj_id = dict_obj.get('id')
        if obj_id:
            existing_data[obj_id] = dict_obj
        existing_data.update(dict_obj)
        with open(self.__file_path, 'w') as file:
            json.dump(existing_data, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                print(self.__objects)
