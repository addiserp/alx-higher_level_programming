#!/usr/bin/python3
'''
    1. Response header value #0
'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    '''
        a Python script that takes in a URL, sends a request to the URL
        and displays the value of the X-Request-Id variable found in the
        header of the response.
    '''
    rurl = argv[1]
    with urllib.request.urlopen(rurl) as response:
        html = response.read()
        print(dict(response.headers).get("X-Request-Id"))
