#!/usr/bin/python3
"""This module contains a Rectangle class"""


class Rectangle:
    """Class Rectangle that defines a rectagle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter in width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter in width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter in height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter in height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcs the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calcs the rectangle' perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        s = (((str(self.print_symbol) * self.width) + '\n') * self.height)[:-1]
        return s

    def __repr__(self):
        """Return the representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
