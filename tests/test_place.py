#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place

class PlaceTestCase(unittest.TestCase):
    def test_place_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_place_inheritance(self):
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

if __name__ == '__main__':
    unittest.main()
