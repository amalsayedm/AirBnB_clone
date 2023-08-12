#!/usr/bin/python3
"""testing user"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ class teting user """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    """attributes testing """
    def test_first_name(self):
        """first name -> string """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """last name -> string """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """E mail -> string """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ password -> string """
        new = self.value()
        self.assertEqual(type(new.password), str)
