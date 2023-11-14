#!/usr/bin/python3
"""Integer addition module"""

def add_integer(a, b=98):
    """Adds sum of two integer passed as parameters
    Args:
        a: first integer param
        b: second integer param

    Raises:
        TypeError: if either a or b is not a float or integer

    Returns:
        Sum of the two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
