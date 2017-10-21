"""Tests for binary_addition"""

import pytest


TEST_BINARIES = [
    (1, 0, "1"),
    (0, 1, "1"),
    (1, 1, "10"),
    (2, 2, "100"),
    (51, 12, "111111"),
    (16, 2, "10010"),
    (80, 10, "1011010"),
    (1000, 1000, "11111010000"),
    (97, 2, "1100011"),
    (2, 5, "111")
]


@pytest.mark.parametrize('a, b, result', TEST_BINARIES)
def test_binary_addition(a, b, result):
    from binary_addition_7kyu import add_binary
    assert add_binary(a, b) == result
