#!/usr/bin/python3
"""method"""


def append_write(filename="", text=""):
    """Write on file create the file if doesn’t exist
    overwrite the content of the file if it already exists"""
    with open(filename, 'a', encoding="utf-8") as fil:
        return(fil.write(text))
