#!/usr/bin/python3
# File storage module

""" Stores classe instances in a json file """

import os
import json


class FileStorage:
    """File storage class
        Args:
            __file_path(str): Path to json file
            __objects(dict): Dictionary to store objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __object"""
        return FileStorage.__objects

    def new(self, obj):
        """save new instances to __objects
           sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fileobj:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, fileobj)

    def project_classes(self):
        """ creates dictionary of local modules """

        from models.base_model import BaseModel
        classes = {
                "BaseModel": BaseModel
                }
        return classes

    def reload(self):
        """ deserializes the JSON file to __objects """
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fileobj:
            obj_dict = json.load(fileobj)
            obj_dict = {
                            k: self.project_classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()
                        }
            FileStorage.__objects = obj_dict
