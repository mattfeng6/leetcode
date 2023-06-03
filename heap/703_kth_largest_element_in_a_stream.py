# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = heapq.nlargest(k, nums)
        heapq.heapify(nums)
        self.heap = nums
        self.k = k


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)