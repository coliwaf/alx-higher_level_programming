#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv)
    funcs = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }

    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    if sys.argv[2] not in list(funcs.keys()):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    func = funcs[sys.argv[2]]
    res = func(a, b)

    print('{:d} {:s} {:d} = {:d}'.format(a, sys.argv[2], b, res))
