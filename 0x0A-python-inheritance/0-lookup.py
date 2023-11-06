#!/usr/bin/python3
"""List of Object's attributes """


def lookup(obj):
    """ Outputs a list of objects methods

    Args:
        (obj) object to search for attributes
    """
    return (dir(obj))
