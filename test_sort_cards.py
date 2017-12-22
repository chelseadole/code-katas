"""Testing module for sort_cards."""

import pytest
from sort_cards import sort_cards
import random

sorted_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']


def test_sort_cards_empty_lst():
    """Sort_card with empty list as input."""
    assert sort_cards([]) == []


def test_sort_cards_on_list_len_1_num():
    """Sort_card on list with just one num."""
    assert sort_cards(['1']) == ['1']


def test_sort_cards_on_list_len_1_letter():
    """Sort_card on list with just one num."""
    assert sort_cards(['A']) == ['A']


def test_sort_cards_list_all_nums():
    """Sort_card on list that is all numbers."""
    assert sort_cards(['3', '2', '7', '9', '8', '4']) == ['2', '3', '4', '7', '8', '9']


def test_sort_cards_list_all_letters():
    """Sort_card on list that is all letters."""
    assert sort_cards(['J', 'K', 'A', 'Q']) == ['A', 'J', 'Q', 'K']


@pytest.mark.parameterize("shuffled_deck, output", [
    (random.shuffle(sorted_deck), sorted_deck) for i in range(100)
])
def parameterized_shuffled_decks(shuffled_deck, output):
    """100 randomly shuffled decks."""
    assert sort_cards(shuffled_deck) == output
