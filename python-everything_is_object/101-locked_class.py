#!/usr/bin/python3
"""Defines a class with restricted instance attributes."""


class LockedClass:
    """Allow instances to have only a first_name attribute."""

    __slots__ = ("first_name",)
