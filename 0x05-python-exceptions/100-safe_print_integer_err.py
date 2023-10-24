#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as val_err:
        print("Exception: {}".format(val_err), file=sys.stderr)
        return False
    except TypeError as typ_err:
        print("Exception: {}".format(typ_err), file=sys.stderr)
        return False
