"""Tests for binary_addition"""

import pytest


TEST_NUMS = [
    (0, 0),
    (15, 51),
    (123456789, 987654321),
    (1237, 7321),
    (99374, 99743),
    (9374, 9743),
    (23, 32),
    (791, 971),
    (100000, 100000)
]


@pytest.mark.parametrize('num, result', TEST_NUMS)
def test_descending_order(num, result):
    from descending_order_7kyu import descending_order
    assert descending_order(num) == result
