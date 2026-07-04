#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects."""
import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to the given filename."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from the given filename."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
