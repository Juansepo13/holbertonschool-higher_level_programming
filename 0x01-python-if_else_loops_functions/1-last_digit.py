#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = "Last digit of"
if number >= 0:
        last = number % 10
else:
        last = number % -10
        if last > 5:
                print("{} {} is {} and is greater than 5".format(st, number, last))
        elif last == 0:
                print("{} {} is {} and is 0".format(st, number, last))
        elif last < 6 and last != 0:
                print("{} {} is {} and is less than 6 and not 0".format(st, number, last))
