#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if ((number % 10) > 5):
    print("Last digit of {} is {} and greater then 5".format(number,(number % 10)))
elif ((number % 10) == 0):
    print("Last digit of {} is {} and zero".format(number,(number % 10)))
elif ((number % 10) < 6 ):
    print("Last digit of {} is {} and less than 6 and not 0".format(number,(number % 10)))
