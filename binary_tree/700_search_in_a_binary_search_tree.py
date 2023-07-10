# https://leetcode.com/problems/search-in-a-binary-search-tree/

from typing import Optional
from TreeNode import TreeNode

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: return None

        if root.val < val: return self.searchBST(root.right, val)
        elif root.val > val: return self.searchBST(root.left, val)
        else: return root