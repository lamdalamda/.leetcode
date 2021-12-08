#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return [-1,-1]
        index1=0
        index2=len(nums)-1
        jump=int(len(nums)/2-0.5)
        #binary upper limit->index1
        #binary down limit -> index2
        if nums[index1]>target or nums[index2]<target:
            return [-1,-1]
        index1dict={}
        index2dict={}
        if nums[0]!=target:
            index1=jump
            while index1 not in index1dict:
                jump=int(jump/2)                         
                if nums[index1]>=target:
                    index1=index1-jump
                else:
                    index1=index1+jump
                index1dict[index1]=nums[index1]
        jump=int((len(nums)-1-index1)/2)       
        if nums[index1]!=target:
            return [-1,-1] 
        if nums[index2]!=target:
            index2=index1+jump
            while index2 not in index2dict: 
                jump=int(jump/2)
                if nums[index2]<=target:
                    index2+=jump
                else:
                    index2-=jump
                index2dict[index2]=nums[index2]
        return [index1,index2]
            
# @lc code=end

