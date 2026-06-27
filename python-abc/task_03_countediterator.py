#!/usr/bin/env python3
"""Module for CountedIterator class."""


class CountedIterator:
    """Class that extends an iterator to count fetched items."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item
