from atcoder import template
import pytest


class TestTemplate(object):

    @pytest.mark.parametrize("n,expected", [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
    ])
    def test_isprime(self, n, expected):
        # Arrange

        # Act
        actual = template.isprime(n)

        # Assert
        assert actual is expected

    @pytest.mark.parametrize("a,b,expected", [
        (3, 10, True),
        (3, 6, False),
    ])
    def test_coprime(self, a, b, expected):
        # Arrange

        # Act
        actual = template.coprime(a, b)

        # Assert
        assert actual is expected

    @pytest.mark.parametrize("n,expected", [
        ((12, 18, 36), 6),
        ((2, 3), 1),
    ])
    def test_gcd(self, n, expected):
        # Arrange

        # Act
        actual = template.gcd(*n)

        # Assert
        assert actual == expected

    @pytest.mark.parametrize("n,expected", [
        ((4, 6, 2), 12),
        ((2, 3), 6),
    ])
    def test_lcm(self, n, expected):
        # Arrange

        # Act
        actual = template.lcm(*n)

        # Assert
        assert actual == expected

    def test_bitsearch(self):
        # Arrange

        # Act
        actual = template.bitsearch([1, 2, 3])

        # Assert
        assert list(actual) == [[], [1], [2], [1, 2],
                                [3], [1, 3], [2, 3], [1, 2, 3]]

    @pytest.mark.parametrize("w,n,expected", [
        (4, [1, 2, 3, 4], True),
        (100, [1, 2, 3, 4], False),
    ])
    def test_recursivesearch(self, w, n, expected):
        # Arrange

        # Act
        actual = template.recursivesearch(w, n)

        # Assert
        assert actual is expected

    def test_fibo(self):
        # Arrange

        # Act
        actual = template.fibo(10)

        # Assert
        assert actual == 55

    def test_dppush(self):
        # Arrange

        # Act
        actual = template.dppush([2, 9, 4, 5, 1, 6, 10])

        # Assert
        assert actual == 8

    def test_dpknapsack(self):
        # Arrange

        # Act
        actual = template.dpknapsack(
            15, [(2, 3), (1, 2), (3, 6), (2, 1), (1, 3), (5, 85)])

        # Assert
        assert actual == 0
