#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if num != 0 and number < 0:
        print('Last digit of {} is -{} and is less than 6 and not 0'.format(
                            number, num))
elif num == 0:
        print('Last digit of {} is {} and is 0'.format(number, num))
elif num > 5:
        print('Last digit of {} is {} and is greater than 5'.format(number, num))
else:
        print('Last digit of {} is {} and is less than 6 and not 0'.format(
                            number, num))
