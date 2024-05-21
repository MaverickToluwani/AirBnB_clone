#!/usr/bin/python3
# FileStorage test module

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

""" unittest module for FileStorage class"""

class TestFileStorage(unittest.Testcase):

    """ unit tests for FileStorage class """

    def setUp(self):
        """set up for the tests """
        self.storage = FileStorage()
        self.testModel = BaseModel()
        self.file_path = "file.json"
        self.storage._FileStorage__file_path = self.file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test for the public instance method all"""
        self.assertEqual(self.storage.all(). {})
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ for the public instance method new"""
        self.storage.new(self.testModel)
        key = f"BaseModel.{self.testModel.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], model)

    def test_save(self):
        """ for the public instance method save"""
         model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        self.assertGreatere(os.path.exists(self.file_path))
