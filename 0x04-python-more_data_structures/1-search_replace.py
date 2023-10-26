#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """replaces all occurences of an element by another new list"""

    return list(map(lambda i: replace if i == search else i, my_list))
