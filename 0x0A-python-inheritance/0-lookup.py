#!/bin/user/python3
"""Write a function that returns the list of
   available attributes and methods of an object"""


def lookup(obj):
    """Prototype: def lookup(obj)
       Returns a list object
       You are not allowed to import any module"""
    return dir(obj)
