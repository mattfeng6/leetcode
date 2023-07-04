# https://leetcode.com/problems/find-bottom-left-tree-value/

from typing import Optional
from TreeNode import TreeNode

from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # Invalid Input
        if not root: return -1

        leftValue = root.val

        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)

            for i in range(length):
                temp = queue.popleft()
                if i == 0:
                    leftValue = temp.val
                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)

        return leftValue
                    

