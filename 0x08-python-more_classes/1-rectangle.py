#!usr/bin/python3
"""Rectangle - and empty class rectangle that defines one area"""


class Rectangle:
    """Empty"""
    pass

class Rectangle:
    """Define instantiates for the square"""
    def __init__(self, width=0, height=0):
        """Set with an height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set and validations"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set and validations"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
