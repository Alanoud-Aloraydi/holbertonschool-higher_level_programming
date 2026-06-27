#!/usr/bin/env python3
"""Module demonstrating Mixins with SwimMixin, FlyMixin and Dragon."""


class SwimMixin:
    """Mixin class providing swimming functionality."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying functionality."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from both SwimMixin and FlyMixin."""

    def roar(self):
        """Print the roaring action."""
        print("The dragon roars!")
