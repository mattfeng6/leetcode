# https://leetcode.com/problems/all-paths-from-source-to-target/

# https://leetcode.com/problems/all-paths-from-source-to-target/solutions/118691/c-python-backtracking/

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # depth first search
        
        # Invalid Input
        if not graph: return []

        def dfs_helper(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs_helper(i, path + [i])
        
        res = []
        dfs_helper(0, [0])
        return res


