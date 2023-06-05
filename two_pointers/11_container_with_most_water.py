# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        currVolumn, maxVolumn = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            currVolumn = min(height[left], height[right]) * (right - left)
            maxVolumn = max(maxVolumn, currVolumn)

            if height[left] < height[right]: left += 1
            else: right -= 1

        return maxVolumn
