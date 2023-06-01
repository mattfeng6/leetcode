# https://leetcode.com/problems/valid-sudoku/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    res += [(i, curr), (curr, j), (i // 3, j // 3, curr)]
        return len(res) == len(set(res))