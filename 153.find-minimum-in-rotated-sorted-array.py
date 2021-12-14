#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1]:
            return nums[0]
        if len(nums)<5:
            return min(nums)
        smallest=nums[-1]
        index1=0
        index2=len(nums)-1

        medium=int((index1+index2)/2)
        if nums[medium]>=smallest:
            return self.findMin(nums[medium:])
        else:
            # 7 8 0 1 2 3 4 5 6
            return self.findMin(nums[0:medium+1])

        
        
# @lc code=end

