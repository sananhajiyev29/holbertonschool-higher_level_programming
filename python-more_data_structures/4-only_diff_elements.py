#!/usr/bin/python3
"""
4-only_diff_elements.py
Contains a function that returns a set of elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements present in only one of the two sets.

    Args:
        set_1 (set): First set
        set_2 (set): Second set

    Returns:
        set: Elements present in only one set
    """
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return None
    return set_1 ^ set_2
