#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #edge cases:
        if len(obstacleGrid)==1:
             
            if max(obstacleGrid[0])==1:
                return 0
            else:
                return 1
        
        if len(obstacleGrid[0])==1:
            for i in obstacleGrid:
                if i[0]==1:
                    return 0
            return 1
        
        if obstacleGrid[-1][-2]==1 and obstacleGrid[-2][-1]==1:
            return 0
        if obstacleGrid[-1][-1]==1:
            return 0
        
        return self.uniquePaths_forward(len(obstacleGrid),len(obstacleGrid[0]),obstacleGrid)
        pass
    def uniquePaths_forward(self, m,n,obstacleGrid: List[List[int]]):
        templist=[]
        # initialize the bottom layer
        accessible=1
        for i in range(n-1,-1,-1):

            if obstacleGrid[-1][i]==1:
                accessible=0
            templist=[accessible]+templist
        # i for the horizontal and j for vertical
        nthcolumn_is_accessible=1

        for i in range(m-2,-1,-1):
            # if grid[i][-1]==1: the last column will be no longer accessible
            if obstacleGrid[i][-1]==1:
                nthcolumn_is_accessible=0
                
            templist[-1]=nthcolumn_is_accessible
            
            for j in range(n-2,-1,-1):
                # start from index=-2 ,update the templist recursively
                if obstacleGrid[i][j]==1:
                    templist[j]=0
                else:
                    templist[j]=templist[j]+templist[j+1]
        
        return templist[0]
                
        

        """
        7*3
        
        
                    1
                    1 
        1 1 1 1 1 1 1

                    1
        7 6 5 4 3 2 1 
        1 1 1 1 1 1 1

7*4

                  3->1
                  |  
        7 6 5 4 3 2 1 
        1 1 1 1 1 1 1
        
        """
    
# @lc code=end

a=Solution()
a.uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0]])