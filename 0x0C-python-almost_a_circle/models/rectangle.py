#!/usr/bin/python3
"""Defining Rectangle Class."""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
        - __width: width
        -__height: height
        -__x: position
        -__y: position
        -id: id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the widht."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area value of Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints in stdout Rectangle instance with character #."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ public method def update that assigns an
        argument to each attribute
        -**kwargs must be skipped if *args exists and is not empty
        -Each key in this dictionary represents an attribute to the instance
        """
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
         """dictionary representation of a Square"""
         key_list = ["id", "width", "height", "x", "y"]
         value_list = [self.id, self.width, self.height, self.x, self.y]
         return dict(zip(key_list, value_list))
