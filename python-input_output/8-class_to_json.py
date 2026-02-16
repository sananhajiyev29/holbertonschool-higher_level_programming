#!/usr/bin/python3
"""Module for converting a class instance to a serializable dict."""


def class_to_json(obj):
    """Returns the dictionary of an object for JSON serialization."""
    return obj.__dict__
