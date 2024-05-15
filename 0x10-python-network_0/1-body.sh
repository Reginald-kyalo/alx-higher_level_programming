#!/bin/bash
#Prints response body of url specified in command line arguments
curl -s -w "%{http_code}" "$1" && [ "$(< /dev/stdin)" = "200" ] && curl -s "$1"
