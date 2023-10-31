#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """An empty class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize this class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets attribute: width

        Raises:
            TypeError: if width is not integer
            ValueError: if width value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets attribute: height

        Raises:
            TypeError: if width is not integer
            ValueError: if width value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area calculation of this rectangle using
        instance attributes: width and height
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter calculation of this rectangle using
        instance attributes: width and height
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Prints the rectangle using the # character"""
        if self.width == 0 or self.height == 0:
            return ("")

        rec_width = "#" * self.width
        rect = rec_width

        for x in range(self.height - 1):
            rect += "\n" + rec_width
        return (rect)
