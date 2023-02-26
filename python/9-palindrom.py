#!/usr/bin/env python3
"""Implementing palindrome verification with recursion
    """


def isPalindrome(string: str) -> bool:
    """Check if string is a palindrome

    Args:
        string (str): String to check

    Returns:
        bool: True if string is a palindrome else False
    """
    if len(string) in [0, 1]:
        return True
    if string[0] != string[-1]:
        return False
    return isPalindrome(string[1:-1])


print(isPalindrome("a"))
print(isPalindrome("ab"))
print(isPalindrome("aba"))
print(isPalindrome("abaaba"))
print(isPalindrome("aba125"))
print(isPalindrome("abasaba"))
print(isPalindrome("abasaba1"))
