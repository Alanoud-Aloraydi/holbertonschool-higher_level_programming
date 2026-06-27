#!/usr/bin/env python3
"""Module for Abstract Animal Class and its Subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the animal's sound."""
        pass


class Dog(Animal):
    """Class representing a dog, inherits from Animal."""

    def sound(self):
        """Returns the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat, inherits from Animal."""

    def sound(self):
        """Returns the sound made by a cat."""
        return "Meow"
