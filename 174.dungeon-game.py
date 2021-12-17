#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    def edgecases(self,dungeon):
        if len(dungeon)==1 and len(dungeon[0])==1:
            return max(-dungeon[0][0]+1,1),True
        return 0,False
    
    def calculateMinimumHP(self, dungeon) -> int:
        return self.calculateMinimumHP1(dungeon)
    def calculateMinimumHP1(self, dungeon) -> int:        
        # use for loops

        """            
        3*4 dungeon
        
        ****
        ****
        ****
        
        """
             
        # initial run
        dungeon[-1][-1]=max(1,-dungeon[len-1][len-1]+1)
        """            
        3*4 dungeon
        
        ****
        ****
        ***-
        
        """
        # bottom row:
        for j in range(2,len(dungeon[0])+1):

            dungeon[-1][-j]=max(dungeon[-1][-j+1]-dungeon[-1][-j],1)            
        """            
        3*4 dungeon
        
        ****
        ****
        ----
        
        """            

        # rightmost column
        for i in range(2,len(dungeon)+1):
            dungeon[-i][-1]=max(dungeon[-i+1][-1]-dungeon[-i][-1],1)      
        """            
        3*4 dungeon
        
        ***-
        ***-
        ----
        
        """            
 
        for i in range(2,len(dungeon)+1): 
            for j in range(2,len(dungeon[0])+1):

                dungeon[-i][-j]=max(min(dungeon[-i+1][-j],dungeon[-i][-j+1])-dungeon[-i][-j],1)

        return dungeon[0][0]        
    def calculateMinimumHP2(self, dungeon) -> int:
        
        # use while and record dict
        if self.edgecases(dungeon)[1]:
            return self.edgecases(dungeon)[0]
        """
        3*4 dungeon
        
        ****
        ****
        ****
        
        """
        """
        ***-
        **--
        *---
        """       
        
        dungeon[len(dungeon)-1][len(dungeon[0])-1]=max(1,-dungeon[len(dungeon)-1][len(dungeon[0])-1]+1)
        calculated_dict={(len(dungeon)-1,len(dungeon[0])-1):dungeon[len(dungeon)-1][len(dungeon[0])-1]}
        new_positions=[]
        if len(dungeon)-2>=0:
            new_positions.append((len(dungeon)-2,len(dungeon[0])-1))
        if len(dungeon[0])-2>=0:
            new_positions.append((len(dungeon)-1,len(dungeon[0])-2))



        while len(new_positions)!=0:
            # update the minimum HP requirements
            for i in new_positions:
                if i in calculated_dict:
                    continue
                criterions=[]

                if i[0]+1<=len(dungeon)-1:
                    
                    
                    criterions.append(dungeon[i[0]+1][i[1]])
                if i[1]+1<=len(dungeon[0])-1:
                    criterions.append(dungeon[i[0]][i[1]+1])
                dungeon[i[0]][i[1]]=max(min(criterions)-dungeon[i[0]][i[1]],1)
                calculated_dict[i]=dungeon[i[0]][i[1]]
                
            # get new positions to calculate
            to_calculate_positions=new_positions
            new_positions=[]
            for i in to_calculate_positions:
                if i[0]-1>=0:
                    new_positions.append((i[0]-1,i[1]))
                if i[1]-1>=0:
                    new_positions.append((i[0],i[1]-1))
        return dungeon[0][0]
        
# @lc code=end


testinput=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
a=Solution()
a.calculateMinimumHP(testinput)
