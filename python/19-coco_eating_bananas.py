#!/usr/bin/env python3

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
import math
from typing import List
def minEatingSpeed(piles: List[int], h: int) -> int:
    """Find the min speed needed to eat all bananas

    Args:
        piles (List[int]): list with a pile of bananas in each position
        h (int): limit of hours

    Returns:
        int: min speed
    """
    elections = range(max(piles) + 1)
    l, r = 0, len(elections) - 1
    result = r
    while l <= r:
        m = (l + r) // 2
        hours = 0
        for el in piles:
            hours += math.ceil(el / m)
        if hours <= h:
            result = min(result, elections[m])
            r = m - 1
        else:
            l = m + 1
    return result

print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))
print(minEatingSpeed([3,6,7,11], 8))