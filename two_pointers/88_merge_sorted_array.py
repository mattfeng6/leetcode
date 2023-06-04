# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not nums1 or not nums2:
            return nums1
        
        index1, index2 = m - 1, n - 1
        for indext in range(len(nums1))[::-1]:

            if index1 < 0:
                nums1[indext] = nums2[index2]
                index2 -= 1
            elif index2 < 0:
                return
            elif nums1[index1] < nums2[index2]:
                nums1[indext] = nums2[index2]
                index2 -= 1
            else:
                nums1[indext] = nums1[index1]
                index1 -= 1
                

