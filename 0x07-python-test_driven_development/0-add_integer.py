#!/usr/bin/python3
"""
Module for add_integer() function.
"""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a: Integer or float.
        b: Integer or float.

    Returns:
        An integer. The addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
