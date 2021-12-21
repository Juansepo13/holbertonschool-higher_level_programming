#!/usr/bin/python3
def uppercase(str):
    for elem in str:
        if (ord(elem) >= ord('a') and ord(elem) <= ord('z')):
            elem = ord(elem) - ord(' ')
        else:
            elem = ord(elem)
            print("{:c}".format(elem), end='')
            print()
