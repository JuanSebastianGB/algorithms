#!/usr/bin/env python3
"""
Given an integer array nums, find the sub array with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The sub array [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The sub array [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The sub array [5,4,-1,7,8] has the largest sum 23.
"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
    """Find the largest sum of the given number of sub arrays

    Args:
        nums (List[int]): List of integers to find the largest sum

    Returns:
        int: largest sum of the given number of sub arrays
    """
    _sum, _max = 0, nums[0]

    for el in nums:
        if _sum < 0:
            _sum = 0
        _sum += el
        _max = max(_sum, _max)
    return _max


print(maxSubArray([5, 4, -1, 7, 8]))
print(maxSubArray([1]))
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
