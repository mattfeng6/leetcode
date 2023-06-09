# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res1, res2 = set(), set()

        for num1 in nums1:
            res1.add(num1)

        for num2 in nums2:
            res2.add(num2)

        return res1 & res2

        
