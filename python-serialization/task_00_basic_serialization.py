#!/usr/bin/python3
"""Task 0: Basic serialization and deserialization of Python dictionaries
to and from JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the file to write JSON data to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file to a Python dictionary.

    Args:
        filename (str): Name of the JSON file to read from

    Returns:
        dict: Python dictionary deserialized from JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
