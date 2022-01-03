#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums=sorted(nums)

            
            
        return self.subsetsWithDup1((nums))
    def subsetsWithDup1(self, nums: List[int],indexdict={}) -> List[List[int]]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [[],nums]
        if max(nums)==min(nums):
            result=[]
            for i in range(0,len(nums)+1):
                result.append([nums[0]]*i)
            return result
        counter=0
        for j in range(0,len(nums)):
            if nums[j]!=nums[0]:
                
                break
            counter+=1
        result=[]
        for i in range(0,j+1):
            for k in self.subsetsWithDup1(nums[j:]):
                result.append([nums[0]]*i+k)
        
        
        return result        
                

            
# @lc code=end

