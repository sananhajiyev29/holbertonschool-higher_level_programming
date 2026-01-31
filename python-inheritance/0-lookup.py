#!/usr/bin/python3
"""
This module provides a function to list all available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Any object

    Returns:
        list: List of attribute and method names
    """
    return dir(obj)
