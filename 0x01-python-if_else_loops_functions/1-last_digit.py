#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    last = (number * -1) % 10
else:
    last = number % 10

if last == 0:
    print("last digit of {} is {} and is zero".format(number, last))
elif last > 5:
    print("last digit of {} is {} and is greater than 5".format(number, last))
else:
    print("last digit of {} is {} and is less than 6 and not zero".format(number, last))
