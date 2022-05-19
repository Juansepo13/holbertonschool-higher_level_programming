#!/usr/bin/python3
"""
function print_square
size
class
"""


def print_square(size):
     """function that prints a square with the character '#' """
     if type(size) is not int:
          raise TypeError("size must be an integer")
     if size < 0:
          raise ValueError("size must be >= 0")
     if type(size) is float and size < 0:
          raise TypeError("size must be an integer")
     for i in range(size):
          print("#" * size)
