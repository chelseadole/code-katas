"""Kata: Descending Order - Take any non-negative int and return with 
its digits in descending order.

#1 Best Practices Solution by laoris and 878 more
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
"""


def descending_order(num):
    num_lst = sorted(list(str(num)))[::-1]
    concat_result = ''
    for i in num_lst:
        concat_result += i
    return int(concat_result)
