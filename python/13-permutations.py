#!/usr/bin/env python3
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """Generate all permutations of a list

    Args:
        nums (List[int]): List of integers to find permutations

    Returns:
        List[List[int]]: all permutations of the list
    """
    results = []

    if len(nums) == 1:  # base condition,that is, when the list has only one element
        return [nums[:]]
    for i in range(len(nums)):
        p = nums.pop(i)  # remove the element at index i
        permutations = permute(nums)
        # append the removed element to all the permutations
        [el.append(p) for el in permutations]
        results.extend(permutations)
        nums.append(p)  # add the removed element back to the list
    return results


print(permute([1, 2, 3]))
print(permute([1]))
print(permute([1, 2]))
