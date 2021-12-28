#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        return self.fastanswers(matrix)
    def setZeroes_brutal(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    for k in range(0,n):
                        if matrix[i][k]!=0:
                            matrix[i][k]="."
                    for k in range(0,m):
                        if matrix[k][j]!=0:
                            matrix[k][j]="."
        
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==".":
                    matrix[i][j]=0        
     
    def fastanswers(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        

        horizontal_0=(0 in matrix[0])
        vertical_0=(0 in [k[0] for k in matrix])

        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,m):        
            if matrix[i][0]==0:
                matrix[i]=[0]*n
        for j in range(1,n): 
            if matrix[0][j]==0:
                for k in range(0,m):
                    matrix[k][j]=0
        
        if horizontal_0:
            matrix[0]=[0]*n
        if vertical_0:
            for k in range(0,m):
                matrix[k][0]=0
        
        
        
# @lc code=end

