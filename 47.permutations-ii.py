#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            if nums[0]==nums[1]:
                return [nums]
            else:
                return [[nums[0],nums[1]],[nums[1],nums[0]]]
        nums=sorted(nums)
        results=[]
        for i in range(len(nums)):
            if i>0:
                if nums[i]==nums[i-1]:
                    continue
            tmp=nums.copy()
            tmp.pop(i)
            for j in self.permuteUnique(tmp):
                results.append(j+[nums[i]])
        
        return results
        
# @lc code=end

