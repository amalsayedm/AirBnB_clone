#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        with open(FileStorage.__file_path, 'w', encoding="UTF8") as obj_f:
            obj_dict = {}
            obj_dict.update(FileStorage.__objects)
            for key, val in obj_dict.items():
                obj_dict[key] = val.to_dict()
            json.dump(obj_dict, obj_f)

    def reload(self):
        """reload objects from files(models folder)"""
        
        classes_list = {"BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review}
        try:
            obj_dict = {}
            with open(FileStorage.__file_pat.,'r', encoding="utf-8") as obj_f:
                obj_dict = json.load(obj_f)
               for key, val in obj_dict.items():
                   self.all()[key] = classes_list[val['__class__']](**val)
        except FileNotFoundError:
            pass
