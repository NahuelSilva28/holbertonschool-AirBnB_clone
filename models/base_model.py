"#!/usr/bin/python3"
import uuid
import datetime
"""Base model class"""


class BaseModel():
    """BseModel with the principal function to inherit"""
    def __init__(self, id=uuid.uuid4(), created_at=None, updated_at=None):
        """the constructor of base"""
        self.id = str(id)

        timeFormat = datetime.datetime.now()
        self.created_at = timeFormat
        timeFormat = datetime.datetime.now()
        self.updated_at = timeFormat

    def save(self):
        """saves a new version of class"""
        timeFormat = datetime.datetime.now()
        self.updated_at = timeFormat

    def __str__(self):
        """str version to print"""
        txt = "[{}] (<{}>) <{}>"
        return txt.format(BaseModel.__name__, self.id, self.__dict__)

    def to_dict(self):
        """To_dict function to have a dictionary version of data"""
        dictio = {}

        dictio.update({"created_at": self.created_at.isoformat()})
        dictio.update({"updated_at": self.updated_at.isoformat()})
        for item in self.__dict__.items():
            dictio[item[0]] = item[1]

        return dictio
