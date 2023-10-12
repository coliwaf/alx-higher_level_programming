#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    myLen = len(sys.argv) - 1

    if myLen == 0:
        print("{} arguments.".format(myLen))
    elif myLen > 1:
        print("{} arguments.".format(myLen))
        for i in range(1, myLen + 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} argument".format(myLen))
        print("{}: {}".format(myLen, sys.argv[1]))
