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
    REALLY tired of documentation
    """
    return self.__position

  @position.setter
  def position(self, value):
    """
    Tired of documentation
    """
    if not isinstance(value[0], int) or not isinstance(value[1], int) or len(value) != 2 or any(i < 0 for i in value):
        raise TypeError('position must be a tuple of 2 positive integers')
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
      print('\n' * space_y, end='')  # print newlines for the y position
      print(('\n'.join([' ' * space_x + '#' * side for k in range(side)])))
