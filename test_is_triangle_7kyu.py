"""Tests for is_triangle"""

import pytest


TEST_ARRAYS = [
    (1, 2, 2, True),
    (7, 2, 2, False),
    (1, 2, 3, False),
    (1, 3, 2, False),
    (3, 1, 2, False),
    (5, 1, 2, False),
    (1, 2, 5, False),
    (2, 1, 5, False),
    (4, 2, 3, True),
    (5, 1, 5, True),
    (2, 2, 2, True),
    (-1, 2, 3, False),
    (1, -2, 3, False),
    (1, 2, -3, False),
    (0, 2, 3, False),
    (5, 5, 5, True),
    (3, 5, 3, True),
    (2, 1, 1, False),
]


@pytest.mark.parametrize('a, b, c, result', TEST_ARRAYS)
def test_is_triangle(a, b, c, result):
    from is_triangle_7kyu import is_triangle
    assert is_triangle(a, b, c) == result
