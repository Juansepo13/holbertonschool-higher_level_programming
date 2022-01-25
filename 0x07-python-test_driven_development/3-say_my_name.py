#!/usr/bin/python3
"""
Module for say_my_name() function.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.
    Args:
        first_name: A string of characters.
        last_name: A string of characters.
    Raises:
        TypeError: If the arguments are not strings of characters.

    Returns:
        A string of characters.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
