#!/usr/bin/python3
"""method  module"""


def read_file(filename=""):
    """read  file function"""
    with open(filename, encoding="utf-8") as textfile:
        for line in textfile:
            print(line, end="")
