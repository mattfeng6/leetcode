# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Base Case
        if root is None: return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left

        return root
       