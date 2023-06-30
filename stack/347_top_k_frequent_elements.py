# https://leetcode.com/problems/top-k-frequent-elements

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        ranking = []
        for key, value in mapping.items():
            heapq.heappush(ranking, (value, key))
            if len(ranking) > k:
                heapq.heappop(ranking)
            
        res = []
        for i in range(k):
            _, key = heapq.heappop(ranking)
            res.append(key)
        
        return res