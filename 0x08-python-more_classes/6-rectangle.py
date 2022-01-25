#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """class rectangle
    - area
    - perimeter
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width < 0:
            raise ValueError("width must be >=0")
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height < 0:
            raise ValueError("height must be >=0")
        self.__height = new_height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print square to stdout"""
        result = ""
        if self.width == 0 and self.height == 0:
            return result
        else:
            for i in range(self.height):
                result += "#" * self.width
                if i != self.height - 1:
                    result += "\n"
        return result

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """print when user delete a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
