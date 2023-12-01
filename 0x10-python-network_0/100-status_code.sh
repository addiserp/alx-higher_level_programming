#!/bin/bash
# a Bash script that sends a request to a URL passed as
curl -s -o /dev/null -w "%{http_code}" "$1"
