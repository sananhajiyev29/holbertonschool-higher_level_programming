#!/usr/bin/python3
"""
6-print_sorted_dictionary.py
Contains a function that prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary by ordered keys (alphabetically).

    Args:
        a_dictionary (dict): The dictionary to print
    """
    if not isinstance(a_dictionary, dict):
        return
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
