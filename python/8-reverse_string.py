#!/usr/bin/env python3

def reverse_string(string: str) -> str:
    """Implements reverse_string with recursion support
    Args:
        string: string to reverse
    Returns:
        str: string reversed
    """
    if string == '':
        return string
    return reverse_string(string[1:]) + string[0]


print(reverse_string("Hello world"))
print(reverse_string("Reversed"))
print(reverse_string("Reversed string"))
