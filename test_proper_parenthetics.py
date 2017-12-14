"""Test suite for proper parenthetics kata."""

import pytest
from proper_parenthetics import proper_parenthetics


def test_pp_empty_str():
    """Test on empty string as input."""
    assert proper_parenthetics('') == 0


def test_pp_on_list():
    """Test pp doesnt take list."""
    with pytest.raises(TypeError):
        assert proper_parenthetics([1, 2, 3])


def test_string_with_non_paren_elements():
    """Test input string where not all elems are parens."""
    with pytest.raises(TypeError):
        assert proper_parenthetics('((7)1')


def test_pp_with_zero_balance():
    """Test input string of balanced parens."""
    assert proper_parenthetics('(())()') == 0


def test_pp_with_neg_1_imbalance():
    """Test broken input string, closing paren has no opener."""
    assert proper_parenthetics('())()') == -1


def test_pp_with_pos_1_imbalance():
    """Test open input string, opening paren has no closer."""
    assert proper_parenthetics('()(())(') == 1
