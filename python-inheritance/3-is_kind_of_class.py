#!/usr/bin/python3
"""Module that checks if an object is an instance or inherited instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
