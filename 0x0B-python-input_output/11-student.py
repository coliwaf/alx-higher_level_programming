#!/usr/bin/python3
"""
Module defines a Student class
"""


class Student:
    """
    Define a student
    Attributes:
        first_name (str): student's first name
        last_name (str): students's last name
        age (int): student's age
    Methods:
        __init__ - Initializes a new Student instance
        to_json - retrieves Student dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        retrieves a Student dictionary representation
        Args:
            attr (list): list of attribure names to be retrieved
        """

        if type(attr) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all Student instance attributes
        """
        for k, v in json.items():
            self.__dict__[k] = v
