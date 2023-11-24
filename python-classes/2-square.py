#!/usr/bin/python3
"""
This is module documentation
"""


class Square:
    """
    This is class documentation
    """
    def __init__(self, size=0):
        """
        This is method documentation
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size=size
