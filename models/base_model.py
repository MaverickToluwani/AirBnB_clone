#!/usr/bin/python3
# Base model definition

"""Base model for AirBnB project"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ base model for application"""
    def __init__(self, *args, **kwargs):
        """Initializing base model attributes
        Args:
            *args(tuple): n number of instance attrubtes
            **kwargs(dictionary): instance attributes with values
            id: Unique identifier for each instance
            created_at: Time when instance was created
            updated_at: time when instance is updated
        """
        if kwargs is not None and kwargs != {}:
            kwargs.pop("__class__")
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return f"[{(type(self)).__name__}] ({self.id}) {self.__dict__}"

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
        storage.save()

    def to_dict(self):
        """ returns dictionary containing all keys and values of __dict__"""
        t_dict = self.__dict__.copy()
        t_dict['__class__'] = type(self).__name__
        t_dict['created_at'] = self.created_at.isoformat()
        t_dict['updated_at'] = self.updated_at.isoformat()
        return t_dict
