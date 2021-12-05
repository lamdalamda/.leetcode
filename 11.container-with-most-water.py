#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #maxarea=min(list[indexa],list[indexb])*(indexa-indexb)
        return self.maxArea_optimized(height)
        
    def maxArea_brutal(self, height: List[int]) -> int:
        #maxarea=min(list[indexa],list[indexb])*(indexa-indexb)
        
        maxarea=0
        for indexa in range(0,len(height)):
            for indexb in range(indexa+1,len(height)):
                maxarea=max(maxarea,min(height[indexa],height[indexb])*(indexb-indexa))
        return maxarea
    def maxArea_optimized(self, height: List[int]) -> int:
        #maxarea=min(list[indexa],list[indexb])*(indexa-indexb)
        indexa=0
        indexb=len(height)-1
        maxarea=min(height[indexa],height[indexb])*(indexb-indexa)
        while indexa<indexb:
            if height[indexa]<height[indexb]:
                indexa+=1
            else:

                indexb=indexb-1
            maxarea=max(maxarea,min(height[indexa],height[indexb])*(indexb-indexa))
        return maxarea
# @lc code=end

        """
        
        起始状态下indexa和indexb分别位于height的两端（0和len（height））
        此时的面积是min(height[indexa],height[indexb])*(indexb-indexa)
        
        下一个面积的indexb-indexa肯定比这个小，所以要求height更大,所以height【index】中更小的那个变成更大为止



            while height[indexa]<height[indexb] and indexa<indexb:
                indexa+=1
                maxarea=max(maxarea,min(height[indexa],height[indexb])*(indexb-indexa))
            while height[indexa]>height[indexb] and indexa<indexb:
                indexb-=1
                maxarea=max(maxarea,min(height[indexa],height[indexb])*(indexb-indexa))        
        """