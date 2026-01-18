#!/usr/bin/python3
"""
2-uniq_add.py
Contains a function that adds all unique integers in a list
"""


def uniq_add(my_list=[]):
    """
    Add all unique integers in a list (only once for each integer).

    Args:
        my_list (list): List of integers

    Returns:
        int: Sum of unique integers
    """
    if not isinstance(my_list, list):
        return None
    return sum(set(my_list))
