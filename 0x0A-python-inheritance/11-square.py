#!/usr/bin/python3
"""Class square inherent from a class rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """Initalize method"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ area of rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """return string and print when print called"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
