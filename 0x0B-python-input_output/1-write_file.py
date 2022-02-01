#!/usr/bin/python3
"""
Initializes the number_of_lines() function.
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file.
    """
    with open(filename) as NewText:
        return sum(1 for line in NewText)
