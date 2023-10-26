#!/usr/bin/python3
"""A square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Initialize the new square
        Args:
            size: size of the new square
        Raises:
            TypeError: raised if size is not an int
            ValueError: raised if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Area of this square

            Returns: size of the square
            """

            return self.__size ** 2
