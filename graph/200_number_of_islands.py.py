# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # depth first search 

        if not grid: return False

        def dfs_helper(grid: List[List[str]], i: int, j: int):

            # check index out of bound situation
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return

            # reach the ocean area
            if grid[i][j] == '0': return
            grid[i][j] = '0'

            # check up
            dfs_helper(grid, i-1, j)

            # check down
            dfs_helper(grid, i+1, j)

            # check left
            dfs_helper(grid, i, j-1)

            # check right
            dfs_helper(grid, i, j+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    dfs_helper(grid, i, j)

        return count

