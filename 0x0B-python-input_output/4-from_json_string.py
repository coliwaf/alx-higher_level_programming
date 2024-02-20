#!/usr/bin/python3
"""
Module defines a json-to-object method
"""
import json


def from_json_string(my_str):
    """
    Returns a Python Obj of a Json string
    """
    return (json.loads(my_str))
