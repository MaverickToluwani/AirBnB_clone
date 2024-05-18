#!/usr/bin/python3
"""Base model for AirBnB project"""

from datetime import datetime
import uuid


class BaseModel:
    """ base model for application"""
    def __init__(self):
        """Initializing base model attributes
        Args:
            id: Unique identifier for each instance
            created_at: Time when instance was created
            updated_at: time when instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __setattr__(self, key, value):
        """Overides the default setattr method such that
        when a new attribute is added self.updated_at is
        updated"""
        if key != 'updated_at':
            self.__dict__[key] = value
            self.__dict__['updated_at'] = datetime.now()
        else:
            super().__setattr__(key, value)

    def save(self):
        """ updates the value of self.updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Alters instance dictionary """
        if "__class__" not in self.__dict__:
            self.__dict__['__class__'] = type(self).__name__
            self.__dict__['created_at'] = datetime.isoformat(self.created_at)
            self.__dict__['updated_at'] = datetime.isoformat(self.updated_at)
            return self.__dict__
        else:
            return self.__dict__

    def __str__(self):
        return f"[{(type(self)).__name__}] ({self.id}) {self.__dict__}"
