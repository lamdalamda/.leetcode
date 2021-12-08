#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k=0

        for pointer in range(0,len(nums)):
            if nums[pointer]!=nums[k]:
                #current=nums[pointer]
                k+=1
                nums[k]=nums[pointer]
 
        return k+1
# @lc code=end

