#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
from models.city import City

class CityTestCase(unittest.TestCase):
    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_inheritance(self):
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

if __name__ == '__main__':
    unittest.main()
