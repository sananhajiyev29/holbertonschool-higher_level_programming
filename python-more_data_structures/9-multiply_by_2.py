#!/usr/bin/python3
"""
9-multiply_by_2.py
Contains a function that returns a new dictionary
with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): dictionary with integer values

    Returns:
        dict: new dictionary with values multiplied by 2
    """
    if not isinstance(a_dictionary, dict):
        return {}

    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2

    return new_dict
