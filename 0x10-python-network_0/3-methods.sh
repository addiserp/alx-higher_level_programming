#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP server will accept.
curl - sI "$1" | grep "Allow" | cut - d " " - f2-