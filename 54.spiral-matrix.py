#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List

# very good practice for list index and range


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.inner(matrix,0)
    def inner(self, matrix: List[List[int]],direction=0):
        
        if len(matrix)==0:
            return []
        if len(matrix[0])==0:
            return []
        if direction==0:
            return matrix.pop(0)+self.inner(matrix,1)
        if direction==1:
            return [i.pop(-1) for i in matrix]+self.inner(matrix,2)
        if direction==2:
            return matrix.pop(-1)[::-1]+self.inner(matrix,3)
        if direction==3:
            return [i.pop(0) for i in matrix][::-1]+self.inner(matrix,0)
        
        
# @lc code=end

