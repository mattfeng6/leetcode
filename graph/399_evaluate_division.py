# https://leetcode.com/problems/evaluate-division/

from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        res = []

        # Invalid Input
        if not equations or not values or not queries:
            return res
        
        # Length of two arrays does not match
        if len(equations) != len(values):
            return res
        
        # TODO
        return res

