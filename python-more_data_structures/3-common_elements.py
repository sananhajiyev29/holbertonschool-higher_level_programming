#!/usr/bin/python3
"""
3-common_elements.py
Contains a function that returns a set of common elements in two sets
"""


def common_elements(set_1, set_2):
    """
    Return a set of common elements in two sets.

    Args:
        set_1 (set): First set
        set_2 (set): Second set

    Returns:
        set: Set of elements present in both sets
    """
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return None
    return set_1 & set_2
