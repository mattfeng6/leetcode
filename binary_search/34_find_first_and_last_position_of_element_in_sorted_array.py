# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/14699/clean-iterative-solution-with-two-binary-searches-with-explanation/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1, -1]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if left >= len(nums) or nums[left] != target: return res
        else: res[0] = left

        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2 + 1
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid

        res[1] = right
        return res

            
        