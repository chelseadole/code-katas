"""Kata: Reversed Words-Return a string of words, where the order is reversed.

#1 Best Practices Solution by CrazyMerlyn & others

def reverseWords(str):
    return " ".join(str.split(" ")[::-1])
"""


def reversewords(str):
    str_lst = str.split()[::-1]
    return_str = ''
    for item in str_lst:
        return_str += item + ' '
    return return_str.rstrip()
