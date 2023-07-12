# https://leetcode.com/problems/counting-bits/
# https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:

        def countBit(num) -> int:
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        
        res = []
        for i in range(n+1):
            res.append(countBit(i))
        return res