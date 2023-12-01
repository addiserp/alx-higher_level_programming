#!/usr/bin/python3
'''
    2. POST an email #0
'''

import urllib.request
from sys import argv

if __name__ == "__main__":

    values = {'email': argv[2]}
    MYD = urllib.parse.urlencode(values).encode('utf-8')
    rurl = urllib.request.Request(argv[1], MYD)

    with urllib.request.urlopen(rurl) as response:
        html = response.read()
        print(html)
