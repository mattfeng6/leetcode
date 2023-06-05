# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        Dict = {}
        words = s.split(" ")

        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False

        for i in range(len(pattern)):
            if pattern[i] in Dict:
                if Dict[pattern[i]] != words[i]:
                    return False
            else: Dict[pattern[i]] = words[i]
        
        return True
               