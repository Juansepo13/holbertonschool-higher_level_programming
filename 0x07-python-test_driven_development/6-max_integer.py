#!/usr/bin/python3
"""
Module to find the
max integer
in a list
"""


def max_integer(lista=[]):
    """
    Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(lista) == 0:
        return None
    if type(lista) is not list:
        raise TypeError("List must be a type list")
    for i in lista:
        if type(i) is not int:
            raise TypeError("Elements of the list must be a integers")
    result = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > result:
            result = lista[i]
        i += 1
    return result
