#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    bool_list = []
    length = len(my_list)

    for i in range(length):
        if my_list[i] % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)

    return (bool_list)
