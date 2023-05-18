#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_sorted_dict = sorted(a_dictionary.keys())
    for key, value in my_sorted_dict.items():
        print(f"{key}: {value}
