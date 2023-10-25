#!/usr/bin/python3
"""A square module"""


class Square:
    """Define a square"""

    def __init__(self, size):
        """Initialize the new square
        Args:
            size: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns current area of the square"""
            return (self.__size * self.__size)
