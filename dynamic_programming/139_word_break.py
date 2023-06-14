# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break/solutions/43808/simple-dp-solution-in-python-with-description/

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if not s or not wordDict:
            return False
        
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for w in wordDict:
                if i >= len(w) and dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True

        return dp[-1]


        
        