#!/usr/bin/env python3
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    """NQueens Solution with backtracking

    Args:
        n (int): Dashboard size

    Returns:
        List[List[str]]: Dashboard with queens
    """
    pDiag = set()
    nDiag = set()
    columnVisited = set()
    result = []
    board = [['.'] * n for _ in range(n)]

    def dfs(row: int):
        if row == n:
            result.append(["".join(col) for col in board])
            return
        for column in range(n):
            if column in columnVisited or (row + column) in pDiag or (row - column) in nDiag:
                continue
            columnVisited.add(column)
            pDiag.add(row + column)
            nDiag.add(row - column)
            board[row][column] = "Q"

            dfs(row + 1)

            columnVisited.remove(column)
            pDiag.remove(row + column)
            nDiag.remove(row - column)
            board[row][column] = "."
    dfs(0)
    return result


print(solveNQueens(1))
print(solveNQueens(4))
print(solveNQueens(5))
print(solveNQueens(6))
