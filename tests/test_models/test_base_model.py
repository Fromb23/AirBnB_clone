#!/usr/bin/python3

import uuid
import datetime
import unittest
from models.base_model import BaseModel

class testBaseModel(unittest.TestCase):
    def setUp(self):
       self._basemodel = BaseModel()
    def test_id_uuid(self):
        try:
            uuid.UUID(self._basemodel.id)
        except ValueError:
            self.fail("_basemodel.id is not a valid UUID")

    def test_created_at_datetime(self):
        self.assertIsInstance(self._basemodel.created_at, datetime.datetime)
    def test_created_at_is_recent(self):
        now = datetime.datetime.now()
        # Allow for a small amount of time difference
        self.assertAlmostEqual(self._basemodel.created_at.timestamp(), now.timestamp(), delta=1)

    def test_updated_at_datetime(self):
        self.assertIsInstance(self._basemodel.updated_at, datetime.datetime)
    def test_updated_at_is_recent(self):
        now = datetime.datetime.now()
        # Allow for a small amount of tim difference
        self.assertAlmostEqual(self._basemodel.updated_at.timestamp(), now.timestamp(), delta=1)

    def test_str(self):
    def test_save(self):
