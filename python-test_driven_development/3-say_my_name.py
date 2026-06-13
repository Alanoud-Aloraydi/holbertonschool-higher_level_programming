#!/usr/bin/python3
"""
This module provides a function `say_my_name`
that prints a first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name: The first name (must be a string).
        last_name: The last name (must be a string, default is "").

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
