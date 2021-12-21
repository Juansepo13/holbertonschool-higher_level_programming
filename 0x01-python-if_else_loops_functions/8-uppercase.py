#!/usr/bin/python3
def uppercase(str):
    for char in str:
        charoffset = 0
        if ord(char) > 96 and ord(char) < 123:
            charoffset = -32
            print("{:s}".format(chr(ord(char) + charoffset)), end='')
            print('')
