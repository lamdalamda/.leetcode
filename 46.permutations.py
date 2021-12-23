#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [[nums[0],nums[1]],[nums[1],nums[0]]]
        
        results=[]
        for i in range(len(nums)):
            tmp=nums.copy()
            tmp.pop(i)
            for j in self.permute(tmp):
                results.append(j+[nums[i]])
        
        return results
        
# @lc code=end

