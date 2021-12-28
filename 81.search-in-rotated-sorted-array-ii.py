#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)<6:
            return (target in nums)
        
        if nums[-1]>nums[0]:    
            # means there is no rotation
            low=0
            high=len(nums)-1
            while high-low>6:
                mid=int((low+high)/2)
                if nums[mid]==target:
                    return True
                if nums[mid]<target:
                    low=mid
                else:
                    high=mid
            
            return (target in nums[low:high+1])
                
        # 45678123 searching 7 
        
        # nums[-1]<=nums[0]
        # if target >= nums[-1]: on the left half
        # if target <= nums[-1]: on the right half
        low=0
        high=len(nums)-1            
        if nums[-1]==nums[0]:
            return (target in nums)
                
        
        if target >= nums[-1]:

            while high-low>6:
                mid=int((low+high)/2)
                if nums[mid]==target:
                    return True
                if nums[mid]<nums[-1]:# means that mid is in the right half:
                    # 4 5 6 7 8 0 1 2 333333333 target 5
                    high=mid
                    continue
                if nums[mid]<target:
                    low=mid
                if nums[mid]>target:
                    high=mid
            return (target in nums[low:high+1])
        if target < nums[-1]:

            while high-low>6:
                mid=int((low+high)/2)
                if nums[mid]==target:
                    return True
                if nums[mid]>nums[-1]:# means that mid is in the left half:
                    # 3333334 5 6 7 8 0 1 2 333333333 target 1
                    low=mid
                    
                    continue
                if nums[mid]<target:
                    low=mid
                if nums[mid]>target:
                    high=mid
            return (target in nums[low:high+1])            
            
        
            
# @lc code=end

