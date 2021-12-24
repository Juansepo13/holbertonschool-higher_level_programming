#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    print("{:d} {:s}{:s}".format(length,
                                 "argument" if length == 1 else "arguments",
                                 "." if length == 0 else ":"))
    for i, string in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, string))
