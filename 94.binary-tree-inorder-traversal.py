#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # edgecases
        if root is None:
            return []

        return self.inorderTraversal_recursive(root)
        
        pass
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        leftmostpointer=root
        
        pass
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        if root.left is None and root.right is None:
            return [root.val]
        if root.right is None:
            return self.inorderTraversal_recursive(root.left)+[root.val]
        if root.left is None:
            return [root.val]+self.inorderTraversal_recursive(root.right)
        
        return self.inorderTraversal_recursive(root.left)+[root.val]+self.inorderTraversal_recursive(root.right)
         
        
        
                
# @lc code=end

