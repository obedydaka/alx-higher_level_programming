#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
temp_num = number

if number < 0:
    number = -(number)

last_digit = number % 10
if temp_num < 0:
    number = temp_num
    last_digit = -(last_digit)

if last_digit > 5:
    string = "and is greater than 5"
elif last_digit == 0:
    string = "and is 0"
elif last_digit < 6:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, last_digit), string)
