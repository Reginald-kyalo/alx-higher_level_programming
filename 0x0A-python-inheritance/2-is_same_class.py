#!/usr/bin/python3
# 2-is_same_class.py
# Reginald-kyalo
"""Defines class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is precisely an instance of a given class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
