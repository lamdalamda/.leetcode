#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums)<10:
            if target in nums:
                templist=[]
                for i in range(0,len(nums)):
                    if nums[i]==target:
                        templist.append(i)
                return [min(templist),max(templist)]
            else:
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
        
        smallindex=len(nums)-1
        largeindex=0
        if nums[0]!=target: 
            index1=jump
            while index1 not in index1dict:
                index1dict[index1]=nums[index1]
                jump=int((jump)/2)                         
                if nums[index1]>target:
                    index1=index1-jump
                elif nums[index1]==target:
                    smallindex=min(smallindex,index1)
                    index1=index1-jump
                else:
                    index1=index1+jump

        jump=int(len(nums)/2-0.5)   
        if nums[smallindex]!=target:
            return [-1,-1] 
        if nums[index2]!=target:
            index2=jump
            while index2 not in index2dict: 
                index2dict[index2]=nums[index2]
                jump=int((jump+1)/2) 
                if nums[index2]<target:
                    index2+=jump
                elif nums[index1]==target:
                    largeindex=max(largeindex,index2)
                    index2=index2+jump

                else:
                    index2-=jump

        return [smallindex,largeindex]
            
# @lc code=end

a=Solution()
a.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4)