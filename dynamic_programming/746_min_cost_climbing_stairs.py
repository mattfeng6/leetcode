# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if not cost: return 0

        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[len(cost)]




