#!/usr/bin/python3
"""
Module that defines the is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Returns Ture if the object is an instance of the specified class.
    """
    return (type(obj) == a_class)
