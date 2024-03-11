import unittest
import os
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Setup method to initialize FileStorage instance before each test.
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        Teardown method to clean up after each test.
        """
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all(self):
        """
        Test the 'all' method of FileStorage.
        """
        # Test if all method returns a dictionary
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        """
        Test the 'new' method of FileStorage.
        """
        # Mock object
        class TestObject:
            def __init__(self, id):
                self.id = id

            def to_dict(self):
                return {'id': self.id}

        # Create a new object
        test_obj = TestObject(id='test_id')
        self.file_storage.new(test_obj)

        # Test if the object has been added to the dictionary
        self.assertIn('TestObject.test_id', self.file_storage.all())

    def test_save_reload(self):
        """
        Test the 'save' and 'reload' methods of FileStorage.
        """
        # Mock object
        class TestObject:
            def __init__(self, id):
                self.id = id

            def to_dict(self):
                return {'id': self.id}

        # Create a new object
        test_obj = TestObject(id='test_id')
        self.file_storage.new(test_obj)

        # Save objects to file
        self.file_storage.save()

        # Create a new FileStorage instance
        new_file_storage = FileStorage()

        # Reload objects from file
        new_file_storage.reload()

        # Test if the reloaded object exists in the new instance
        self.assertIn('TestObject.test_id', new_file_storage.all())


if __name__ == '__main__':
    unittest.main()
