#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Initializes instance attributes

         Args:
            *args: list of arguments
             **kwargs: dict of key-values arguments
        """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        me = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        me = self.value()
        copy = me.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is me)

    def test_kwargs_int(self):
        """ """
        me = self.value()
        copy = me.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        me = self.value()
        me.save()
        key = self.name + "." + me.id
        with open('file.json', 'r') as f:
            js = json.load(f)
            self.assertEqual(js[key], me.to_dict())

    def test_str(self):
        """ """
        me = self.value()
        self.assertEqual(str(me), '[{}] ({}) {}'.format(self.name, me.id,
                         me.__dict__))

    def test_todict(self):
        """ """
        me = self.value()
        ne = me.to_dict()
        self.assertEqual(me.to_dict(), ne)

    def test_kwargs_none(self):
        """ """
        nl= {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**nl)

    def test_kwargs_one(self):
        """ """
        nl = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**nl)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        nl = new.to_dict()
        new = BaseModel(**nl)
        self.assertFalse(new.created_at == new.updated_at)
