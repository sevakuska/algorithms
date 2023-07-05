import unittest

import algorithms


class TestAlgorithms(unittest.TestCase):
    def test_binary_search(self):
        test_list = [1, 4, 5, 10, 11, 14, 27, 34, 40]
        self.assertEqual(
            first=6,
            second=algorithms.binary_search(test_list, 27),
            msg='Should be 6'
        )
        self.assertEqual(
            first=None,
            second=algorithms.binary_search(test_list, 0),
            msg='Should be -1'
        )

    def test_two_point(self):
        test_list = [-5, -3, 2, 3, 5, 7, 10, 16, 18, 20, 22, 27, 35]
        self.assertEqual(
            first=(-5, 20),
            second=algorithms.two_point(test_list, 15),
            msg='Should be (-5, 20)'
        )
        self.assertEqual(
            first=(None, None),
            second=algorithms.two_point(test_list, 31),
            msg='Should be (None, None)'
        )
    
    def test_recursive_sum(self):
        test_list = [-5, 4, 7, 9, 12]
        self.assertEqual(
            first=27,
            second=algorithms.recursive_sum(test_list),
            msg='Should be 27'
        )

    def test_find_smallest(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        self.assertEqual(
            first=5,
            second=algorithms.find_smallest(test_list),
            msg='Should be 5'
        )

    def test_selection_sort(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        sorted_list = [-2, 1, 15, 25, 27, 30, 40]
        self.assertEqual(
            first=sorted_list,
            second=algorithms.selection_sort(test_list),
            msg='Should be [-2, 1, 15, 25, 27, 30, 40]'
        )
    
    def test_quick_sort(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        sorted_list = [-2, 1, 15, 25, 27, 30, 40]
        self.assertEqual(
            first=sorted_list,
            second=algorithms.quick_sort(test_list),
            msg='Should be [-2, 1, 15, 25, 27, 30, 40]'
        )
    
    def test_bubble_sort(self):
        test_list = [30, 25, 40, 1, 15, -2, 27]
        sorted_list = [-2, 1, 15, 25, 27, 30, 40]
        self.assertEqual(
            first=sorted_list,
            second=algorithms.bubble_sort(test_list),
            msg='Should be [-2, 1, 15, 25, 27, 30, 40]'
        )


if __name__ == '__main__':
    unittest.main()
