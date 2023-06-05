# https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/246-strobogrammatic-number-easy.html

class Solution:
    def isStrobogrammatic(self, s: str, t: str) -> bool:
        
        # Special Situation: length not equal
        if len(s) != len(t): return False

        # 0 -> 0; 1 -> 1; 6 -> 9; 8 -> 8; 9 -> 6
        
        Dict = {'0': '0',
                '1': '1',
                '6': '9',
                '8': '8',
                '9': '6'}
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] not in Dict or s[right] not in Dict:
                return False
            if Dict[s[left]] != s[right]:
                return False
            left += 1; right += 1
        return True
