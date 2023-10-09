from unittest import TestCase

from algorithms import binary_search
from algorithms import linear_search
from algorithms import bubble_sort
from algorithms import quick_sort
from algorithms import selection_sort


class TestAlgorithms(TestCase):
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
            msg='Must be None'
        )
        try:
            binary_search(test_list, 0, strict=True)
        except ValueError:
            pass

    def test_linear_search(self):
        test_list = [1, 4, 5, 10, 11, 14, 27, 34, 40]
        self.assertEqual(
            first=6,
            second=linear_search(test_list, 27),
            msg='Must be 6'
        )
        self.assertEqual(
            first=None,
            second=linear_search(test_list, 0),
            msg='Must be None'
        )
        try:
            linear_search(test_list, 0, strict=True)
        except ValueError:
            pass

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
