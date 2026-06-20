#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2
