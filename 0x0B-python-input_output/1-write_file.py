#!/usr/bin/python3
"""
Module contains function that writes a
string to text file
"""


def write_file(filename="", text=""):
    """
    writes a string to text file and
    returns number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as fl:
        return (fl.write(text))
