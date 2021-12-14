#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def detectrotation(self, nums: List[int], target: int) -> int:
        if nums[0]<nums[-1]:
            return nums
        largest=-10000
        index1=0
        index2=len(nums)-1
        jump=int(len(nums)/2+0.5)
        while jump>1:
            jump=int(jump/2+0.5)
            if nums[index1+jump]>largest[1]:
                
    def search(self, nums: List[int], target: int) -> int:
        
# @lc code=end

