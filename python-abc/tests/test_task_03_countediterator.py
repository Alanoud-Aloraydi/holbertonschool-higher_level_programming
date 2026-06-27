#!/usr/bin/env python3
"""Unittests for CountedIterator."""
import unittest
from task_03_countediterator import CountedIterator


class TestCountedIterator(unittest.TestCase):
    """Test cases for CountedIterator."""

    def test_normal_iteration(self):
        """Test normal list iteration."""
        c_iter = CountedIterator([1, 2])
        self.assertEqual(c_iter.get_count(), 0)
        self.assertEqual(next(c_iter), 1)
        self.assertEqual(c_iter.get_count(), 1)
        self.assertEqual(next(c_iter), 2)
        self.assertEqual(c_iter.get_count(), 2)
        with self.assertRaises(StopIteration):
            next(c_iter)

    def test_empty_iterable(self):
        """Test empty iterable."""
        c_iter = CountedIterator([])
        with self.assertRaises(StopIteration):
            next(c_iter)
        self.assertEqual(c_iter.get_count(), 0)

    def test_string_iterable(self):
        """Test string iteration."""
        c_iter = CountedIterator("ab")
        self.assertEqual(next(c_iter), 'a')
        self.assertEqual(c_iter.get_count(), 1)


if __name__ == "__main__":
    unittest.main()
