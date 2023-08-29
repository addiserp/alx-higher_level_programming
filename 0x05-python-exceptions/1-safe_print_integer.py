#!/usr/bin/python3
# a function that prints an integer with "{:d}".format().
def safe_print_integer(v):
    try:
        print("{:d}".format(v))
        return True
    except Exception:
        return False
