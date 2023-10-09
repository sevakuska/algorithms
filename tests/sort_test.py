from unittest import TestCase

from algorithms import bubble_sort
from algorithms import quick_sort
from algorithms import selection_sort


class TestSortAlgorithms(TestCase):
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
