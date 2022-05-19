#!/usr/bin/python3
"""Module Method."""


def read_file(filename=""):
    """Function that read file"""
    with open(filename, encoding="utf-8") as textfile:
        for line in textfile:
            print(line, end="")
