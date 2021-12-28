#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        #nums>=3
        checkingindex=1
        moving_to_index=1
        thisnumber_count=True 
        # 1st appear: unknown->True. secondappear: True->False. 3rd appear:get the false status
        
        current_number=nums[0]
        for checkingindex in range(1,len(nums)):
            if nums[checkingindex]==current_number:
                if thisnumber_count:
                    # this is the 2nd appearance
                    thisnumber_count=False
                    nums[moving_to_index]=current_number
                    moving_to_index+=1
                else:
                    # means that this is at least 3rd appearance
                    
                    pass
                
            else:
                current_number=nums[checkingindex]
                thisnumber_count=True
                nums[moving_to_index]=current_number
                moving_to_index+=1
        return moving_to_index

# @lc code=end

