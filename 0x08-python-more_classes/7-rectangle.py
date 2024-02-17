#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """An empty class that represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize class
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves attribute - width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets attribute - width

        Raises:
            TypeError: if width is not integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves attribute - height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets attribute - height

        Raises:
            TypeError: if height is not integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle by calculating
        instance attributes: width and height
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of the rectangle by calculating using
        instance attributes: width and height
        """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Prints rectangle using the # character"""
        if self.width == 0 or self.height == 0:
            return ("")

        rec_width = ("{}".format(self.print_symbol)) * self.width
        rect = rec_width

        for x in range(self.height - 1):
            rect += "\n" + rec_width
        return (rect)

    def __repr__(self):
        """Recreates a new instance using eval() and returns
        a string representation of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Called when an instance of class rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
