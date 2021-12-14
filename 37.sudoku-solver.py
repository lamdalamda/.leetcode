#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        impossible_value_dict={}
        impossible_nums_dict={}
        min_impossible=(9,(0,0))
        isvalid=True
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    impossible_value_dict[(i,j)]=[]
                    
                    impossible_nums_dict[(i,j)]=0
                    
                    for k in range(0,9):
                        if board[i][k]!=".":
                            if board[i][k] in impossible_value_dict[(i,j)]:
                                return False
                            impossible_value_dict[(i,j)].append(board[i][k])
                            impossible_nums_dict[(i,j)]+=1
                        if board[k][j]!=".":
                            if board[k][j] in impossible_value_dict[(i,j)]:
                                return False
                            impossible_value_dict[(i,j)].append(board[k][j])
                            impossible_nums_dict[(i,j)]+=1
                    for m in board[int(i/3)*3:int(i/3)*3+3][int(j/3)*3:int(j/3)*3+3]:
                        if m!=".":
                            if m in impossible_value_dict[(i,j)]:
                                return False
                            impossible_value_dict[(i,j)].append(board[k][j])
                            impossible_nums_dict[(i,j)]+=1
                    if impossible_nums_dict[(i,j)]<min_impossible[0]:
                        min_impossible=(impossible_nums_dict[(i,j)],(i,j))

        possibleboards=[]
        for i in impossible_value_dict[min_impossible[1]]:
            newboards=board
            newboards[min_impossible[1]]=i
            if self.solveSudoku(newboards)!=False:
                self.possibleboards.append(newboards)
        while True:
            
                    
        
# @lc code=end

