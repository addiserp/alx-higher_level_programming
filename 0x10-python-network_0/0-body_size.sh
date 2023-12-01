#!/bin/bash
# a Bash script that takes in a URL, sends a request to..
curl -sI $1 -L | grep "Content-Length" | cut -d " " -f