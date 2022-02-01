#!/usr/bin/python3
"""Class definition"""


class MyInt(int):
    """Class MyInt"""

    def __eq__(self, other):
        """Method to override equal -> ne"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Method to overrider ne -> eq"""
        return super().__eq__(other)
