#!/usr/bin/python
# initializes a package

""" creates a Filestorage instance"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
