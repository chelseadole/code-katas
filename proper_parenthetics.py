"""Proper parenthetics extra credit kata."""


def proper_parenthetics(string):
    """Return if parentheses are matching or not."""
    if isinstance(string, str):
        paren_list = list(string)
        opening_parens = 0
        closing_parens = 0
        for i in paren_list:
            # import pdb; pdb.set_trace()
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
