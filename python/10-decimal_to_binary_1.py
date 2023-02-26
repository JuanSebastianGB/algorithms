#!/usr/bin/env python3
"""Decimal to binary using loops
    """


def decimalToBinary(num: int) -> str:
    """Converts a decimal number to a binary string

    Args:
        num (int): decimal number to convert

    Returns:
        str: result string
    """
    result = ''
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result[::-1]


print([decimalToBinary(el) for el in range(11)])
