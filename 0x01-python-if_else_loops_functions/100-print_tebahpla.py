#!/usr/bin/python3


i = 122
while i > 96:
    c = 0
    if i % 2 != 0:
        i -= 32
        c = 1

    print("{}".format(chr(i)), end="")

    if c == 1:
        i += 32

    i -= 1
