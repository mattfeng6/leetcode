# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        count = 0
        if not citations: return count
        
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i+1:
                count = i+1

        return count
