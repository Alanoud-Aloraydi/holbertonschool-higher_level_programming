#!/usr/bin/env python3
"""Unittests for CustomObject serialization."""
import unittest
import os
from task_01_pickle import CustomObject


class TestCustomObject(unittest.TestCase):
    """Test cases for CustomObject."""

    def test_serialization_deserialization(self):
        """Test valid serialization and deserialization."""
        obj = CustomObject("John", 25, True)
        obj.serialize("test.pkl")
        self.assertTrue(os.path.exists("test.pkl"))
        new_obj = CustomObject.deserialize("test.pkl")
        self.assertEqual(new_obj.name, "John")
        self.assertEqual(new_obj.age, 25)
        self.assertEqual(new_obj.is_student, True)
        os.remove("test.pkl")

    def test_deserialize_nonexistent(self):
        """Test deserialization of a non-existent file."""
        res = CustomObject.deserialize("nonexistent.pkl")
        self.assertIsNone(res)

    def test_deserialize_malformed(self):
        """Test deserialization of a malformed file."""
        with open("bad.pkl", "w") as f:
            f.write("Not a pickle file")
        res = CustomObject.deserialize("bad.pkl")
        self.assertIsNone(res)
        os.remove("bad.pkl")


if __name__ == "__main__":
    unittest.main()
