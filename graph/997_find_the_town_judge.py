# https://leetcode.com/problems/find-the-town-judge/

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # consider trust as a graph, all pairs are directed edge
        # in-degree - out-degree = n - 1

        trust_rate = [0] * (n+1)

        for left, right in trust:
            trust_rate[left] -= 1
            trust_rate[right] += 1

        for i in range(1, n+1):
            if trust_rate[i] == n - 1:
                return i
            
        return -1
