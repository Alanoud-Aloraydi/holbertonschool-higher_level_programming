#!/usr/bin/python3
"""Module that defines a Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
