#!/usr/bin/python3
def max_integer(my_list=[]):
    if not list:
        return
    temp = 0
    for i in range(len(my_list)):
        if my_list[i] > temp:
            temp = my_list[i]
    return temp 
