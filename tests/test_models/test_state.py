#!/usr/bin/python3
"""state testing """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """state class testing """

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """testing  name atribute (string) """
        new = self.value()
        self.assertEqual(type(new.name), str)
