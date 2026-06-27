#!/usr/bin/env python3
"""Module exploring multiple inheritance with Fish and Bird."""


class Fish:
    """Class representing a generic Fish."""

    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a generic Bird."""

    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a FlyingFish inheriting from Fish and Bird."""

    def fly(self):
        """Override the flying behavior for FlyingFish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swimming behavior for FlyingFish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat for FlyingFish."""
        print("The flying fish lives both in water and the sky!")
