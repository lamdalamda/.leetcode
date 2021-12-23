#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start



class Solution:
    def detectrotation(self, nums: List[int], target: int) -> int:
        if nums[0]<nums[-1]:
            # distinct value
            # 0 1 2 3 4 5 6 
            return False # is not rotated
        
        return True # is rotated

    def edgecases(self, nums: List[int], target: int) -> int:
        if len(nums)<6:
            for i in range(0,len(nums)):
                if nums[i]==target:
                    return i
            return -1
        
        
    
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<6:
            for i in range(0,len(nums)):
                if nums[i]==target:
                    return i
            return -1        
        lower_bound=0
        upper_bound=len(nums)-1        
        
        if self.detectrotation(nums, target):
            # if rotated

            
            if target<nums[0]:
                # only appears at right half
                
                # 9 10 11 0 1 2 3 4 5 6 7 8 
                # serach for 1.?
                
                
                while upper_bound-lower_bound>6:
                    middle=int((upper_bound+lower_bound)/2)
                    if nums[middle]==target:
                        return middle
                    if nums[middle]>nums[0]:
                        lower_bound=middle
                        continue
                    if nums[middle]<target:
                        lower_bound=middle
                    

                    if nums[middle]>target:
                        upper_bound=middle

                for i in range(lower_bound, upper_bound+1):
                    if nums[i]==target:
                        return i
                return -1   
            else: # 只出现在左半边    
                while upper_bound-lower_bound>6:
                    middle=int((upper_bound+lower_bound)/2)
                    if nums[middle]==target:
                        return middle
                    if nums[middle]<nums[0]:
                        upper_bound=middle
                        continue
                    if nums[middle]<target:
                        lower_bound=middle
                    

                    if nums[middle]>target:
                        upper_bound=middle

                for i in range(lower_bound, upper_bound+1):
                    if nums[i]==target:
                        return i
                return -1  
        else:
            # no rotation
            while upper_bound-lower_bound>6:
                middle=int((upper_bound+lower_bound)/2)
                if nums[middle]==target:
                    return middle

                if nums[middle]<target:
                    lower_bound=middle
                
                if nums[middle]>target:
                    upper_bound=middle

            for i in range(lower_bound, upper_bound+1):
                if nums[i]==target:
                    return i
            return -1              
            
                             
        pass
        
# @lc code=end

