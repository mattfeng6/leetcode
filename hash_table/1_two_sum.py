# https://leetcode.com/problems/two-sum/

from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Function 1 : Dictionary
        records = dict()
        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index] # Return the indices of the two numbers that sum up to target
            records[value] = index
        return [] # Return an empty list if no two numbers sum up to the target value
    
        # Function 2 : Set
        # seen = set()       
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in seen:
        #         return [nums.index(complement), i]
        #     seen.add(num)