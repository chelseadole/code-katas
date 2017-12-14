"""Proper parenthetics extra credit kata."""


def proper_parenthetics(string):
    """Return if parentheses are matching or not."""
    paren_list = list(string)
    opening_parens = 0
    closing_parens = 0
    import pdb; pdb.set_trace()
    for i in paren_list:
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
