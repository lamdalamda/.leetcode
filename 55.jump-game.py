#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
        
    def canJump(self, nums: List[int]) -> bool:
        # only need to worry about 0
        
        # edge cases
        if len(nums) <= 1:
            return True
        
        
        maxdistance=0
        for i in range(0,len(nums)-1):
            if nums[i]!=0:
                maxdistance=max(maxdistance,i+nums[i])
            else:
                if maxdistance<=i:
                    return False
        return True
            
            
            
            
# @lc code=end

