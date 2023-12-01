#!/usr/bin/python3
'''
    a Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
'''

import urllib.request
from sys import argv


if __name__ == "__main__":

    RURL = argv[1]
    try:
        with urllib.request.urlopen(RURL) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except urllib.error.URLError as e:
        print(e.reason)
