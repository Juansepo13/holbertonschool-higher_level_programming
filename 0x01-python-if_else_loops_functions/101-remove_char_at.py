#!/usr/bin/python3
def remove_char_at(str, n):
    Copy = str[:n] + str[n + 1:]
    if n < 0:
        Copy = str
    return Copy
