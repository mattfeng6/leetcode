# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        record = dict()

        for value in nums:
            record[value] = record.get(value, 0) + 1
        
        return max(record, key=record.get)

        # Moore's Voting Algorithm

        # solution = None
        # count = 0
        # for i in nums:
        #     if count == 0:
        #         solution = i
        #     count += (1 if i == solution else -1)
        # return solution

        # Sorting

        # nums = sorted(nums)
        # return nums[len(nums) // 2]