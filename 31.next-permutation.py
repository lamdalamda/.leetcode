#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start



# what is  lexicographically next greater permutation??
class Solution:
    def mergesort(self,nums):
        if len(nums)==1:
            return nums
        if len(nums)==2:
            if nums[0]<=nums[1]:
                return nums
            return [nums[1],nums[0]]
        resultlist = []
        part1=self.mergesort(nums[0:int(len(nums)/2)])
        part2=self.mergesort(nums[int(len(nums)/2):])
        while len(part1)!=0 or len(part2)!=0:
            if len(part1)==0:
                resultlist.extend(part2)
                break
            if len(part2)==0:
                resultlist.extend(part1)
                break
            if part1[0]<part2[0]:
                resultlist.append(part1.pop(0))
                continue
            resultlist.append(part2.pop(-1))
             
        
        
    def nextPermutation1(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums==self.mergesort(nums):
            for i in range(0,len(nums)-1):
                if nums[len(nums)-1-i]!=nums[len(nums)-2-i]:
                    temp=nums[len(nums)-1-i]
                    nums[len(nums)-1-i]=nums[len(nums)-2-i]
                    nums[len(nums)-2-i]=temp
                    return nums
        else:
            nums=self.mergesort(nums)
    def nextPermutation(self, nums):
        change=False
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    swap=nums[j]
                    nums[j]=nums[i]
                    nums[i]=swap
                    change=True
        if change==False:
            for i in range(0,len(nums)-1):
                if nums[len(nums)-1-i]!=nums[len(nums)-2-i]:
                    temp=nums[len(nums)-1-i]
                    nums[len(nums)-1-i]=nums[len(nums)-2-i]
                    nums[len(nums)-2-i]=temp
                    return            
                            
# @lc code=end
