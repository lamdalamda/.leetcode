#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    
    def check_duplicate(self,list_to_check):
        checklist=[]
        for i in list_to_check:
            if i in checklist and i!=".":
                return False
            checklist.append(i)
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker=[]
        for i in range(0,9):
            checklist=[]
            for j in range(0,9):
                if board[i][j] in checklist and board[i][j]!=".":
                    return False
                checklist.append(board[i][j])
            checklist=[]
            for j in range(0,9):
                if board[j][i] in checklist and board[j][i]!=".":
                    return False
                checklist.append(board[j][i])    
        for i in range(0,3):
            checklist=[]
            for m in range(0,3):
                checklist=[]
                for j in range(3*i,3*i+3):
                    for k in range(3*m,3*m+3):
                        if board[j][k] in checklist and board[j][k]!=".":
                            return False
                        checklist.append(board[j][k])                                           
        return True

# @lc code=end

