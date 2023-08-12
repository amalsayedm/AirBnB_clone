#!/usr/bin/python3
""" testing city"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """tetsing class city """

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """testing state id (string) """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """testing name (string) """
        new = self.value()
        self.assertEqual(type(new.name), str)
