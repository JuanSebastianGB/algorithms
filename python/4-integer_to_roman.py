#!/usr/bin/env python3

equivalence = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
_sorted = dict(sorted(equivalence.items(), key=lambda x: x[1], reverse=True))


def intToRoman(num: int) -> str:
    """converts an int to a roman string

    Args:
        num (int): number to convert

    Returns:
        str: roman string
    """
    result = ''
    for symbol, value in _sorted.items():
        while num >= value:
            result += symbol
            num -= value
    return result


print(intToRoman(5))
print(intToRoman(100))
print(intToRoman(1000))
print(intToRoman(550))
print(intToRoman(9))
print(intToRoman(800))
