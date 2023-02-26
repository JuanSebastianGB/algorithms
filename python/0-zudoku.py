#!/usr/bin/env python3

"""Sudoku solver."""

from typing import List
SUDOKU = [
    [6, 0, 0, 7, 9, 0, 2, 0, 8],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 4, 0, 6, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 2, 8, 0, 7],
    [8, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 7, 0, 0, 4, 0],
    [4, 0, 0, 0, 2, 0, 6, 0, 9],
    [0, 0, 1, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],

]


def is_valid(sudoku: List[List[int]], n: int, i: int, j: int):
    """Find if the number is valid in the given row, column and segment.

    Args:
        sudoku (List[List[int]]): _description_
        n (int): number from 1 to 9
        i (int): elements in row
        j (int): elements in column

    Returns:
        bool: True if the number is valid else False
    """
    row = sudoku[i]
    column = [el[j] for el in sudoku]
    segment = [sudoku[a][b] for a in range(9) for b in range(
        9) if a // 3 == i // 3 and b // 3 == j // 3]
    return n not in row and n not in column and n not in segment


def solve(sudoku: List[List[int]]) -> bool:
    """Solution of the sudoku.

    Args:
        sudoku (List[List[int]]): sudoku to solve

    Returns:
        bool: True if the sudoku is solved else False
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    if is_valid(sudoku, n, i, j):
                        sudoku[i][j] = n
                        if solve(sudoku):
                            return True
                        sudoku[i][j] = 0
                return False
    return True


solve(SUDOKU)
print(SUDOKU)
