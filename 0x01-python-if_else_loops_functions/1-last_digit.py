#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number % 10
if ((number % 10) > 5):
    print("Last digit of {} is {} and greater than 5".format(number, rem))
elif ((number % 10) == 0):
    print("Last digit of {} is {} and zero".format(number, rem))
elif ((number % 10) < 6):
    print("Last digit of {} is {} and less than 6 and not 0".format(number, rem))
