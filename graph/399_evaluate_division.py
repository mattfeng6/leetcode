# https://leetcode.com/problems/evaluate-division/
# https://www.youtube.com/watch?v=Uei1fwDoyKk

from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # graph

        res = []

        # Invalid Input
        if not equations or not values or not queries:
            return res
        
        # Length of two arrays does not match
        if len(equations) != len(values):
            return res 
        
        graph = collections.defaultdict(dict)
        for i, equation in enumerate(equations):
            first, second = equation
            graph[first][second] = values[i]
            graph[second][first] = 1 / values[i]

        def dfs_helper(curr, final, visited):

            # invalid input
            if curr not in graph or final not in graph:
                return float(-1)

            # relationship already in equations
            if final in graph[curr]:
                return graph[curr][final]
            
            for next in graph[curr]:
                if next not in visited:
                    visited.add(next)
                    temp = dfs_helper(next, final, visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[curr][next] * temp 
            
            return -1
        
        for query in queries:
            res.append(dfs_helper(query[0], query[1], set()))

        return res

# BlackRock