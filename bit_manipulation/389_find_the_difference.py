# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        res = 0
        for i in range(len(s)):
            res ^= ord(s[i]) ^ ord(t[i])

        res ^= ord(t[-1])
        return chr(res)
