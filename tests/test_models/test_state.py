#!/usr/bin/python3
"""tests for the state model """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_State_inheritence(self):
        """Tests the inherits form BaseModel to State class"""
      
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """Tests State class contains attribute : name"""
      
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        """Tests state attribute type (name:str)"""
        
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
