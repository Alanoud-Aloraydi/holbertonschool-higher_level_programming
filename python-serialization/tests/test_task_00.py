#!/usr/bin/env python3
"""Unittests for basic serialization."""
import unittest
import os
from task_00_basic_serialization import serialize_and_save_to_file
from task_00_basic_serialization import load_and_deserialize


class TestBasicSerialization(unittest.TestCase):
    """Test cases for serialization module."""

    def setUp(self):
        """Set up test environment."""
        self.filename = "test_data.json"
        self.data = {"name": "Holberton", "age": 100}

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_serialization_deserialization(self):
        """Test the full serialization cycle."""
        serialize_and_save_to_file(self.data, self.filename)
        self.assertTrue(os.path.exists(self.filename))
        result = load_and_deserialize(self.filename)
        self.assertEqual(self.data, result)


if __name__ == "__main__":
    unittest.main()
