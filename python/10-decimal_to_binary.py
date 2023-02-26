#!/usr/bin/env python3

def _decimalToBinary(num: int, result: str) -> str:
    """Converts a decimal number to a binary string

    Args:
        num (int): decimal number to convert
        result (str): string where the result is returned

    Returns:
        str: result string
    """
    if num == 0:
        return result
    result = f"{num % 2}" + result
    return _decimalToBinary(num // 2, result)


def decimalToBinary(num: int) -> str:
    """Converts a decimal number to a binary string

    Args:
        num (int): decimal number to convert

    Returns:
        str: result string binary representation
    """
    return _decimalToBinary(num, '')


print([decimalToBinary(el) for el in range(11)])
