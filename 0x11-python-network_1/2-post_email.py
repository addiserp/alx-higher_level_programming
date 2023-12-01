#!/usr/bin/python3
'''
    a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the response
    (decoded in utf-8)
'''

import urllib
import sys


if __name__ == "__main__":

    values = {'email': sys.argv[2]}
    MYD = urllib.parse.urlencode(values).encode('utf-8')
    rurl = urllib.request.Request(sys.argv[1], MYD)

    with urllib.request.urlopen(rurl) as response:
        html = response.read()
        print(html)
