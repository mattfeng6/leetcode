# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def curDepth(root) -> int:
            if not root: return 0
            
            leftDepth = curDepth(root.left)
            rightDepth = curDepth(root.right)
            if leftDepth < 0 or rightDepth < 0 or abs(leftDepth - rightDepth) > 1:
                return -1
            return 1 + max(leftDepth, rightDepth)
        
        return curDepth(root) >= 0
        
