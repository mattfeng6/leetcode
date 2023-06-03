# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        res = []
        m, n, visited = len(nums1), len(nums2), set()
        if not m or not n: return res
        
        heap = [(nums1[0] + nums2[0], (0, 0))]
        for _ in range(min(m*n, k)):
            val, (i, j) = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] +nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))

        return res