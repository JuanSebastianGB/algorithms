#!/usr/bin/env python3
"""Container with most water using 2 pointer algorithm
    """

from typing import List


def maxArea(heights: List[int]) -> int:
    """it returns the max area of the container

    Args:
        heights (List[int]): heights of the container

    Returns:
        int: max area
    """
    l, r, max_area = 0, len(heights) - 1, 0
    while l < r:
        width = r - l
        height = min(heights[r], heights[l])
        max_area = max(width * height, max_area)
        if heights[r] < heights[l]:
            r -= 1
        else:
            l += 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([4, 3, 2, 1, 4]))
print(maxArea([1, 2, 1]))
print(maxArea([1, 2, 4, 3]))
print(maxArea([1, 2, 4, 3, 2, 1]))
print(maxArea([1, 2, 4, 3, 2, ]))
