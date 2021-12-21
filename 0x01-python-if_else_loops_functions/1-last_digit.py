#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
        new = number * (-1)
        last = new % 10
        last *= (-1)
else:
        last = number % 10
        if last > 5:
                r = ("and is greater than 5")
        elif last == 0:
                r = ("and is 0")
        elif last != 0 and last < 6:
                r = ("and is less than 6 and not 0")
                print("Last digit of {} is {} {}".format(number, last, r))
