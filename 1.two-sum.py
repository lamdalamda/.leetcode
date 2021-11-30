#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lennums=len(nums)
        for i in range(0,lennums):
            for j in range(i+1,lennums):
                if nums[j]+nums[i] == target:
                    return ([i,j])
            
            
# @lc code=end

