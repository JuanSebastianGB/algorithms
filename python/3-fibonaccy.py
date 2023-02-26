#!/usr/bin/env python3
"""
Function that returns Fibonacci sequence
"""
from typing import List

cache = {0: 0, 1: 1}


def _fibonacci(n: int) -> int:
    """Generate fibonacci result

    Args:
        n (int): input number

    Returns:
        int: fibonacci result
    """

    if n in cache:
        return cache[n]
    cache[n] = _fibonacci(n - 1) + _fibonacci(n-2)
    return cache[n]


def _fibonacci_s(n: int) -> List[int]:
    """Generate a list with fibonacci results

    Args:
        n (int): limit to find fibonacci results

    Returns:
        _type_: fibonacci list
    """
    stack = []
    for el in range(n+1):
        stack.append(_fibonacci(el))
    return stack


print(_fibonacci_s(10))
print(_fibonacci_s(20))
print(_fibonacci_s(60))
