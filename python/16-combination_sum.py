#!/usr/bin/env python3

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

from typing import List


def combinationSum(nums: List[int], target: int):
    data = []

    def dfs(i: int, cur: List[int], total: int):
        if target == total:
            return data.append(cur[:])
        if i >= len(nums) or total > target:
            return

        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        cur.pop()
        dfs(i + 1, cur, total)
    dfs(0, [], 0)
    return data


print(combinationSum([1, 2, 3, 4, 5], 7))
print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print(combinationSum([2], 1))
print(combinationSum([1], 1))
print(combinationSum([2, 3, 6, 7], 7))
