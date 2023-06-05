# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        Set = set()
        for num in nums:
            if num in Set:
                return True
            Set.add(num)
        return False
        
        # return len(set(nums)) != len(nums)