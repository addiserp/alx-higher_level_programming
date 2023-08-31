#!/usr/bin/python3
# a function that divides 2 integers.
def safe_print_division(a, b):
    try:
        val = a / b
    except (ZeroDivisionError, TypeError):
        False
    except IndexError:
        print("out of range")
    finally:
        print('Inside result: {}'.format(val))

    return val
