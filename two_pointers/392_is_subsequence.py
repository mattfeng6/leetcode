# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_index = 0

        for t_index in range(len(t)):
            if s_index == len(s): return True
            if s[s_index] == t[t_index]:
                s_index += 1

        return s_index == len(s)
