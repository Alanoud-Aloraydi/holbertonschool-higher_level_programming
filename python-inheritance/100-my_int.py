#!/usr/bin/python3
"""Module that defines a rebel integer class MyInt."""


class MyInt(int):
    """Class that inherits from int and inverts == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator to !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator to ==."""
        return super().__eq__(other)
