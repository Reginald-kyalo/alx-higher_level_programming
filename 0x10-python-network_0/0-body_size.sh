#!/bin/bash
#Print the content-length of a specified url in bytes
curl -sI $1 | grep -i "Content-Length" | awk '{print $2}'
