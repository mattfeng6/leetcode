# https://leetcode.com/problems/merge-two-binary-trees/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None
        
        if not root1: return root2
        if not root2: return root1

        root3 = TreeNode(root1.val + root2.val)
        root3.left = self.mergeTrees(root1.left, root2.left)
        root3.right = self.mergeTrees(root1.right, root2.right)

        return root3