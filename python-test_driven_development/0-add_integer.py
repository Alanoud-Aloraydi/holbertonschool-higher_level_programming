#!/usr/bin/python3
"""
This module provides a function `add_integer`
that adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a: First integer or float.
        b: Second integer or float (default 98).

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
