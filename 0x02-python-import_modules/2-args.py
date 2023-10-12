#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    myLen = len(sys.argv) - 1
    vocab = 'argument'
    symbol = '.'

    if myLen > 1 or myLen == 0:
        vocab = 'arguments'
    if myLen == 1 or myLen > 1:
        symbol = ':'

    print("{:d} {:s}{:s}".format(myLen, vocab, symbol))

    for i in range(1, myLen + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
