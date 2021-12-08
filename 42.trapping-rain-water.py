#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        maxheight=max(height)
        heightdict={}
        for i in range(0,maxheight):
            heightdict[i]=[]
        for i in range(0,len(height)):
            for j in range(0,height[i]):
                heightdict[j].append(i)
        water=0    
        for i in heightdict:
            if len(heightdict[i])>=2:
                water+=heightdict[i][-1]-heightdict[i][0]+1-len(heightdict[i])
        return water
# @lc code=end

