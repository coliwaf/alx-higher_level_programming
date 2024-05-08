#!/usr/bin/python3
"""
Module that has function that prints a
file to stdout without import
"""


def read_file(filename=""):
    """
    Reads a file and prints it out to STDOUT
    """
    with open(filename, "r", encoding="UTF-8") as fl:
        for line in fl:
            print(line, end="")
