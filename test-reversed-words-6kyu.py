"""Tests for reversedwords kata"""

import pytest


REV_STRINGS = [
    ("Alas, poor Yorick", "Yorick poor Alas,"),
    ("Chelsea Fay Dole", "Dole Fay Chelsea"),
    ("Once upon a time!", "time! a upon Once"),
    ("Hello goodbye, is the saying", "saying the is goodbye, Hello")
]


@pytest.mark.parametrize('n, result', REV_STRINGS)
def test_reversed_words(n, result):
    """Test if series imports."""
    from reversed_words import reversewords
    assert reversewords(n) == result
