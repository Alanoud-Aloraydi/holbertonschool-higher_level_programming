#!/usr/bin/python3
"""Module defining the Student class with filter."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student."""
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
