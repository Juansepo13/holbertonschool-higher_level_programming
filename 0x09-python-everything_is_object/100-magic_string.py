#!/usr/bin/python3
def magic_string(Count=[0]):
    Count[0] += 1
    return("".join(list("holberton" * Count[0])))
