#!/usr/bin/python3
"""
A script that takes in a URL and an email address, sends a
finally displays the body of the response and
POST request to the passed URL with the email as a parameter,

"""


import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
