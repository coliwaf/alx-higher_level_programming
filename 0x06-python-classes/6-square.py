#!/usr/bin/python3
"""A square module"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the new square
        Args:
            size: size of the new square
            position: position of the new square
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ Size of the square lengthwise
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Raises:
            TypeError: raised if size is not an integer
            ValueError: raised if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """The position property for this square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of this square

        Returns: size of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Public instace that prints this square
        using the # char
        """

        for i in range(self.position[1]):
            print("")

        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for k in range(self.size):
                print("#", end="")
            print("")

        if self.size == 0:
            print("")
