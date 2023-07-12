# https://leetcode.com/problems/reverse-bits/
# https://www.youtube.com/watch?v=UcoN6UjAI64&ab_channel=NeetCode
# https://leetcode.com/problems/reverse-bits/solutions/54738/sharing-my-2ms-java-solution-with-explanation/

class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1

        return res