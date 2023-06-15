# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid + 1
            else:
                right = mid - 1
            
        return right