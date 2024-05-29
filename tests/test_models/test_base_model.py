#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    basemodel = BaseModel()
    
    @staticmethod
    def validate_uuid(uuid_string):
        try:
            uuid.UUID(uuid_string)
            return True
        except ValueError:
            return False

    def test_init(self):
        self.assertIsInstance(TestBaseModel.basemodel.id, str)
        self.assertIsInstance(TestBaseModel.basemodel.updated_at, datetime)
        self.assertIsInstance(TestBaseModel.basemodel.created_at, datetime)
        self.assertTrue(TestBaseModel.validate_uuid(TestBaseModel.basemodel.id))


if '__name__' == '__main__':
    unittest.main()
