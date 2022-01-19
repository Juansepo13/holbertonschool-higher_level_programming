#!/usr/bin/python3
"""Module that creates an empty square."""


class Square:
    """Empty square."""
    def __init__(self, size=0):
        """Initialize square with size."""
        self.__size = size

        def area(self):
            """returns the current square area"""
            return self.__size * self.__size

        @property
        def size(self):
            """rescue the size of the square"""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of the square!"""
            if type(size) is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def my_print(self):
            """prints in stdout the square with the character #:"""
            """if size is equal to 0, print an empty line"""
            for i in range(self.__size):
                print("#" * self.__size))
            if self.__size is 0:
                print()
