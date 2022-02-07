#!/usr/bin/python3
"""Defining Square Class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor of square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size of square with rectangle attributes"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """*args is the list of arguments - no-keyworded arguments
        - **kwargs must be skipped if *args exists and is not empty
        - Each key in this dictionary represents an attribute to the instance
        """
        args_list = ["id", "width", "x", "y"]
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

    def __str__(self):
        """The overloading __str__ method for square"""
        return ("[Square] {:d} {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
