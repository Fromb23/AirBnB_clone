#!/usr/bin/python3

import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import Filestorage


class TestBaseModel(unittest.TestCase):
    """Test cases for the 'BaseModel' class."""

    def setUp(self):
        pass

    def tearDown(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization_positive(self):
        """Test passing cases for `BaseModel` initialization."""
        #test with valid attributes
        b1 = BaseModel(id="12345", created_at="2024-01-01T12:00:00.00001",
                                    updated_at="2024-01-01T12:00:00.0001",
                                    name="TestModel", value=42)
        self.assertEqual(b1.id, "12345")
        self.assertEqual(b1.name, "TestModel")
        self.assertEqual(b1.value, 42)
        self.assertEqual(str(type(b1)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

        #test with explicit attributes
        b2 = BaseModel()
        self.assertIsInstance(b2.id, str)
        self.assertIsInstance(b2.created_at, datetime)
        self.assertIsInstance(b2.updated_at, datetime)

    def test_str(self):
        """Test method for `__str__` representation."""
        b1 = BaseModel(id="12345", name="TestModel", value = 42)
        string = f"[{type(b1).__name__}] (12345) {'{' + \"'name': 'TestModel',
        'value': 42}\" + '}'}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """Test method for `save`."""
        b = BaseModel()
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_save_storage(self):
        """Test that `stotage.save()` is called from `save`."""
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.isfile(file_path))
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
            self.assertEqual(len(file_content), len(json.dumps(d)))
            self.assertEqual(json.loads(file_content), d)

    def test_to_dict(self):
        """Test method for `to_dict`."""
        b1 = BaseModel(id="12345", name="TestModel", value=42)
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id', b1_dict.keys())
        self.assertIn('created_at', b1_dict.keys())
        self.assertIn('updated_at', b1_dict.keys())
        self.assertEqual(b1_dict['__class__'], type(b1).__name__)

        #check datetime conversion
        # Check datetime conversion
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)

    def test_dict_isinstance(self):
        """Test creating an instance from a dictionary."""
        dict_instance = {'name': 'Rombo', 'age': '22'}
        new_instance = BaseModel(**dict_instance)
        self.assertIsInstance(new_instance, BaseModel)
        self.assertEqual(new_instance.name, 'Rombo')
        self.assertEqual(new_instance.age, 22)

if __name__ == "__main__":
    unittest.main()
