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

    def to_json(self):
        """
        retrieves a Student dictionary representation
        """
        return self.__dict__
