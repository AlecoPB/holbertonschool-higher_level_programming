#!/usr/bin/python3
"""
This is module documentation
"""
class Square:
    """
    This is class documentation
    """
    def __init__(self, size=0):
        self.__size=size

    @property
    def size(self):
        """
        This is method documentation
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is also method documentation
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size=size
        
    def area(self):
        """
        Can you guess what this is?
        """
        return self.__size**2
