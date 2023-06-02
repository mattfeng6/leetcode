# https://leetcode.com/problems/clone-graph/

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:

        if not node: return node

        dict = {node.val: Node(node.val, [])}

        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor.val not in dict:
                    dict[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)

                dict[curr.val].neighbors.append(dict[neighbor.val])
        return dict[node.val]