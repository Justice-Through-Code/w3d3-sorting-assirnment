import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from merge_sort import merge_sort
from quick_sort import quick_sort


class TestStudentSorting(unittest.TestCase):

    def setUp(self):
        # List of student tuples: (name, gpa)
        self.students_tuples = [
            ("Alice", 3.9),
            ("Bob", 3.4),
            ("Charlie", 3.6),
            ("Diana", 3.4)
        ]

        # List of student dicts
        self.students_dicts = [
            {"name": "Alice", "gpa": 3.9},
            {"name": "Bob", "gpa": 3.4},
            {"name": "Charlie", "gpa": 3.6},
            {"name": "Diana", "gpa": 3.4}
        ]

    def test_merge_sort_tuples_by_gpa(self):
        sorted_list = merge_sort(self.students_tuples, key=lambda x: -x[1])
        expected = [
            ("Alice", 3.9),
            ("Charlie", 3.6),
            ("Bob", 3.4),
            ("Diana", 3.4)
        ]
        self.assertEqual(sorted_list, expected)

    def test_quick_sort_tuples_by_name(self):
        sorted_list = quick_sort(self.students_tuples, key=lambda x: x[0])
        expected = [
            ("Alice", 3.9),
            ("Bob", 3.4),
            ("Charlie", 3.6),
            ("Diana", 3.4)
        ]
        self.assertEqual(sorted_list, expected)

    def test_merge_sort_dicts_by_gpa(self):
        sorted_list = merge_sort(self.students_dicts, key=lambda x: -x["gpa"])
        expected = [
            {"name": "Alice", "gpa": 3.9},
            {"name": "Charlie", "gpa": 3.6},
            {"name": "Bob", "gpa": 3.4},
            {"name": "Diana", "gpa": 3.4}
        ]
        self.assertEqual(sorted_list, expected)

    def test_quick_sort_dicts_by_name(self):
        sorted_list = quick_sort(self.students_dicts, key=lambda x: x["name"])
        expected = [
            {"name": "Alice", "gpa": 3.9},
            {"name": "Bob", "gpa": 3.4},
            {"name": "Charlie", "gpa": 3.6},
            {"name": "Diana", "gpa": 3.4}
        ]
        self.assertEqual(sorted_list, expected)

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        single = [("Only", 4.0)]
        self.assertEqual(merge_sort(single), single)
        self.assertEqual(quick_sort(single), single)

if __name__ == '__main__':
    unittest.main()
