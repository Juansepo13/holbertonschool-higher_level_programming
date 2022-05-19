#!/usr/bin/python3
"""insert a line of text in a file """


def append_after(filename="", search_string="", new_string=""):
    """append text after in file"""
    with open(filename, "r+", encoding="utf-8") as f:
        new_l = ""
        for line in f:
            new_l += line
            if search_string in line:
                new_l += new_string
        f.seek(0)
        f.write(new_l)
