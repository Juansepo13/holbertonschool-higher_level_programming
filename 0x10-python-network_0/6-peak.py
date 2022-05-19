#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """ find peak """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
