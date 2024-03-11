#!/usr/bin/python3

import unittest
from unittest.mock import patch
import os
import json
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the 'BaseModel' class."""

    def test_init(self):
        """Test the initialization of BaseModel without arguments."""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_args(self):
        """Test the initialization of BaseModel with arguments."""
        obj = BaseModel(id="123", created_at="2022-01-01T12:00:00.000000", name="test")
        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.name, "test")
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel."""
        obj = BaseModel(id="123", created_at="2022-01-01T12:00:00.000000", name="test")
        expected_str = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        instance = BaseModel()
        instance.created_at = datetime(2024, 3, 11, 12, 0, 0)
        instance.updated_at = datetime(2024, 3, 12, 12, 0, 0)

        result = instance.to_dict()

        self.assertIsInstance(result, dict)
        self.assertIn('__class__', result)
        self.assertEqual(result['__class__'], 'BaseModel')
        self.assertIn('created_at', result)
        self.assertEqual(result['created_at'], '2024-03-11T12:00:00')
        self.assertIn('updated_at', result)
        self.assertEqual(result['updated_at'], '2024-03-12T12:00:00')

if __name__ == '__main__':
    unittest.main()
