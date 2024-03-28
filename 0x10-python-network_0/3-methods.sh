#!/bin/bash
#Displays allowed methods
curl -sI $1 | grep -i "Allow" | awk '{$1=""; print $0}' | sed 's/^[ \t]*//'
