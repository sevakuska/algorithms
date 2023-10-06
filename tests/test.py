import unittest

from algorithms.search.binary import binary_search
from algorithms.sort.bubble import bubble_sort
from algorithms.sort.quick import quick_sort
from algorithms.sort.selection import selection_sort


class TestAlgorithms(unittest.TestCase):
    def test_binary_search(self):
        test_list = [1, 4, 5, 10, 11, 14, 27, 34, 40]
        self.assertEqual(
            first=6,
            second=binary_search(test_list, 27),
            msg='Must be 6'
        )
        self.assertEqual(
            first=None,
            second=binary_search(test_list, 0),
            msg='Must be -1'
        )

    def test_selection_sort(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        sorted_list = [-2, 1, 15, 25, 27, 30, 40]
        self.assertEqual(
            first=sorted_list,
            second=selection_sort(test_list),
            msg='Must be [-2, 1, 15, 25, 27, 30, 40]'
        )

    def test_quick_sort(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        sorted_list = [-2, 1, 15, 25, 27, 30, 40]
        self.assertEqual(
            first=sorted_list,
            second=quick_sort(test_list),
            msg='Must be [-2, 1, 15, 25, 27, 30, 40]'
        )

    def test_bubble_sort(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        sorted_list = [-2, 1, 15, 25, 27, 30, 40]
        self.assertEqual(
            first=sorted_list,
            second=bubble_sort(test_list),
            msg='Must be [-2, 1, 15, 25, 27, 30, 40]'
        )


if __name__ == '__main__':
    unittest.main()
