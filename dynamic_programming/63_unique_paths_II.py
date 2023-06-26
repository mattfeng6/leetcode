# https://leetcode.com/problems/unique-paths-ii/

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else: break # elements after obstacle should have no path
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else: break

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]

