#!/usr/bin/python3
"""
Module defines function that writes json obj to file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an Obj to txt file in Json format

    Args:
        my_obj (object): object to serialize
        filename (str): file name to write to
    """
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
