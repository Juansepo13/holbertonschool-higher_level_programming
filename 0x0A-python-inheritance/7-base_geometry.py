#!/usr/bin/python3
"""
Module that define an empty class.
"""


class BaseGeometry:
    """
    class BaseGeometry.
    """
    def area(self):
        raise Exception("are() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater that 0")
