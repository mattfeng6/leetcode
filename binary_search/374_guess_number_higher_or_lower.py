# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution:
    def guessNumber(self, n: int) -> int:

        def guess(num: int) -> int:
            return 1
        
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1