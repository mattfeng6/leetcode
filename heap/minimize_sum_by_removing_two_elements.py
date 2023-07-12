# https://www.geeksforgeeks.org/minimize-the-sum-calculated-by-repeatedly-removing-any-two-elements-and-inserting-their-sum-to-the-array/#

from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, arr: List[int]) -> int:

        res = 0

        while len(arr) > 1:
            temp = heapq.heappop(arr) + heapq.heappop(arr)
            res += temp
            heapq.heappush(arr, temp)

        return res
    
# Chase