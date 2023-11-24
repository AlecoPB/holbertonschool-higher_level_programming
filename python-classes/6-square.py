#!/usr/bin/python3
"""
This is module documentation
"""


class Square:
    """
    This is class documentation
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2 or\
           not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        This is method documentation
        """
        return self.__size

    @property
    def position(self):
        """
        REALLY tired of documentation
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        This is also method documentation
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Tired of documentation
        """
        if not isinstance(value[0], int) or not isinstance(value[1], int) or\
           len(value) != 2 or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Can you guess what this is?
        """
        return self.__size**2

    def my_print(self):
        """
        Wowowow what is this?
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
