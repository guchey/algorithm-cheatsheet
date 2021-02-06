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


def enum_divisors(value):
    """
    約数列挙
    """
    result = set()
    i = 1
    while i * i <= value:
        if value % i == 0:
            result.add(i)
            result.add(value // i)
        i += 1
    return sorted(result)


def calc_digit(value):
    """
    桁数カウント
    """
    result = 0
    while value:
        result += 1
        value //= 10
    return result


class TestIntegral(unittest.TestCase):

    def test_is_prime(self):
        # Arrange

        # Act

        # Assert
        assert is_prime(59) is True
        assert is_prime(57) is False

    def test_enum_divisors(self):
        # Arrange
        testdata = 100
        expected = [1, 2, 4, 5, 10, 20, 25, 50, 100]

        # Act
        actual = enum_divisors(testdata)

        # Assert
        assert actual == expected

    def test_calc_digit(self):
        # Arrange
        testdata = 1239483459827059273
        expected = 19

        # Act
        actual = calc_digit(testdata)

        # Assert
        assert actual == expected


if __name__ == '__main__':
    unittest.main()
