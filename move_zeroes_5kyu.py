"""Kata: Move Zeroes - Move all zeroes in list to end.

#1 Best Practices Solution by riyakayal

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
"""


def move_zeroes(array):
    all_zeroes = list(filter((lambda x: x == 0 and type(x) is not bool), array))
    non_zeroes = list(filter((lambda x: x != 0 or type(x) is bool), array))
    return non_zeroes + all_zeroes
