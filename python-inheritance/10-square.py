#!/usr/bin/python3
"""Module that defines a Square inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initializes a new Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
