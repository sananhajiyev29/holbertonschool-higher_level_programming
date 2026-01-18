#!/usr/bin/python3
"""
8-simple_delete.py
Contains a function that deletes a key in a dictionary
"""


def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary if it exists.

    Args:
        a_dictionary (dict): dictionary to modify
        key (str): key to delete

    Returns:
        dict: the modified dictionary
    """
    if not isinstance(a_dictionary, dict):
        return a_dictionary

    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
