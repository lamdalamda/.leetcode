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
        index1=0
        index2=0
        halfindex=int(len(nums)/2)
        sorted_subarray1=self.mergesort(nums[0:halfindex])
        sorted_subarray2=self.mergesort(nums[halfindex:])
        result=[]
        while index1<len(sorted_subarray1) or index2<len(sorted_subarray2):
            if index2 >=len(sorted_subarray2):
                result.append(sorted_subarray1[index1])
                index1+=1
                continue
            if index1 >=len(sorted_subarray1):
                result.append(sorted_subarray2[index2])
                index2+=1
                continue
            if sorted_subarray1[index1]<=sorted_subarray2[index2]:
                result.append(sorted_subarray1[index1])
                index1+=1
                continue
            else:
                result.append(sorted_subarray2[index2])
                index2+=1
                continue
        return result
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
