#!/usr/bin/env python3
"""Unittests for convert_csv_to_json."""
import unittest
import os
from task_02_csv import convert_csv_to_json


class TestCsvToJson(unittest.TestCase):
    """Test cases for CSV to JSON conversion."""

    def setUp(self):
        """Set up test environment."""
        self.csv_file = "test_data.csv"
        self.json_file = "data.json"
        with open(self.csv_file, 'w', encoding='utf-8') as f:
            f.write("name,age\nAlice,24\nBob,22\n")

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_conversion_success(self):
        """Test successful conversion."""
        res = convert_csv_to_json(self.csv_file)
        self.assertTrue(res)
        self.assertTrue(os.path.exists(self.json_file))

    def test_file_not_found(self):
        """Test with non-existent file."""
        res = convert_csv_to_json("nonexistent.csv")
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
