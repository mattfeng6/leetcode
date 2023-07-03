# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        count = 0

        if not root: return count

        stack = []
        stack.append(root)

        while stack:
            length = len(stack)
            for _ in range(length):
                temp = stack.pop()
                count += 1
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)

        return count
    
        # if not root: return 0
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    