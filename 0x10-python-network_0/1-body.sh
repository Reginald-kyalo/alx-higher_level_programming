#!/bin/bash
#Prints response body of url specified in command line arguments
#only if status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$response" = "200" ]; then
    curl -s "$1"
fi
