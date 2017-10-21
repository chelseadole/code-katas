"""Kata: Is Triangle - see if 3 side lengths can create a triangle.

#1 Best Practices Solution by Kamyk

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
"""


def is_triangle(a, b, c):
    max_num = max(a, b, c)
    all_sum = a + b + c
    if all_sum - max_num >= max_num + 1:
        return True
    else:
        return False
