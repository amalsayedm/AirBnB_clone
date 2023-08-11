#!/usr/bin/python3
"""review testuing """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """review testing class """

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """testing place id (string)"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """testing user id (string) """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """testing new inputs (string) """
        new = self.value()
        self.assertEqual(type(new.text), str)
