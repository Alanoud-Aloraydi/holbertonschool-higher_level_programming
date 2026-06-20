#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to set the position with validation."""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            msg = "position must be a tuple of 2 positive integers"
            raise TypeError(msg)
        self.__position = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character and position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
