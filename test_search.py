# -*- coding: utf8 -*-

import unittest


def linear_search(arr, value):
    """
    最悪計算時間: O(nm)
    """
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    else:
        return None


def binary_search(arr, value, imin=None, imax=None):
    """
    最悪計算時間: O(log2n)
    """
    imin = imin or 0
    imax = imax or len(arr)
    imid = imin + (imax - imin) // 2
    if arr[imid] > value:
        return binary_search(arr, value, imin, imid - 1)
    elif arr[imid] < value:
        return binary_search(arr, value, imid + 1, imax)
    else:
        return imid
    return None


testdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


class TestSearch(unittest.TestCase):

    def test_linear_search(self):
        # Arrange
        expected = 18

        # Act
        acutual = linear_search(testdata, 19)

        # Assert
        self.assertEqual(acutual, expected)

    def test_binary_search(self):
        # Arrange
        expected = 18

        # Act
        acutual = binary_search(testdata, 19)

        # Assert
        self.assertEqual(acutual, expected)


if __name__ == '__main__':
    unittest.main()
