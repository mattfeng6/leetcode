# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # If length does not equal,
        # strings will not be isomorphic
        if len(s) != len(t):
            return False
        
        s2t, t2s = {}, {}

        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
    
    # https://leetcode.com/problems/isomorphic-strings/solutions/1337259/2-liner-with-99-efficiency-and-explanation/

    # zip function

    # zipped_set = set(zip(s, t))
    # return len(zipped_set) == len(set(s))
