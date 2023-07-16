#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes FileStroage.__objects
        """
        new_dict = {}
        for key, value in self.__objects.items():
            if isinstance(value, BaseModel):
                new_dict[key] = value.to_dict()
            else:
                new_dict[key] = value
        with open(self.__file_path, 'w+', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes instances got from json file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                deserialized = json.load(f)
                for key, value in deserialized.items():
                    class_name = value.get('__class__')
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        from models.user import User  # Avoid circular import
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
