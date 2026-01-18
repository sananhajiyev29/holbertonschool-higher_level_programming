#!/usr/bin/python3
"""
1-search_replace.py
Contains a function that replaces all occurrences of an element in a list
"""


def search_replace(my_list, search, replace):
    """
    Replace all occurrences of `search` in `my_list` with `replace`.

    Args:
        my_list (list): The initial list
        search: The element to replace
        replace: The new element

    Returns:
        list: A new list with replaced elements
    """
    if not isinstance(my_list, list):
        return None
    return [replace if x == search else x for x in my_list]
