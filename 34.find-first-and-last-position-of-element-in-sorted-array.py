#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start

class Solution:
    def largest2power(self,len=32):
        result=0
        is2power=0
        while len>1:
            if len%2==1:
                is2power=1
            result+=1
            len=int(len/2)
        return (2**(result+is2power))
            
    
    def searchRange(self, nums,target: int):

        if len(nums)<10:
            if target in nums:
                templist=[]
                for i in range(0,len(nums)):
                    if nums[i]==target:
                        templist.append(i)
                return [min(templist),max(templist)]
            else:
                return [-1,-1]
        lowerindex=0
        
        temp=self.largest2power(len(nums))
        
        jump=temp
        if nums[lowerindex]!=target:
            while jump>1:
                jump=int(jump/2)
                if jump+lowerindex<len(nums) and nums[jump+lowerindex]<target:
                    lowerindex=jump+lowerindex
            lowerindex=lowerindex+1
        if nums[lowerindex]!=target:
            return [-1,-1]
        
        upperindex=len(nums)-1
        
        temp=self.largest2power(len(nums))        
        
        jump=temp
        if nums[upperindex]!=target:
            while jump>1:
                jump=int(jump/2)
                if upperindex-jump >0 and nums[upperindex-jump]>target:
                    upperindex=upperindex-jump
            upperindex=upperindex-1        
        
        
        return [lowerindex,upperindex]
# @lc code=end

a=Solution()
a.searchRange([0,1,2,3,3,4,4,5,5,6,6,7,7,7,9,9,11,11,11,12,12,12,12],12)