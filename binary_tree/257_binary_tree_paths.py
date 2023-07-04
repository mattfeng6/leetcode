# https://leetcode.com/problems/binary-tree-paths/

from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # backtracking

        res = []
        path = []

        if not root: return res

        def traversal(cur, path, res):
            path.append(cur.val)
            if not cur.left and not cur.right:
                sPath = '->'.join(map(str, path))
                res.append(sPath)
                return
            if cur.left:
                traversal(cur.left, path, res)
                path.pop()
            if cur.right:
                traversal(cur.right, path, res)
                path.pop()


        traversal(root, path, res)
        return res

        