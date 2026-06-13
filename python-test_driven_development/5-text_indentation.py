#!/usr/bin/python3
"""
This module provides a function `text_indentation`
that prints a text with 2 new lines after each '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.
    There should be no space at the beginning or at the end
    of each printed line.

    Args:
        text: The text string to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
