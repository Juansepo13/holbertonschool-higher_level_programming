#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# abs is to calculate the absolute of a number
if number < 0:
    lastDigit = abs(number) % 10 * -1
else:
    lastDigit = number % 10

print("Last digit of {0:d} is {1:d} ".format(number, lastDigit), end="")

if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
