# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res, Set = 0, set()

        for num in nums:
            Set.add(num)
        
        for i in range(len(nums)):
            count = 1
            curr = nums[i]
            
            while curr - 1 in Set:
                curr -= 1
                Set.remove(curr)
                count += 1

            curr = nums[i]
            while curr + 1 in Set:
                curr += 1
                Set.remove(curr)
                count += 1

            res = max(res, count)
        return res
            

            
        



