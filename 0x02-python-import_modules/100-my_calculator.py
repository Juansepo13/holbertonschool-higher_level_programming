#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    var = len(argv) - 1
    if var != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = str(argv[2])
    b = int(argv[3])
    if op not in ['+', '-', '*', '/']:
        msg = "Unknown operator. Available operators: +, -, * and /"
        print(msg, end='\n')
        exit(1)
    else:
        eq = {'+': add(a, b), '*': mul(a, b), '-': sub(a, b), '/': div(a, b)}
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, eq.get(op)), end='\n')
