# https://leetcode.com/problems/sliding-window-maximum/
# https://leetcode.com/problems/sliding-window-maximum/solutions/3491147/python-decreasing-deque-with-comments-beats-96/

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        res = []

        for r in range(len(nums)):
            
            # remove all eles less than curr
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            # if window not full then continue adding elements
            if r + 1 < k: continue

            if queue[0] < r+1-k: queue.popleft()

            res.append(nums[queue[0]])

        return res


        # 跑不了太大的数

        # res = []

        # def findMaxIndexValue(nums, left, right):
        #     max_idx, max_val = left, nums[left]
        #     for i in range(left, right + 1):
        #         if nums[i] > max_val:
        #             max_idx, max_val = i, nums[i]

        #     return max_idx, max_val

        # max_idx, max_val = findMaxIndexValue(nums, 0, k-1)
        # res.append(max_val)
        
        # for left in range(1, len(nums) - k + 1):
        #     right = left + k - 1

        #     # Check new element
        #     new_idx, new_val = right, nums[right]
        #     if new_val > max_val:
        #         max_idx, max_val = new_idx, new_val


        #     # Check removed element
        #     if max_idx < left:
        #         max_idx, max_val = findMaxIndexValue(nums, left, right)

        #     res.append(max_val)
        
        # return res
