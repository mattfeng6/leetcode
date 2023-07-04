# https://leetcode.com/problems/sum-of-left-leaves/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root: return 0
        if not root.left and not root.right: return 0

        leftVal = self.sumOfLeftLeaves(root.left)
        rightVal = self.sumOfLeftLeaves(root.right)
        
        # node have a left child which is a leaf
        if root.left and not root.left.left and not root.left.right:
                leftVal = root.left.val

        return leftVal + rightVal
        