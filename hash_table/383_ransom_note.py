# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mapping = {}

        for charMag in magazine:
            mapping[charMag] = mapping.get(charMag, 0) + 1

        for charRan in ransomNote:
            if charRan not in mapping or mapping[charRan] == 0:
                return False
            mapping[charRan] -= 1

        return True