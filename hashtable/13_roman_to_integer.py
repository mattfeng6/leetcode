# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        # I: 1
        # V: 5
        # X: 10
        # L: 50
        # C: 100
        # D: 500
        # M: 1000

        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:
            res += translations[char]
        return res
        
            