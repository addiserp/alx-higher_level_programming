#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))


try:
    r2 = Rectangle()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))