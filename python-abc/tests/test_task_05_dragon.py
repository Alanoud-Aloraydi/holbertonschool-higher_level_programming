#!/usr/bin/env python3
"""Unittests for Dragon, SwimMixin, and FlyMixin."""
import unittest
from io import StringIO
from unittest.mock import patch
from task_05_dragon import Dragon, SwimMixin, FlyMixin


class TestDragon(unittest.TestCase):
    """Test cases for Dragon class and its Mixins."""

    def test_swim(self):
        """Test swim method inherited from SwimMixin."""
        d = Dragon()
        with patch('sys.stdout', new=StringIO()) as out:
            d.swim()
            self.assertEqual(out.getvalue().strip(), "The creature swims!")

    def test_fly(self):
        """Test fly method inherited from FlyMixin."""
        d = Dragon()
        with patch('sys.stdout', new=StringIO()) as out:
            d.fly()
            self.assertEqual(out.getvalue().strip(), "The creature flies!")

    def test_roar(self):
        """Test roar method specific to Dragon class."""
        d = Dragon()
        with patch('sys.stdout', new=StringIO()) as out:
            d.roar()
            self.assertEqual(out.getvalue().strip(), "The dragon roars!")

    def test_mixin_standalone(self):
        """Test that mixins can technically be instantiated and used."""
        s = SwimMixin()
        f = FlyMixin()
        with patch('sys.stdout', new=StringIO()) as out:
            s.swim()
            self.assertEqual(out.getvalue().strip(), "The creature swims!")
        with patch('sys.stdout', new=StringIO()) as out:
            f.fly()
            self.assertEqual(out.getvalue().strip(), "The creature flies!")


if __name__ == "__main__":
    unittest.main()
