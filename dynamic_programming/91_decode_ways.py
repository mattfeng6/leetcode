# https://leetcode.com/problems/decode-ways/
# https://leetcode.com/problems/decode-ways/solutions/2644238/leetcode-the-hard-way-explained-line-by-line/

class Solution:
    def numDecodings(self, s: str) -> int:

        # special situation:
        # s == null or s starts with '0'
        if not s or int(s[0]) == 0:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if int(s[i-1]) != 0:
                dp[i] = dp[i-1]
            if i >= 2 and 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
