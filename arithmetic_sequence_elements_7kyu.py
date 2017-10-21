"""Kata: Arithmetic Sequence - Return set of numbers defined by
length (n), step(r), and start number(a)

#1 Best Practices Solution by CrazyMerlyn & others

def opposite(number):
    return -number
"""


def arithmetic_sequence_elements(a, r, n):
    sequence = str(a) + ', '
    for rep in range(n - 1):
        sequence += str((a + r)) + ', '
        a += r
    return sequence[:len(sequence) - 2]
