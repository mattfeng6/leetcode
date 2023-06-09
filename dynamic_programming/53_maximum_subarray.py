# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums: return 0

        prefix = [0] * len(nums)
        maxValue = prefix[0] = nums[0]

        for i in range(1, len(prefix)):
            prefix[i] = max(prefix[i-1] + nums[i], nums[i])
            maxValue = max(maxValue, prefix[i])

        return maxValue
