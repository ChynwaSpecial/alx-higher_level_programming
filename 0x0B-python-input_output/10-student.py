#!/usr/bin/python3
"""Defines a class Student"""

class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student"""
          if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
    def __str__(self):
        """Return a string representation of a student instance"""
        return
    def __repr__(self):
        """Return a representation of a student instance for debugging"""
        return self.__str__()

