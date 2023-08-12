#!/usr/bin/python3
""" testing place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """testing place class"""

    def __init__(self, *args, **kwargs):
       """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    """atributes tests"""

    def test_city_id(self):
        """ city id -> string"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ user id -> string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ name -> string """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """number of rooms -> intiger """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """number of bathrooms -> intiger """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """max number of guests ->intiger """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ night price -> intiger"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """latitude -> float """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ longitude -> float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """amenity id -> list """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
