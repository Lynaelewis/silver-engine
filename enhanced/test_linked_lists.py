"""Standard-library tests for the enhanced version. Run: python -m unittest discover -s enhanced -p 'test_*.py'"""
import unittest

from linked_lists import LinkedList, ReversibleLinkedList, SortedLinkedList, UniqueLinkedList


class LinkedListTests(unittest.TestCase):
    def test_basic_add_remove(self):
        values = LinkedList([1, 2])
        values.add_first(0)
        values.add_last(3)
        self.assertEqual(values.to_list(), [0, 1, 2, 3])
        self.assertEqual(values.remove_first(), 0)
        self.assertEqual(values.remove_last(), 3)
        self.assertEqual(values.to_list(), [1, 2])
        self.assertEqual(len(values), 2)

    def test_empty_and_singleton(self):
        values = LinkedList()
        with self.assertRaises(RuntimeError):
            values.remove_last()
        values.add_last(7)
        self.assertEqual(values.remove_last(), 7)
        self.assertEqual(values.to_list(), [])
        self.assertIsNone(values.get_tail())

    def test_reverse(self):
        values = ReversibleLinkedList([1, 2, 3])
        values.reverse()
        self.assertEqual(values.to_list(), [3, 2, 1])
        self.assertEqual(values.get_tail(), 1)
        values.reverse()
        self.assertEqual(values.to_list(), [1, 2, 3])

    def test_reverse_empty(self):
        values = ReversibleLinkedList()
        values.reverse()
        self.assertEqual(values.to_list(), [])

    def test_sorted(self):
        values = SortedLinkedList([5, 1, 3, 3])
        values.add_sorted(0)
        values.add_sorted(9)
        self.assertEqual(values.to_list(), [0, 1, 3, 3, 5, 9])
        self.assertEqual(values.get_tail(), 9)
        with self.assertRaises(NotImplementedError):
            values.add_last(10)

    def test_unique(self):
        values = UniqueLinkedList([1, 2, 1, 3, 2, 2])
        self.assertEqual(values.remove_dups(), {1: 1, 2: 2, 3: 0})
        self.assertEqual(values.to_list(), [1, 2, 3])
        self.assertEqual(len(values), 3)
        self.assertEqual(values.get_tail(), 3)


if __name__ == "__main__":
    unittest.main()
