#!/usr/bin/env python3
"""Find a number using binary search with recursion
    """
from typing import List


def _binary_search(nums: List[int], l: int, r: int, target: int) -> int:
    """Find the index of the searched number

    Args:
        nums (List[int]): list to look into
        l (int): left index of the list to search
        r (int): right index of the list to search
        target (int): value to find

    Returns:
        int: index of the searched number
    """
    if r < l:
        return -1
    middle_index = (l + r) // 2
    if nums[middle_index] == target:
        return middle_index
    if nums[middle_index] < target:
        return _binary_search(nums, middle_index + 1, r, target)
    return _binary_search(nums, l, middle_index - 1, target)


def binary_search(nums: List[int], target: int) -> int:
    """Find the index of the searched number
    Args:
        nums (List[int]): list to look into
        target (int): value to find
    Returns:
        int: index of the value
    """
    return _binary_search(nums, 0, len(nums) - 1, target)


print(binary_search([1, 10, 15, 20, 35, 55, 90], 10))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 90))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 100))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 20))
print(binary_search([1, 10, 15, 20, 35, 55, 90], 15))
