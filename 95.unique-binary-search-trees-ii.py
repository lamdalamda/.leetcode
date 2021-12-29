#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.



class Solution:
    def generateTrees(self, n: int) -> List:
        
    def inner(self,sorted_list_0_n=[]):
        if len(sorted_list_0_n) <2:
            raise ValueError
        
        return [TreeNode()]
    
    
        
# @lc code=end

