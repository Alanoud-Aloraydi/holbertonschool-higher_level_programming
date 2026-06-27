#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """Class MyList that inherits from list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
