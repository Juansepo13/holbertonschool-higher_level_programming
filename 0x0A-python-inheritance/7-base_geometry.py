#!/usr/bin/python3
"""
Module that define an empty class.
"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
