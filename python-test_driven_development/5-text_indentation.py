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

    i = 0
    while i < len(text):
        # Skip leading spaces
        while i < len(text) and text[i] == ' ':
            i += 1

        if i == len(text):
            break

        chunk = ""
        # Build the segment until a punctuation mark or newline
        while i < len(text) and text[i] not in ['.', '?', ':', '\n']:
            chunk += text[i]
            i += 1

        if i < len(text):
            if text[i] in ['.', '?', ':']:
                chunk += text[i]
                print(chunk.strip(" "), end="\n\n")
                i += 1
            elif text[i] == '\n':
                print(chunk.strip(" "), end="\n")
                i += 1
        else:
            print(chunk.strip(" "), end="")
