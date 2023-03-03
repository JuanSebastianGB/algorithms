#!/usr/bin/env python3
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List


def canJump(nums: List[int]) -> bool:
    """define if with the steps given in the list you can reach the last index

    Args:
        nums (List[int]): List of integers to define if you can reach the last index

    Returns:
        bool: true if you can reach the last index, false otherwise
    """
    goal = len(nums) - 1
    for el in range(goal, -1, -1):
        if el + nums[el] >= goal:
            goal = el
    return goal == 0


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([2, 0]))
