# https://leetcode.com/problems/maximum-binary-tree/

from typing import Optional, List
from TreeNode import TreeNode

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None
        
        root_val = max(nums)
        root = TreeNode(root_val)

        seperator_idx = nums.index(root_val)

        root.left = self.constructMaximumBinaryTree(nums[:seperator_idx])
        root.right = self.constructMaximumBinaryTree(nums[seperator_idx+1:])

        return root