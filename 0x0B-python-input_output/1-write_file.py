#!/usr/bin/python3
"""method"""


def write_file(filename="", text=""):
    """write on file create the file if doesn’t exist
    overwrite the content of the file if it already exists"""
    with open(filename, 'w', encoding="utf-8") as fil:
        return(fil.write(text))
