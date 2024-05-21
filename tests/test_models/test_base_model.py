#!/usr/bin/python3
""" Unitests for base.py """



from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.testModel = BaseModel()

    def test_attributes(self):
        """ tests instantiation of BaseModel class """
        try:
            uuid_test = uuid.UUID(self.testModel.id, version=4)
        except ValueError:
            self.fail(f"{self.testModel.id}is an invalid uuid")
        self.assertIsInstance(self.testModel.created_at, datetime)
        self.assertIsInstance(self.testModel.updated_at, datetime)
        self.assertEqual(self.testModel.created_at, self.testModel.updated_at)
        self.assertIsInstance(self.testModel, BaseModel)
        self.assertIsInstance(self.testModel.id, str)

    def test_update_attribute_change(self):
        """ tests updated_at """
        initial = self.testModel.updated_at
        self.testModel.name = "test"
        self.assertNotEqual(self.testModel.updated_at, initial)
        self.assertGreater(self.testModel.updated_at, initial)

    def test_str_rep(self):
        """Test the string representation of a BaseModel instance."""
        expected_str = f"[BaseModel] ({self.testModel.id}) {self.testModel.__dict__}"
        self.assertEqual(str(self.testModel), expected_str)

    def test_save(self):
        """ tests public instant method save()"""
        initial_update = self.testModel.updated_at
        self.testModel.save()
        self.assertNotEqual(initial_update, self.testModel.updated_at)
        self.assertGreater(self.testModel.updated_at, initial_update)

    def test_to_dict(self):
        """ tests public instant method to_dict()"""
        dict_t = self.testModel.to_dict()
        self.assertEqual(dict_t['id'], self.testModel.id)
        self.assertEqual(dict_t['created_at'], \
                self.testModel.created_at.isoformat())
        self.assertEqual(dict_t['updated_at'], \
                self.testModel.updated_at.isoformat())
        self.assertEqual(dict_t['__class__'], type(self.testModel).__name__)
        
        
if __name__=='__main__':
    unittest.main()
