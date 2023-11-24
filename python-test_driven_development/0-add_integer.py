#!/usr/bin/python3
"""
This is module documentation
"""


def add_integer(a, b=98):
    """
    This is method documentation
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        else:
            a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    return a + b
