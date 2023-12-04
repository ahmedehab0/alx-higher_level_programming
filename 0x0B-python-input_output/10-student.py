#!/usr/bin/python3

"""defines a class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """method to initialize public instances
        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
