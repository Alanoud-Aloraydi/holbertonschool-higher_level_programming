#!/usr/bin/env python3
"""Module for extending the Python list with notifications."""


class VerboseList(list):
    """List subclass that prints notifications on modification."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list with items and print a notification."""
        items_added = len(item)
        super().extend(item)
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        value = self[index]
        print("Popped [{}] from the list.".format(value))
        return super().pop(index)
