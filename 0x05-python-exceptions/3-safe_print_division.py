#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        inside = a / b
        return inside
    except ZeroDivisionError:
        inside = None
        return inside
    finally:
        print("Inside result: {}".format(inside))
