#!/usr/bin/env python3
"""Find a number using binary search with loops
    """
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Find the index of the searched number
    Args:
        nums (List[int]): list to look into
        target (int): value to find
    Returns:
        int: index of the value
    """
    middle, l, r = 0, 0, len(nums) - 1
    while l <= r:
        middle = (l + r) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            l = middle + 1
        else:
            r = middle - 1
    return -1


print(binary_search([1, 10, 15, 20, 35, 55, 90], 10))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 90))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 100))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 20))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 15))
