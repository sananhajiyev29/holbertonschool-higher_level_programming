#!/usr/bin/python3
"""
7-update_dictionary.py
Contains a function that replaces or adds key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): dictionary to update
        key (str): key to update or add
        value: value to associate with key

    Returns:
        dict: the updated dictionary
    """
    if not isinstance(a_dictionary, dict):
        return a_dictionary

    a_dictionary[key] = value
    return a_dictionary
