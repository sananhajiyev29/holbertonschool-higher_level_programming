#!/usr/bin/python3
"""Check if an object is an instance of a class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or inherits from, a given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses,
        otherwise False.
    """
    return isinstance(obj, a_class)
