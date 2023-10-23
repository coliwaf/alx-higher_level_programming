#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0

    for itm in my_list:
        if i < x:
            try:
                print("{}".format(itm), end="")
                i += 1
            except IndexError:
                print()
                return i

    print()
    return i
