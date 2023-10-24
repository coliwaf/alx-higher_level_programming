#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    bigst_int = my_list[0]
    for i in range(length):
        if my_list[i] > bigst_int:
            bigst_int = my_list[i]

    return (bigst_int)

