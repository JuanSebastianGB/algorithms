#!/usr/bin/env python3

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
you may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """_summary_

    Args:
        nums (List[int]): nums to check for sum
        target (int): target sum

    Returns:
        List[int]: list of indices that sum to target
    """
    index_store = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in index_store:
            return[index_store[diff], index]
        index_store[value] = index
    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([3, 3, 4], 7))
