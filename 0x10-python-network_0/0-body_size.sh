#!/bin/bash
# It takes in a URL, sends a request and displays the size of the body
curl -sI $1 -L | grep "Content-Length" | cut -d " " -f2
