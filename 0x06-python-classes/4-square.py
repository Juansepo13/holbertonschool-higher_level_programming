#!/usr/bin/python3
"""Create new class Square"""


class Square:
    """Class Square empty"""
    def __init__(self, size=0):
        """Initialize square with size."""
        self.__size = size

    def area(self):
        """Returns current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Rescue the square's size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size!"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
