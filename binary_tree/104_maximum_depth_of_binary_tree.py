# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Base Case
        if not root: return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))