# https://leetcode.com/problems/house-robber/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # Special Situation
        if not nums: return 0
        if len(nums) <= 2: return max(nums)

        dp = [0] * (len(nums) + 1)

        dp[1] = nums[0]
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])

        return dp[len(nums)]