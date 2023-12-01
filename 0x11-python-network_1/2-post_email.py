#!/usr/bin/python3
'''
    2. POST an email #0
'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    '''
        a Python script that takes in a URL and an email,
        sends a POST request to the passed URL with the email
        as a parameter, and displays the body of the response
        (decoded in utf-8)
    '''

    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    rurl = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(rurl) as response:
        html = response.read()
        print(html)
