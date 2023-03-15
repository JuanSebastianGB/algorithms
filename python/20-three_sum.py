#!/usr/bin/env python3

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for index in range(len(nums) - 1):
        if index > 0 and nums[index - 1] == nums[index]:
            continue
        l, r = index + 1, len(nums) - 1
        while l < r:
            _sum = nums[index] + nums[l] + nums[r]
            if _sum > 0:
                r -= 1
            elif _sum < 0:
                l += 1
            else:
                res.append([nums[index], nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
    return res
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0]))
print(threeSum([0, 1, 1]))