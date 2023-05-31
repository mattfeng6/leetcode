from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        Set = set()
        for index, num in enumerate(nums):
            # remove the front element to control the length
            if index > k:
                Set.remove(nums[index - k - 1])
            
            # find the duplicate
            if num in Set: return True
            Set.add(num)
        return False




