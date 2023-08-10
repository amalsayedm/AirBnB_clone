#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns official string representation"""
        cself = (str(type(self)).split('.')[-1]).split('\'')[0]
        return "[{}] ({}) {}".format(cself, self.id, self.__dict__)
        
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel class."""
        my_dct = {}
        my_dct.update(self.__dict__)
        my_dct.update({'__class__' :
                      (str(type(self)).split('.')[-1]).split('\'')[0]})
        my_dct['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        my_dct['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")

        return my_dct
