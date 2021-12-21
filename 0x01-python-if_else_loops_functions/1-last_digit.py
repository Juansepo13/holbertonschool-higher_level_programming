#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of "
last = number % 10
if number < 0:
        last -= 10
        if last > 5:
                print(str+"{:d} is {:d} and is greater than 5".format(number, last))
        elif last == 0:
                print(str+"{:d} is {:d} and is 0".format(number, last))
        else:
                print(str+"{:d} is {:d} and is less than 6 and not 0".format(number, last))
