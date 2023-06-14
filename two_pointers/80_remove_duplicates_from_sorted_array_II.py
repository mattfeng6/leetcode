# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums: return False

        if len(nums) <= 2: return len(nums)

        left, right = 2, 2
        while right < len(nums):
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left

