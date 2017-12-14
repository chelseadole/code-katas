"""Write a function sort_cards() that sorts a shuffled list of cards, so that any given list of cards
is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
"""

import itertools


def sort_cards(lst):
    """Sort a shuffled list of cards."""
    all_nums = [i for i in lst if i.isdigit()]
    all_a = [i for i in lst if i.upper() == 'A']
    all_t = [i for i in lst if i.upper() == 'T']
    all_j = [i for i in lst if i.upper() == 'J']
    all_q = [i for i in lst if i.upper() == 'Q']
    all_k = [i for i in lst if i.upper() == 'K']
    output = itertools.chain(all_a, sorted(all_nums), all_t, all_j, all_q, all_k)
    return list(output)