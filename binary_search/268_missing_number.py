# https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        missing = len(nums)

        for i in range(missing):
            missing ^= i
            missing ^= nums[i]

        return missing

        # if not nums: return 0

        # n = len(nums)
        # total = n * (n+1) // 2

        # for num in nums:
        #     total -= num

        # return total