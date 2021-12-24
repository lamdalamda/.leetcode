#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def swap(self,matrix,index1,index2):
        tmp=matrix[index1[0]][index1[1]]
        matrix[index1[0]][index1[1]]=matrix[index2[0]][index2[1]]
        matrix[index2[0]][index2[1]]=tmp
    def rotate(self, matrix: List[List[int]]) -> None:
        return self.rotate_assign(matrix)
    def rotate_swap(self, matrix: List[List[int]]) -> None:
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_length = len(matrix)
        center_position= (len(matrix)/2,len(matrix)/2)
        
        max_index=len(matrix)-1

        
        
        
        for i in range(0,int(matrix_length/2)):
            for j in range(0,int(matrix_length/2+0.5)):
                # upper left half
                # consider n=odd
                
                # for example n=5
                # then swap everything in the (0:2,0:3) range
                current_position=(i,j)# for example  0,1
                relative_current_position=(i-len(matrix)/2,len(matrix)/2-j)# (for example -2,3)
                
                """
                *1*|***
                ***|**2
                ***|***
                -------
                ***|***
                4**|***
                ***|*3*

            
                swap 12, swap 34, swap13 (position)       
                
                """
                
 
                # i=0,j=1
                
                self.swap(matrix,(i,j),(j,max_index-i))
                self.swap(matrix,(max_index-j,i),(max_index-i,max_index-j))
                self.swap(matrix,(i,j),(max_index-i,max_index-j))
                

        return matrix  

    def rotate_assign(self, matrix: List[List[int]]) -> None:
        
        """
        Do not return anything, modify matrix in-place instead.
        """

        max_index=len(matrix)-1

        for i in range(0,int(len(matrix)/2)):
            for j in range(0,int(len(matrix)/2+0.5)):
    
                
                """
                *1*|***
                ***|**2
                ***|***
                -------
                ***|***
                4**|***
                ***|*3*

               assign:
                *4*|***
                ***|**1
                ***|***
                -------
                ***|***
                3**|***
                ***|*2*  
                
                """
                
                #oldvalues=(matrix[i][j],matrix[j][max_index-i],matrix[max_index-j][i],matrix[max_index-i][max_index-j])
                #matrix[i][j]=oldvalues[3]
                #matrix[j][max_index-i]=oldvalues[0]
                #matrix[max_index-j][i]=oldvalues[1]
                #matrix[max_index-i][max_index-j]=oldvalues[2]
                #oldvalues=(matrix[max_index-j][i],matrix[i][j],matrix[max_index-i][max_index-j],matrix[j][max_index-i])
                matrix[i][j],matrix[j][max_index-i],matrix[max_index-j][i],matrix[max_index-i][max_index-j]=(matrix[max_index-j][i],matrix[i][j],matrix[max_index-i][max_index-j],matrix[j][max_index-i])
        return matrix    
        
        
        
        
        

# @lc code=end

