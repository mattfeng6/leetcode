# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        list = set()
        for num1 in nums1:
            list.add(num1)

        for num2 in nums2:
            if num2 in list:
                res.append(num2)

        return set(res)
    
        # return list(set(nums1) & set(nums2))