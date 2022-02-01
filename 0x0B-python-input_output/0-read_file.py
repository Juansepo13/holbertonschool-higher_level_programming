#!/usr/bin/python3
"""0. Read file
"""


def read_file(filename=""):
    """Write a function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename, 'r') as file:
        file_content = file.read()
    print(file_content, end="")
