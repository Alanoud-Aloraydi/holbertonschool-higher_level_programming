#!/usr/bin/env python3
"""Module for converting CSV to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to a JSON file and return status."""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvf:
            reader = csv.DictReader(csvf)
            data = list(reader)
        with open('data.json', 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf)
        return True
    except Exception:
        return False
