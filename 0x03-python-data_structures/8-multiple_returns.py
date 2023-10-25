#!/usr/bin/python3


def multiple_returns(sentence):

    length = len(sentence)

    if (length < 1):
        return (0, None)

    first_char = sentence[0]
    tup_res = length, first_char
    return (tup_res)
