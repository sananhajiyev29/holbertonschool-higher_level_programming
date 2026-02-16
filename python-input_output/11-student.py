#!/usr/bin/python3
"""Module defining a Student class with reload capability."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict of attributes, optionally filtered by attrs."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dict."""
        for key, value in json.items():
            setattr(self, key, value)
