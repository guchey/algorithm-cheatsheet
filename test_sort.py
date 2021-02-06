# -*- coding: utf8 -*-

import copy
import unittest


def bubble_sort(arr):
    """
    最悪計算時間: O(n^{2})
    最良計算時間: O(n)
    平均計算時間: O(n^{2})
    最悪空間計算量: O(1) auxiliary
    """
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            a, b = arr[j], arr[j-1]
            if a < b:
                arr[j], arr[j-1] = b, a


def shaker_sort(arr):
    """
    最悪計算時間: O(n^{2})
    """
    top_index = 0
    bot_index = len(arr) - 1
    while True:
        last_swap_index = top_index
        for i in range(top_index, bot_index):
            a, b = arr[i], arr[i+1]
            if a > b:
                arr[i], arr[i+1] = b, a
                last_swap_index = i
        bot_index = last_swap_index
        if top_index == bot_index:
            break
        last_swap_index = bot_index
        for i in reversed(range(top_index, bot_index)):
            a, b = arr[i], arr[i+1]
            if a > b:
                arr[i], arr[i+1] = b, a
                last_swap_index = i
        top_index = last_swap_index
        if top_index == bot_index:
            break


testdata = [1, 45, 3, 123, 5, 7, 3, 2, 7, 8, 3, 2, 21, 5, 47, 6,
            8, 5, 898, 42354, 23, 134, 234, 63, 745, 74, 68, 5, 23, 42, 42]
expected = sorted(testdata)


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        # Arrange
        acutual = copy.copy(testdata)

        # Act
        bubble_sort(acutual)

        # Assert
        self.assertEqual(acutual, expected)

    def test_shaker_sort(self):
        # Arrange
        acutual = copy.copy(testdata)

        # Act
        shaker_sort(acutual)

        # Assert
        self.assertEqual(acutual, expected)


if __name__ == '__main__':
    unittest.main()
