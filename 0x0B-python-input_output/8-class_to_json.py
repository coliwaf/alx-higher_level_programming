#!/usr/bin/python3
"""
Module defines a Python class to Json function
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    for json serialization of object
    """

    return obj.__dict__
