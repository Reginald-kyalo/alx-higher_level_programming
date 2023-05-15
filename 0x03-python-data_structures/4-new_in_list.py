#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return list
    list[idx] = element
    return list
