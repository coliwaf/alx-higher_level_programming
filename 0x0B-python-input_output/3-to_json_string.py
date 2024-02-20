#!/usr/bin/python3
"""
Module defines a json-to-String method
"""
import json



def to_json_string(my_obj):
    """
    Returns a Json representation of an object
    """
    return (json.dumps(my_obj))
