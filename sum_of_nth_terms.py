"""
Kata: sum_of_nth_terms-function which returns the sum of this series.
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16, etc.
"""


def series_sum(n):
    """Return sum of series up to nth term"""
    if n == 0:
        return "0.00"
    final_count, denominator = 1, 4
    for reps in range(n - 1):
        final_count += (1 / denominator)
        denominator += 3
    formatted_num = format(final_count, '.2f')
    return str(formatted_num)
