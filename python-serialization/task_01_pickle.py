#!/usr/bin/python3
"""Task 1: Pickling Custom Classes.

This module defines a CustomObject class that can be serialized and deserialized
using the pickle module.
"""

import pickle


class CustomObject:
    """Custom class with attributes name, age, is_student and
    methods for displaying and pickling.
    """

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance.

        Args:
            name (str): Name of the object
            age (int): Age of the object
            is_student (bool): Whether the object represents a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object and save to a file.

        Args:
            filename (str): The file to save the object to
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Args:
            filename (str): The file to load the object from

        Returns:
            CustomObject: The deserialized object or None if failed
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
