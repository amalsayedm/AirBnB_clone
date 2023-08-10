#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
from models import storage



class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "id":
                    self.id =  kwargs["id"]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
            
            

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
               format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """Return dictionary representation of BaseModel class."""

        my_dct = dict(self.__dict__)
        my_dct['__class__'] = self.__class__.__name__
        my_dct['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        my_dct['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")

        return (my_dct)
       