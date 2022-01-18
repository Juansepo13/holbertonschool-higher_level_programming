#!/usr/bin/python3
"""Module that creates an empty square."""


class Square:
    """Create Square Empty."""
    def __init__(self, size = 0):
        """Initialize square with size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
