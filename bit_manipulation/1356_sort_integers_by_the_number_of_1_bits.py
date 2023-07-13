# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from typing import List
import heapq

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def countOnes(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            
            return count
        
        temp = []
        for num in arr:
            ones = countOnes(num)
            temp.append((ones, num))

        heapq.heapify(temp)

        res = []
        while temp:
            res.append(heapq.heappop(temp)[1])

        return res
        
# Chase 