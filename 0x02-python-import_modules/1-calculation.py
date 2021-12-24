#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
if __name__ == "__main__":
    # add
    print("{:s} + {:s} = {:s}".format(str(a), str(b), str(add(a, b))))
    # sub
    print("{:s} - {:s} = {:s}".format(str(a), str(b), str(sub(a, b))))
    # mul
    print("{:s} * {:s} = {:s}".format(str(a), str(b), str(mul(a, b))))
    # div
    print("{:s} / {:s} = {:s}".format(str(a), str(b), str(div(a, b))))
