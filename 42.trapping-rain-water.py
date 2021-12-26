#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List
# @lc code=start



class Solution:
    def trap(self, height: List[int]) -> int: 
        return self.trap1(height)
    def trap1(self, height: List[int]) -> int:    
        
        totalarea=0

        leftindex=0
        rightindex=len(height)-1
        
        left_maxheight_index=0
        right_maxheight_index=len(height)-1
        

        while rightindex>leftindex:
            if height[leftindex]<height[rightindex]:
                leftindex=leftindex+1
                if height[leftindex]<height[left_maxheight_index]:
                    totalarea-=height[leftindex]
                else:
                    totalarea+=height[left_maxheight_index]*(leftindex-left_maxheight_index-1)
                    left_maxheight_index=leftindex

            else:
                rightindex=rightindex-1
                if height[rightindex]<height[right_maxheight_index]:
                    totalarea-=height[rightindex]
                else:
                    totalarea+=height[right_maxheight_index]*(right_maxheight_index-rightindex-1)
                    right_maxheight_index=rightindex
                    height[right_maxheight_index]=height[rightindex]
        return totalarea
                
        
        pass
    def trap2(self, height: List[int]) -> int:
        

        for i in range(0,len(height)):
            if height[i] > maxheight[0]:
                maxheight=[height[i],i]
        
        lefthalf=[(height[0],0)]
        righthalf=[(height[-1],len(height)-1)]
        blocks=0
        totalarea=0
        
                
        if maxheight[1]!=0:
        
            for i in range(1,maxheight[1]):
                if height[i]>lefthalf[-1][0]:
                    lefthalf.append((height[i],i))
                else:
                    blocks+=height[i]

            lefthalf.append(maxheight)

            for i in range(0,len(lefthalf)-1):
                totalarea+=lefthalf[i][0]*(lefthalf[i+1][1]-lefthalf[i][1]-1)
                
        if maxheight[1]!=len(height)-1:
        
            for i in range(len(height)-2,maxheight[1],-1):
                if height[i]>righthalf[-1][0]:
                    righthalf.append((height[i],i))
                else:
                    blocks+=height[i]
                
            righthalf.append(maxheight)

            for i in range(0,len(righthalf)-1):
                totalarea+=righthalf[i][0]*(righthalf[i][1]-righthalf[i+1][1]-1)

        
        totalarea-=blocks
        return totalarea
        
        
        
# @lc code=end

a=Solution()
a.trap([0,1,0,2,1,0,1,3,2,1,2,1])
