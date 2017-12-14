"""Proper parenthetics extra credit kata."""

from _que_structure import Q


def proper_parenthetics(string):
    """Return if parentheses are matching or not."""
    if isinstance(string, str):
        paren_q = Q(list(string))
        opening_parens = 0
        closing_parens = 0
        while paren_q.size() > 0:
            i = paren_q.dequeue().data
            if i != '(' and i != ')':
                raise TypeError('proper_parenthetics takes only parentheses.')
            if i == '(' and closing_parens == 0:
                opening_parens += 1
            elif i == '(' and closing_parens > 0:
                closing_parens -= 1
            elif i == ')' and opening_parens == 0:
                return -1
            elif i == ')' and opening_parens > 0:
                opening_parens -= 1
        if opening_parens - closing_parens == 0:
            return 0
        if opening_parens - closing_parens > 0:
            return 1
    raise TypeError('proper_parenthetics takes only strings')

