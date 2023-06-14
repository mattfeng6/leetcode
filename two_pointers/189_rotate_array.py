# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)

        def swap(nums: List[int], i: int, j: int) -> None:
            
            while i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1; j-= 1

        swap(nums, 0, len(nums) - 1)
        swap(nums, 0, k - 1)
        swap(nums, k, len(nums) - 1)
        
