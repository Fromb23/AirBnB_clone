#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel

class ReviewTestCase(unittest.TestCase):
    def test_review_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_inheritance(self):
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

if __name__ == '__main__':
    unittest.main()
