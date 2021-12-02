#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target: int):
        hashdict={}

        for i in range(0, len(nums)):
          
            if nums[i] in hashdict:
                return [i,hashdict[nums[i]]]
            hashdict[target-nums[i]]=i
   
            
# @lc code=end

