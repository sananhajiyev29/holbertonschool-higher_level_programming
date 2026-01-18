#!/usr/bin/python3
"""Task 2: Converting CSV Data to JSON Format.

This module provides a function to read a CSV file and serialize it into
a JSON file named data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format and save it to data.json.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(dict(row))

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)
        return True
    except Exception:
        return False
