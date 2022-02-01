#!/usr/bin/python3
"""method """


def class_to_json(obj):
    """Cfunction that returns the dictionary
    description with simple data structure"""
    return obj.__dict__
