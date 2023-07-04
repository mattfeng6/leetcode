# https://leetcode.com/problems/path-sum-ii/

from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        # Backtracking

        res = []
        if not root: return res

        path = []
        def currList(curr, targetSum, path, res):
            path.append(curr.val)
            if not curr.left and not curr.right and targetSum == curr.val:
                res.append(list(path))
            
            if curr.left:
                currList(curr.left, targetSum-curr.val, path, res)
            if curr.right:
                currList(curr.right, targetSum-curr.val, path, res)
            path.pop()

        currList(root, targetSum, path, res)
        return res