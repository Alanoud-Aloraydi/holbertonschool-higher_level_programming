#!/usr/bin/env python3
"""Unittests for XML serialization."""
import unittest
import os
from task_03_xml import serialize_to_xml, deserialize_from_xml


class TestXmlSerialization(unittest.TestCase):
    """Test cases for XML serialization and deserialization."""

    def setUp(self):
        """Set up test environment."""
        self.filename = "test_data.xml"

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_serialization_deserialization(self):
        """Test the full XML serialization cycle."""
        data = {'name': 'John', 'age': '28'}
        serialize_to_xml(data, self.filename)
        self.assertTrue(os.path.exists(self.filename))
        result = deserialize_from_xml(self.filename)
        self.assertEqual(data, result)


if __name__ == "__main__":
    unittest.main()
