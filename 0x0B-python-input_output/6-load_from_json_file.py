#!/usr/bin/python3
"""
Module defines function that reads json frm file
"""
import json


def load_from_json_file(filename):
    """
    Function creates a Python Obj from json txt file

    Args:
        filename (str): file name to write to
    """
    with open(filename, "r") as fl:
        myObj = json.load(fl)
        return (myObj)
