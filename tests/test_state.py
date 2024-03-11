#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
from models.state import State

class StateTestCase(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_inheritance(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

if __name__ == '__main__':
    unittest.main()
