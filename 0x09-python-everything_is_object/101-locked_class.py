#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """ 
    Prevents the user from dynamically creating new instance attrbutes
    """

    __slots__ = ["first_name"]
