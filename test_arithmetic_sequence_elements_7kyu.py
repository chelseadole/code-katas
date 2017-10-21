"""Tests for arithmetic_sequence_elements kata"""

import pytest


TEST_SEQUENCES = [
    (1, 2, 5, '1, 3, 5, 7, 9'),
    (1, -3, 10, '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'),
    (50, 2, 5, '50, 52, 54, 56, 58'),
    (17, -1, 3, '17, 16, 15'),
    (0, 50, 8, '0, 50, 100, 150, 200, 250, 300, 350'),
    (8, 3, 3, '8, 11, 14')
]


@pytest.mark.parametrize('a, r, n, result', TEST_SEQUENCES)
def test_arithmetic_sequence_elements(a, r, n, result):
    from arithmetic_sequence_elements_7kyu import arithmetic_sequence_elements
    assert arithmetic_sequence_elements(a, r, n) == result
