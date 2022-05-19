#!/usr/bin/python3
"""created class Square that inherits that Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter public,
        its width and height have the same values"""

        return self.width

    @size.setter
    def size(self, value):
        """validations"""

        self.width = value

    def __str__(self, **kwargs):
        """overloading"""

        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """adding method public"""
        if len(args):
            """args non-kwargs"""
            for iter_arg, arg in enumerate(args):
                if iter_arg == 0:
                    self.id = arg
                elif iter_arg == 1:
                    self.size = arg
                elif iter_arg == 2:
                    self.x = arg
                elif iter_arg == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """by adding the public method, that returns the dictionary"""

        vars = ['id', 'size', 'x', 'y']
        dict = {}
        for i in range(len(vars)):
            dict.update({vars[i]: getattr(self, vars[i])})
        return dict
