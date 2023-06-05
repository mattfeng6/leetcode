# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        record = dict()

        for value in nums:
            if value in record:
                record[value] += 1
            else:
                record[value] = 1
        
        return max(record, key=record.get)

        # Moore's Voting Algorithm

        # solution = None
        # count = 0
        # for i in nums:
        #     if count == 0:
        #         solution = i
        #     count += (1 if i == solution else -1)
        # return solution
    

