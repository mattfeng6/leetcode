# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        while n:
            if n & 1:
                return not (n>>1)
            n >>= 1
            
        return False

    
