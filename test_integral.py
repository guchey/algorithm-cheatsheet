# -*- coding: utf8 -*-

import unittest


def is_prime(value):
    """
    最悪計算時間: O(root(n))
    """
    if value == 1:
        return False
    i = 2
    while i * i <= value:
        if value % i == 0:
            return False
        i += 1
    return True


class TestIntegral(unittest.TestCase):

    def test_is_prime(self):
        # Arrange

        # Act

        # Assert
        assert is_prime(59) is True
        assert is_prime(57) is False


if __name__ == '__main__':
    unittest.main()
