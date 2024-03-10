#!/usr/bin/python3

import unnitest
import os
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        p = Place()
        p3 = Place("hello", "wait", "in")
        key = f"{type(p).__name__}.{p.id}"
        self.assertIsInstance(p.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(p3.name, "")
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.amenity_ids, list)

    def test_init(self):
        p = Place()
        p2 = Place(**p.to_dict())
        self.assertIsInstance(p.id, str)
        self.assertIsInstance(p.created_at, datetime)
        self.assertIsInstance(p.updated_at, datetime)
        self.assertEqual(p.updated_at, p2.updated_at)

    def test_str(self):
        p = Place()
        string = f"[{type(p).__name__}] ({p.id}) {p.__dict__}"
        self.assertEqual(p.__str__(), string)

    def test_save(self):
        p = Place()
        old_update = p.updated_at
        p.save()
        self.assertNotEqual(p.updated_at, old_update)

     def test_todict(self):
        p = Place()
        p2 = Place(**p.to_dict())
        a_dict = p2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(p2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(p, p2)


if __name__= "__main__":
    unittest.main()
