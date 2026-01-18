#!/usr/bin/python3
"""
5-number_keys.py
Contains a function that returns the number of keys in a dictionary
"""


def number_keys(a_dictionary):
    """
    Return the number of keys in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary

    Returns:
        int: Number of keys in the dictionary
    """
    if not isinstance(a_dictionary, dict):
        return None
    return len(a_dictionary.keys())
