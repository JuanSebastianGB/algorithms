#!/usr/bin/env python3

"""Implementing merge sort function
    """

from typing import List


def merge_sort(nums: List[int]) -> None:
    """merge sort implementation

    Args:
        nums (List[int]): list to sort
    """

    if len(nums) <= 1:
        return
    left_arr = nums[:len(nums)//2]
    right_arr = nums[len(nums)//2:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i, j, k = 0, 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            nums[k] = left_arr[i]
            i += 1
        else:
            nums[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        nums[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        nums[k] = right_arr[j]
        j += 1
        k += 1


list_to_test = [10, 1, 5, 50, 3, 5, 100, -1, -100] + [el for el in range(9)]

merge_sort(list_to_test)
print(list_to_test)
