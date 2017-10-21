"""Tests for create_phone_number"""

import pytest


TEST_NUMS = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"),
    ([2, 0, 6, 9, 1, 4, 7, 0, 2, 1], "(206) 914-7021"),
    ([1, 5, 6, 3, 3, 0, 2, 1, 2, 7], "(156) 330-2127"),
    ([9, 9, 0, 3, 4, 4, 2, 6, 1, 2], "(990) 344-2612"),
    ([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], "(000) 010-0000"),
    ([6, 7, 4, 5, 2, 4, 1, 3, 4, 3], "(674) 524-1343")

]


@pytest.mark.parametrize('n, result', TEST_NUMS)
def test_create_phone_number(n, result):
    from create_phone_number_6kyu import create_phone_number
    assert create_phone_number(n) == result
