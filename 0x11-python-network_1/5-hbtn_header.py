#!/usr/bin/python3
"""
Response header value #1
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get('X-Request-Id')))
