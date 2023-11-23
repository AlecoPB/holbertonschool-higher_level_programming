#!/usr/bin/python3
"""
This is module documentation
"""
class Square:
    """
    This is class documentation
    """
    def __init__(self, size=0, position=(0, 0)):
      self.__size = size
      self.__position = position
      
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
      if not isinstance(value, int):
        raise TypeError('size must be an integer')
      if value < 0:
        raise ValueError('size must be >= 0')
      self.__size = value

    @property
    def position(self):
      """
      This is a getter
      """
      return self.__position

    @position.setter
    def position(self, value):
      """
      This is a setter
      """
      if not isinstance(value[0], int) or not isinstance(value[1], int) or value[0] < 0 or value [1] < 0:
        raise TypeError('position must be a tuple of two positive integers')
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
      side = self.__size
      space_x = self.__position[0]
      space_y = self.__position[1]
      if side == 0:  
        print()
      else:
        for i in range(space_y): 
          print()
        for i in range(side):
          for j in range(space_x):
            print(" ", end='')
          for j in range(side):
            print('#', end='')
          print()
