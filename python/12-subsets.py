#!/usr/bin/env python3
"""
Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Create all subsets, that are not permutation

    Args:
        nums (List[int]): list of integers

    Returns:
        List[List[int]]: subsets
    """
    result, subset = [], []

    def dfs(i):
        if i >= len(nums):
            result.append(subset[:])
            return
        subset.append(nums[i])
        dfs(i + 1)  # add
        subset.pop()
        dfs(i + 1)  # not add
    dfs(0)
    return result


print(subsets([]))
print(subsets([1]))
print(subsets([1, 2]))
print(subsets([1, 2, 3]))
