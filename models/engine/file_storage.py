#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import models

class FileStorage:
      """Represent an abstracted storage engine.

      Attributes:
             __file_path (str): The name of the file to save objects to.
             __objects (dict): A dictionary of instantiated objects.
      """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects the obj with key <obj class name>.id
        Aguments:
            obj : An instance object.
        """

         key = "{}.{}".format(type(obj).__name__, obj.id)
         FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects attribute to JSON file."""

        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

         with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
             json.dump(objects_dict, fd)


