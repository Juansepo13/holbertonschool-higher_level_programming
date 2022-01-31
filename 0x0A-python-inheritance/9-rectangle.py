#!/usr/bin/python3
""" Module that import a class. """


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Class Rectangle."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
