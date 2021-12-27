#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        shu=len(grid)-1
        heng=len(grid[0])-1
        for i in range(heng-1,-1,-1):
            # 最底下这行
            grid[shu][i]+=grid[shu][i+1]
        for j in range(shu-1,-1,-1):
            # 最右边这列
            grid[j][heng]+=grid[j+1][heng]
            
        for i in range(shu-1,-1,-1):
            for j in range(heng-1,-1,-1):
                grid[i][j]+=min(grid[i+1][j],grid[i][j+1])    
        return grid[0][0]
            
            
# @lc code=end

a=Solution()
a.minPathSum([[1,3,1],[1,5,1],[4,2,1]])