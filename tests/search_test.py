from unittest import TestCase

from algorithms import binary_search
from algorithms import linear_search


class TestSearchAlgorithms(TestCase):
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
