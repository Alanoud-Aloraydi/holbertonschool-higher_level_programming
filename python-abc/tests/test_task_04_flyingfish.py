#!/usr/bin/env python3
"""Unittests for FlyingFish, Fish, and Bird classes."""
import unittest
from io import StringIO
from unittest.mock import patch
from task_04_flyingfish import Fish, Bird, FlyingFish


class TestFlyingFish(unittest.TestCase):
    """Test cases for multiple inheritance and MRO."""

    def test_fish_methods(self):
        """Test Fish class methods."""
        f = Fish()
        with patch('sys.stdout', new=StringIO()) as out:
            f.swim()
            self.assertEqual(out.getvalue().strip(), "The fish is swimming")
        with patch('sys.stdout', new=StringIO()) as out:
            f.habitat()
            self.assertEqual(out.getvalue().strip(), "The fish lives in water")

    def test_bird_methods(self):
        """Test Bird class methods."""
        b = Bird()
        with patch('sys.stdout', new=StringIO()) as out:
            b.fly()
            self.assertEqual(out.getvalue().strip(), "The bird is flying")
        with patch('sys.stdout', new=StringIO()) as out:
            b.habitat()
            self.assertEqual(out.getvalue().strip(), "The bird lives in the sky")

    def test_flyingfish_methods(self):
        """Test FlyingFish class overridden methods."""
        ff = FlyingFish()
        with patch('sys.stdout', new=StringIO()) as out:
            ff.swim()
            self.assertEqual(out.getvalue().strip(), "The flying fish is swimming!")
        with patch('sys.stdout', new=StringIO()) as out:
            ff.fly()
            self.assertEqual(out.getvalue().strip(), "The flying fish is soaring!")
        with patch('sys.stdout', new=StringIO()) as out:
            ff.habitat()
            self.assertEqual(out.getvalue().strip(), "The flying fish lives both in water and the sky!")

    def test_mro(self):
        """Test Method Resolution Order (MRO) for FlyingFish."""
        expected_mro = [FlyingFish, Fish, Bird, object]
        self.assertEqual(FlyingFish.mro(), expected_mro)


if __name__ == "__main__":
    unittest.main()
