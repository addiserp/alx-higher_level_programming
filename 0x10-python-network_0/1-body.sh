#!/bin/bash
# a Bash script that takes in a URL, sends a GET
curl -sX GET "$1" -L 200
