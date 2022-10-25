#!/usr/bin/python3
"""
Adding two integers
"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    typecast floats to ints before adding
    raised a TypeError if any arg is neither
        a float or an int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
