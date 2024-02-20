#!/usr/bin/python3
"""
Module contains function that appends a
a string to file end
"""


def append_write(filename="", text=""):
    """
    appends a string to end of text file and
    returns number of characters written

    Args:
        filename (str): file name
            text (str): text to append to file
        Return: No. of written characters
    """
    with open(filename, "a", encoding="UTF-8") as fl:
        return (fl.write(text))
