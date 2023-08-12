#!/usr/bin/python3
"""amenity testing """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ amenity class testing"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """name atribute (string) """
        new = self.value()
        self.assertEqual(type(new.name), str)
