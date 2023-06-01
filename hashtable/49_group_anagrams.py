# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(str)
        
        return res.values()