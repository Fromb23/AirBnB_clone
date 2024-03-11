#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
from models.user import User

class UserTestCase(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_inheritance(self):
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

if __name__ == '__main__':
    unittest.main()
