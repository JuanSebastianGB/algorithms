#!/usr/bin/env python3

from typing import List


def find_partition(nums: List[int], left: int, right: int) -> int:
    """Find partition index

    Args:
        nums (List[int]): list to sort
        left (int): left index
        right (int): right index

    Returns:
        int: partition index
    """
    i = left
    j = right-1
    pivot = nums[right]

    while i < j:
        while i < right and nums[i] < pivot:
            i += 1
        while j > left and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]
    return i


def _quick_sort(nums: List[int], left: int, right: int) -> None:
    """implements quick sort algorithm

    Args:
        nums (List[int]): list to sort
        left (int): left index
        right (int): right index
    """
    if left >= right:
        return
    partition_index = find_partition(nums, left, right)
    _quick_sort(nums, left, partition_index - 1)
    _quick_sort(nums, partition_index + 1, right)


def quick_sort(nums: List[int]) -> None:
    """Implement sort in ascending order

    Args:
        nums (List[int]): list to sort
    """
    _quick_sort(nums, 0, len(nums) - 1)


list_to_test = [10, 1, 5, 50, 3, 5, 100, -1, -100, 25, 75, 90, 1, 2, 3, 4, 49]

quick_sort(list_to_test)
print(list_to_test)
