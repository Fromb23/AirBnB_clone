#!/usr/bin/python3

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest

class AmenityTestCase(unittest.TestCase):
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_inheritance(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

if __name__ == '__main__':
    unittest.main()
