#!/usr/bin/python3
"""
This is module documentation
"""


def print_square(size):
    """
    This is function documentation
    """
    if not isinstance(size, int):
      raise TypeError("size must be an integer")
    elif size < 0:
      raise ValueError("size must be >= 0")
    for i in range(size):
      print("#" * size)
