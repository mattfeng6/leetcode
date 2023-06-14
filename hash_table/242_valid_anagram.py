# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        Dict = {}
        for char in s:
            if char in Dict:
                Dict[char] += 1
            else:
                Dict[char] = 1

        for char in t:
            if char not in Dict:
                return False
            if Dict[char] == 1:
                Dict.pop(char)
            else:
                Dict[char] -= 1

        return len(Dict) == 0
    
        # for idx in set(s):
        #     if s.count(idx) != t.count(idx):
        #         return False
        # return True
