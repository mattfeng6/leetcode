# https://leetcode.com/problems/triangle/

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle: return 0

        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])

        return dp[0]


        # dp = [triangle[0][0]]

        # for row in triangle:
        #     if len(row) == 1: continue
        #     temp = [0] * len(row)
        #     for i in range(len(row)):
        #         if i == 0:
        #             temp[i] = dp[i] + row[i]
        #         elif i == len(row) - 1:
        #             temp[i] = dp[i-1] + row[i]
        #         else:
        #             temp[i] = min(dp[i-1], dp[i]) + row[i]
        #     dp = temp
    
        # return min(dp)

