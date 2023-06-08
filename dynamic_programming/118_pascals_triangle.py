# https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows <= 0: return []

        dp = [[1]] * numRows
        for i in range(1, numRows):
            temp = [1] * (i+1)
            for j in range(len(temp)):
                if j != 0 and j != len(temp) - 1:
                    temp[j] = dp[i-1][j-1] + dp[i-1][j]
            dp[i] = temp

        return dp



            




